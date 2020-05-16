from typing import NewType, Tuple
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

    double_x: Pipe[Dict, Dict] = to(lambda p: {'x': p['x'] * 2, 'y': p['y']})
    double_y: Pipe[Dict, Dict] = to(lambda p: {'x': p['x'], 'y': p['y'] * 2})

    (
        open('points.json')
        - json_loads()
        + [
            double_x,
            double_y,
        ]
        > log()
    )
