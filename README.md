# Modern API for Python collections [![Build Status](https://travis-ci.org/nvbn/mcoll.svg)](https://travis-ci.org/nvbn/mcoll)

## Rationale

In Python we have such a good functions like `map`, `reduce`, `filter` and
others for manipulations with collections, but using more then two-three
of them is an unreadable mess:

```python
reduce(operator.add,
       filter(lambda x: x > 5,
              map(lambda x: x.value, coll)))
```

And for comprehensions/generator expressions makes it a slightly better:

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
transformer_factory(*args, coll) => result
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

I guess it's more readable than functions and more extensible than fluent interface.

## Installation

```bash
pip install mcoll
```

## Usage

Available transformers and transformer factories:

`dict_values`, `flatten`, `merge`, `dict_items`, `map`, `nth`, `dict_keys`, `merge_with`, `reversed`, `zip_with`, `filter`, `into`, `slice`, `zip`, `reduce`, `sorted`.

Use transformer factory:

```python
from mcoll import t

transformer = t.map(lambda x: x ** 2)
transformer(range(5))  # => [0, 1, 4, 9, 16] 
```

Use transformer:

```python
t.map(lambda x: x ** 2, range(5))  # => [0, 1, 4, 9, 16]
t.flatten([[1, 2], [3, 4]])  # => [1, 2, 3, 4]
```

Creation transformer from list of transformers:

```python
transformer = t.into([t.map(lambda x: x ** 2),
                         t.filter(lambda x: x % 2),
                         t.reversed])
transformer(range(5))  # => [9, 1]
```

Just apply list of transformers:

```python
t.into([t.dict_items,
        t.flatten,
        t.map(lambda x: x + 5),
        t.filter(lambda x: x % 2),
        t.reduce(lambda memo, x: memo + x)],
        {9: 10, 11: 12, 13: 14})  # => 51
```

transformer is just a function, so you easily can create your own:

```python
to_lower = lambda coll: [x.lower() for x in coll]
t.into([t.dict_items,
        t.flatten,
        to_lower], {'A': 'B', 'C': 'D'})  # => ['c', 'd', 'a', 'b']
```

transformer factory is a bit complex concept, but you can create it easyly with
`trans` decorator:

```python
from mcoll.utils import trans

@trans
def inc_by(num, coll):
    return [x + num for x in coll]
    
inc_by(10, [1, 2])  # => [11, 12]
inc_by(5)([1, 2])  # => [6, 7]
t.into([t.flatten,
        inc_by(3)], [[1, 2], [3, 4]])  # => [4, 5, 6, 7]
```

## Licensed under MIT
