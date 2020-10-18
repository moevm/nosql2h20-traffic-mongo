from models.get_model import get_mongo, DB_NAME

# this is mongo!
db = get_mongo()[DB_NAME]


def find_paths(x0, y0, x1, y1):
    nodeid_from = find_nearest_node(x0,y0)
    return [[x0, y0], [x1, y1], [59.9180, 30.3088]]
    # Should returns array of ways
    # request to db | some algortms

def find_nearest_node(x, y):
    dbnodes = db.nodes
