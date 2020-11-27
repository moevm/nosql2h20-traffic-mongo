import json
from models.get_model import get_mongo, DB_NAME
from models.find_ways import get_speed_from_lvl


def get_last_path_ways(category):
    try:
        with open('last_path.json') as file:
            last_path = json.load(file)
            last_path = [el[f'{i}'] for i, el in enumerate(last_path)]
    except BaseException as err:
        print(err)
        return []
    ways = get_ways(last_path, category)
    return ways


def get_ways(nodes, category):
    ways = []
    for i in range(len(nodes) - 1):
        comm_way = find_common_way(nodes[i], nodes[i+1], category)
        if comm_way is not None:
            ways.append(comm_way)
    return ways


def find_common_way(node_id1, node_id2, category):
    db = get_mongo()[DB_NAME]
    speed_limit = (get_speed_from_lvl(category[1])[0], get_speed_from_lvl(category[0])[1])
    way = db.ways.find_one(
        {
            'nodes': {
                '$all': [node_id1, node_id2]
            },
            'avg_speed':
                {
                    '$gte': speed_limit[0],
                    '$lte': speed_limit[1]
                }
        }
    )
    return way


def get_traffic_stat():
    return [get_lvl_count(i) for i in range(4)]


def get_lvl_count(lvl):
    speed = get_speed_from_lvl(lvl)
    ways = get_mongo()[DB_NAME].ways
    res = ways.find(
        {
            'avg_speed':
                {
                    '$gte': speed[0],
                    '$lte': speed[1]
                }
        }
    ).count()
    return res
