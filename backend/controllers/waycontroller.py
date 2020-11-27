from models.find_ways import get_ways, get_lvl_from_speed, check_name


def get_ways_info(min_jam, max_jam, name):
    if not (-1 < min_jam < max_jam < 4):
        min_jam = 0
        max_jam = 3
    ways = get_ways(min_jam, max_jam, name)
    return [
        {
            "id": el['_id'],
            "name": check_name(el['tags']),
            "traffic_jam_level": get_lvl_from_speed(el['avg_speed'])
        }
        for el in ways]
