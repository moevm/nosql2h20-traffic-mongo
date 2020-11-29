from models.get_stat_info import get_last_path_ways, get_traffic_stat
from models.find_ways import get_lvl_from_speed
import json

EPS = 0.01


def get_stat_info(category):
    print("Start getting statistics, category: {}".format(category))
    ways = get_last_path_ways(category)
    avg = 0
    avg_speed = 0
    for way in ways:
        speed = way['avg_speed']
        avg_speed += speed
        avg += get_lvl_from_speed(speed)
    if len(ways) != 0:
        avg /= len(ways)
    try:
        with open('last_path_len.json') as file:
            last_path_len = json.load(file)
            last_path_len = last_path_len['last_path_lens']
    except BaseException:
        last_path_len = []
    data = []
    for i in range(len(ways)):
        data.append(
            {'id': ways[i]['_id'],
             'time': last_path_len[i] / (ways[i]['avg_speed'] + EPS),
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
    return result
