from models.get_model import get_mongo, DB_NAME
import numpy

# this is mongo!
db = get_mongo()[DB_NAME]
FIND_RANGE = 0.001


def find_paths(x0, y0, x1, y1):
    nodeid_from = find_nearest_node(x0, y0)
    nodeid_to = find_nearest_node(x1, y1)
    way = find_way(nodeid_from, nodeid_to)
    if not (nodeid_from is None) or not (nodeid_to is None):
        return [[x0, y0]] + way + [[x1, y1]]
    else:
        return [[x0, y0], [x1, y1]]
    # Should returns array of ways
    # request to db | some algortms

def find_nearest_node(x, y):
    dbnodes = db.nodes
    nearest_nodes = dbnodes.find({
        'lon': {
            '$gt': y - FIND_RANGE,
            '$lt': y + FIND_RANGE
        },
        'lat': {
            '$gt': x - FIND_RANGE,
            '$lt': x + FIND_RANGE
        },
        'in_ways': {
            '$ne': []
        }
    })
    return find_min_distance(x, y, nearest_nodes)


def find_min_distance(x0, y0, nodes):
    a = numpy.array([x0, y0])
    res = None
    min = 1
    for node in nodes:
        useless_node = True
        way_ids = node['in_ways']
        for way_id in way_ids:
            way = db.ways.find_one({'_id': way_id})
            if way is None:
                print('Error: way {} does not match (find_nearest_node)'.format(way_id))
            else:
                if 'maxspeed' in way['tags'].keys():
                    useless_node = False
                    break
        if useless_node:
            continue
        b = numpy.array([node['lat'], node['lon']])
        if numpy.linalg.norm(a - b) < min:
            res = node['_id']
    return res


def find_way(nodeid_from, nodeid_to):
    nodes_list = [(0.0, nodeid_from, nodeid_from)]
    passed_nodes = {}
    curr = nodeid_from
    i = 0
    print("STAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAART")
    is_found = False
    while len(nodes_list) > 0:
        nodes_list = sorted(nodes_list, key=lambda node: node[0])
        curr_el = nodes_list.pop(0)
        curr = curr_el[1]
        i += 1
        print(nodes_list)
        passed_nodes[curr] = curr_el[2]
        if curr == nodeid_to:
            is_found = True
            print("Пришли!")
            break
        neighb_nodes = get_neighb_nodes(curr)
        for node in neighb_nodes:
            if node in passed_nodes.keys():
                print('Уже был!')
                continue
            nodes_list.append((get_distance(curr, node), node, curr))
    if is_found:
        res = find_back_path(nodeid_from, nodeid_to, passed_nodes)
        res = [get_node_coords(i) for i in res]
        return res
    else:
        return [get_node_coords(nodeid_from), get_node_coords(nodeid_to)]


def get_neighb_nodes(node_id):
    node = db.nodes.find_one({'_id': node_id})
    res = []
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
    print(passed_nodes)
    res = []
    while curr != nodeid_from:
        res.append(curr)
        curr = passed_nodes[curr]
        print(res)
    res.append(curr)
    res.reverse()
    return res


def get_node_coords(node_id):
    node = db.nodes.find_one({'_id': node_id})
    if node is None:
        return None
    else:
        return [node['lat'], node['lon']]


def get_distance(node1_id, node2_id):
    a = numpy.array(get_node_coords(node1_id))
    b = numpy.array(get_node_coords(node2_id))
    return numpy.linalg.norm(a - b)

