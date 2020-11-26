from models.get_model import get_mongo, DB_NAME


def get_lvl_from_speed(speed):
    if speed < 20:
        return 3
    elif speed < 40:
        return 2
    elif speed < 60:
        return 1
    else:
        return 0


def get_speed_from_lvl(lvl):
    lvls = {3: (0, 20), 2: (20, 40), 1: (40, 60), 0: (60, 100)}
    return lvls[lvl]


def get_ways(min_lvl, max_lvl, name):
    db = get_mongo()[DB_NAME]
    ways = db.ways
    speed_limit = (get_speed_from_lvl(max_lvl)[0], get_speed_from_lvl(min_lvl)[1])
    if name == '':
        res = ways.find(
            {
                'avg_speed':
                    {
                        '$gte': speed_limit[0],
                        '$lte': speed_limit[1]
                    }
            }
        )
    else:
        res = ways.find(
            {
                'tags.name': {'$regex': name},
                'avg_speed':
                    {
                        '$gte': speed_limit[0],
                        '$lte': speed_limit[1]
                    }
            }
        )
    return res


def check_name(tags):
    if 'name' in tags:
        return tags['name']
    else:
        return 'Noname'
