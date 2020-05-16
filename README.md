# plmbr

Type safe, reusable pipes to process streams of data.

```python
from plmbr.pipes import *

if __name__ == '__main__':
    double: Pipe[int, int] = transform(lambda i: i * 2)
    ge5: Pipe[int, int] = keep(lambda i: i >= 5)

    (
        range(10)
        - ge5
        dou
        > log()

    )
```