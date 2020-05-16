from typing import Tuple
from plmbr.pipes import *
from plmbr.pipe import Pipe

if __name__ == '__main__':
    point = Tuple[int, int]

    (
        zip(range(5), range(5))
        - keep[point](lambda p: p[0] >= 2)
        - to[point, Dict](lambda p: {'x': p[0], 'y': p[1]})
        - json_dumps()
        > save('points.json')
    )

    (
        open('points.json')
        - json_loads()
        + [
            same[Dict](),
            to(lambda p: {'x': p['x'] * 2, 'y': p['y']}),
            to(lambda p: {'x': p['x'] * 2, 'y': p['y']}),
        ]
        > log()
    )
