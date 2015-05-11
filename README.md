# Modern API for Python collections

## Rationale

In Python we have such a good functions like `map`, `reduce`, `filter` and
others for manipulations with collections, but using more then two-three
of them is an unreadable mess:

```python
reduce(operator.add,
       filter(lambda x: x > 5,
              map(lambda x: x.value, coll)))
```

For comprehensions/generator expressions makes it a bit better:

```python
reduce(operator.add,
       (x[0] + x[1]
       for x in zip((x.value for x in coll if x.value > 5),
                    range(5))))
```

And in Python we don't have threading/piping operators or macros.
So we should use something different, and I guess transducers is
what we need. It's not actually transducers, but very similar concept,
let's call it transformers and transformers factories:

```python
transformer(coll) => result
transformer_factory(*args) => transformer(coll) => result
transformer_factory(*args, args) => result
```

In use:

```python
import operator
from mcoll import t

t.into([t.map(lambda x: x.value),
        t.filter(lambda x: x > 5),
        t.reduce(operator.add)], coll)

t.into([t.map(lambda x: x.value),
        t.filter(lambda x: x > 5),
        t.zip(range(5)),
        t.map(sum),
        t.reduce(operator.add)], coll)
```

So `t.map`, `t.filter`, `t.zip`, `t.reduce` and `t.into` is a transformer factories.
`t.into` is a special one, it can apply list of transformers to collection.
