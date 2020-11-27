from models.find_path import find_paths


def find_paths_from_one_point_to_another_point(x0, y0, x1, y1):
    res = find_paths(x0, y0, x1, y1)
    if len(res) == 2:
        return [
            {'error': 'Cannot find path (probably, the nearest node is not the part of road)'}
        ]
    else:
        return [
            {
                "way": res
            }
        ]
