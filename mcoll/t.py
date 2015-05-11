from collections.abc import Iterable, Sequence
import builtins
import functools
import itertools
from .utils import trans, list_or_seq
from .seq import Seq


map = trans(builtins.map)
filter = trans(builtins.filter)
reduce = trans(functools.reduce)
zip = trans(builtins.zip)
seq = Seq
flatten = itertools.chain.from_iterable

dict_keys = lambda x: x.keys()
dict_values = lambda x: x.values()
dict_items = lambda x: x.items()


@trans
def merge(other_coll, coll, right=False):
    if right:
        return list_or_seq(other_coll) + list_or_seq(coll)
    else:
        return list_or_seq(coll) + list_or_seq(other_coll)


@trans
def slice(start, coll, stop=None, step=None):
    return list_or_seq(coll)[start:stop:step]


@trans
def nth(num, coll):
    return list_or_seq(coll)[num]


@trans
@functools.singledispatch
def into(dest, coll):
    return dest(coll)


@into.register(Iterable)
def _into_list(dest, coll):
    for t in dest:
        coll = into(t, coll)
    return coll
