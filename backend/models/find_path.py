from models.get_model import get_mongo, DB_NAME
import numpy

# this is mongo!
db = get_mongo()[DB_NAME]
FIND_RANGE = 0.001


def find_paths(x0, y0, x1, y1):
    nodeid_from = find_nearest_node(x0, y0)
    return [[x0, y0], [nodeid_from['lat'], nodeid_from['lon']], [x1, y1]]
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
    min = 1
    for node in nodes:
        b = numpy.array([node['lat'], node['lon']])
        if numpy.linalg.norm(a - b) < min:
            res = node
    return res

