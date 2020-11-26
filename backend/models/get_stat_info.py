from flask import g
from models.get_model import get_mongo, DB_NAME
from models.find_ways import get_speed_from_lvl


def get_last_path_ways():
    ways = get_ways(g.last_path)
    return ways


def get_ways(nodes):
    ways = []
    for i in range(len(nodes) - 1):
        comm_way = find_common_way(nodes[i], nodes[i+1])
        ways.append(comm_way)
    return ways


def find_common_way(node_id1, node_id2):
    db = get_mongo()[DB_NAME]
    way = db.ways.find_one(
        {
            'nodes': {
                '$all': [node_id1, node_id2]
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
