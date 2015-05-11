from collections.abc import Iterable, Sequence
import builtins
import functools
import itertools
from .utils import trans


map = trans(builtins.map)
filter = trans(builtins.filter)
flatten = trans(itertools.chain.from_iterable, True)
reversed = trans(builtins.reversed, True)

dict_keys = trans(lambda x: x.keys(), True)
dict_values = trans(lambda x: x.values(), True)
dict_items = trans(lambda x: x.items(), True)


@trans
def reduce(fn, coll, initial=None):
    if initial is None:
        return functools.reduce(fn, coll)
    else:
        return functools.reduce(fn, coll, initial)


@trans
def zip_with(others, coll, right=False):
    if right:
        return builtins.zip(*list(others) + [coll])
    else:
        return builtins.zip(coll, *others)


@trans
def zip(other, coll, right=False):
    return zip_with([other], coll, right=right)


@trans
def merge_with(other_colls, coll, right=False):
    if right:
        return flatten(list(other_colls) + [coll])
    else:
        return flatten([coll] + list(other_colls))


@trans
def merge(other_coll, coll, right=False):
    return merge_with([other_coll], coll, right=right)


@trans
def slice(start, coll, stop=None, step=None):
    try:
        return itertools.islice(coll, start, stop, step)
    except ValueError:
        return slice(start, list(coll), stop=stop, step=step)


@slice.register(Sequence)
def _slice_sequence(start, coll, stop=None, step=None):
    return coll[start:stop:step]


@trans
def nth(num, coll):
    try:
        return next(itertools.islice(coll, num, num + 1))
    except ValueError:
        return nth(num, list(coll))


@nth.register(Sequence)
def _nth_sequence(num, coll):
    return coll[num]


@trans
def into(dest, coll):
    if isinstance(dest, Iterable):
        for t in dest:
            coll = into(t, coll)
        return coll
    else:
        return dest(coll)
