from models.get_stat_info import get_last_path_ways, get_traffic_stat
from models.find_ways import get_lvl_from_speed
from flask import g


def get_stat_info():
    ways = get_last_path_ways()
    avg = 0
    avg_speed = 0
    for way in ways:
        speed = way['avg_speed']
        avg_speed += speed
        avg += get_lvl_from_speed(speed)
    avg /= len(ways)
    data = []
    for i in range(len(ways)):
        data.append(
            {'id': ways[i]['_id'],
             'time': ways[i]['avg_speed'] * g.last_path_len[i],
             'trafficJamLevel': get_lvl_from_speed(ways[i]['avg_speed'])
             }
        )
    time = sum([el['time'] for el in data])
    result = {
        'avgTime': time,
        'avgLevel': avg,
        'data': data,
        'generalData': get_traffic_stat()
    }
    print(result)
    return result
