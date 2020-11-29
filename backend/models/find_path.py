from models.get_model import get_mongo, DB_NAME
from math import radians
import json
import numpy
# this is mongo!
db = get_mongo()[DB_NAME]
FIND_RANGE = 0.001

CORRECT_HIGHWAY_TAGS = ['motorway', 'motorway_link', 'trunk', 'trunk_link', 'primary', 'primary_link', 'secondary',
                        'secondary_link', 'tertiary', 'tertiary_link', 'unclassified', 'unclassified_link',
                        'residential', 'residential_link', 'living_street']

def find_paths(x0, y0, x1, y1):
    nodeid_from = find_nearest_node(x0, y0)
    nodeid_to = find_nearest_node(x1, y1)
    way = find_way(nodeid_from, nodeid_to)
    if (nodeid_from is None) or (nodeid_to is None) or (way == []):
        return [[x0, y0], [x1, y1]]
    else:
        return [[x0, y0]] + way + [[x1, y1]]


def find_nearest_node(x, y):
    dbnodes = db.nodes
    nearest_nodes = []
    range = FIND_RANGE
    nearest_node = None
    while nearest_node is None:
        nearest_nodes = list(dbnodes.find({
            'lon': {
                '$gt': y - range,
                '$lt': y + range
            },
            'lat': {
                '$gt': x - range,
                '$lt': x + range
            },
            'in_ways': {
                '$ne': []
            }
        }))
        range += FIND_RANGE
        nearest_node = find_min_distance(x, y, nearest_nodes)
    return nearest_node


def find_min_distance(x0, y0, nodes):
    a = numpy.array([x0, y0])
    res = None
    min_dist = 1
    for node in nodes:
        useless_node = True
        way_ids = node['in_ways']
        for way_id in way_ids:
            way = db.ways.find_one({'_id': way_id})
            if way is None:
                print('Error: way {} does not match (find_min_distance)'.format(way_id))
            else:
                if 'highway' in way['tags'].keys():
                    if way['tags']['highway'] in CORRECT_HIGHWAY_TAGS:
                        useless_node = False
                        break
        if useless_node:
            continue
        b = numpy.array([node['lat'], node['lon']])
        dist = numpy.linalg.norm(a - b)
        if dist < min_dist:
            res = node['_id']
            min_dist = dist
    return res


def find_way(nodeid_from, nodeid_to):
    nodes_list = [(0.0, nodeid_from, nodeid_from)]
    passed_nodes = {}
    print(f'Searching for way: from {nodeid_from} to {nodeid_to}')
    is_found = False
    while len(nodes_list) > 0:
        nodes_list = sorted(nodes_list, key=lambda node: node[0])
        curr_el = nodes_list.pop(0)
        curr = curr_el[1]
        passed_nodes[curr] = curr_el[2]
        if curr == nodeid_to:
            is_found = True
            print("Way was found!")
            break
        if len(nodes_list) > 20000:
            is_found = False
            break
        neighb_nodes = get_neighb_nodes(curr)
        for node in neighb_nodes:
            if node in passed_nodes.keys():
                continue
            nodes_list.append((get_distance(nodeid_to, node), node, curr))
    if is_found:
        res = find_back_path(nodeid_from, nodeid_to, passed_nodes)
        with open('last_path.json', 'w') as file:
            last_path = [{f'{i}': val} for i, val in enumerate(res)]
            json.dump(last_path, file)
        res = [get_node_coords(i) for i in res]
        with open('last_path_len.json', 'w') as file:
            last_path_len = find_path_len(res)
            last_path = {'last_path_lens': last_path_len}
            json.dump(last_path, file)
        print(f'Way length is {sum(last_path_len)}')
        return res
    else:
        print('Cannot find way!')
        return [get_node_coords(nodeid_from), get_node_coords(nodeid_to)]


def get_neighb_nodes(node_id):
    node = db.nodes.find_one({'_id': node_id})
    res = []
    if node is None:
        return res
    for way_id in node['in_ways']:
        way = db.ways.find_one({'_id': way_id})
        if 'maxspeed' not in way['tags'].keys():
            continue
        nodes_in_way = way['nodes']
        index = nodes_in_way.index(node_id)
        if index is 0:
            res.append(nodes_in_way[index+1])
        elif index is len(nodes_in_way)-1:
            res.append(nodes_in_way[index-1])
        else:
            res.append(nodes_in_way[index + 1])
            res.append(nodes_in_way[index-1])
    return res


def find_back_path(nodeid_from, nodeid_to, passed_nodes):
    curr = nodeid_to
    print('From {}'.format(nodeid_from))
    print('To {}'.format(nodeid_to))
    res = []
    while curr != nodeid_from:
        res.append(curr)
        curr = passed_nodes[curr]
    res.append(curr)
    res.reverse()
    return res


def get_node_coords(node_id):
    node = db.nodes.find_one({'_id': node_id})
    if node is None:
        print('get_node_coords: Node is not found (node_id={})'.format(node_id))
        return None
    else:
        return [node['lat'], node['lon']]


def get_distance(node1_id, node2_id):
    a = numpy.array(get_node_coords(node1_id))
    b = numpy.array(get_node_coords(node2_id))
    return numpy.linalg.norm(a - b)


def find_path_len(path):
    l = []
    R = 6371
    for i in range(len(path) - 1):
        lat1, lat2 = (path[i][0], path[i+1][0])
        lon1, lon2 = (path[i][1], path[i + 1][1])
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        sin1 = numpy.sin((lat1 - lat2) / 2)
        sin2 = numpy.sin((lon1 - lon2) / 2)
        l.append(2 * R * numpy.arcsin(numpy.sqrt(sin1 * sin1 + sin2 * sin2 * numpy.cos(lat1) * numpy.cos(lat2))))
    return l
