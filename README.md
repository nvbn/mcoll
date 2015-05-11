# Modern collections api for Python

## Examples

```python
In [0]: from mcoll import t

In [1]: t.into([t.filter(lambda x: x > 5),
                t.map(lambda x: x ** 2),
                t.merge(range(5)),
                t.slice(1, stop=15, step=12),
                t.zip(range(15)),
                t.map(lambda xy: (chr(xy[0]+ 60), xy[1])),
                dict], range(100))
Out[1]: {'m': 0, 'ƥ': 1}
```
