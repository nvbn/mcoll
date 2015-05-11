from functools import partial, wraps
from .seq import Seq


def trans(fn):
    @wraps(fn)
    def wrapper(arg, coll=None, **kwargs):
        if coll is None:
            return partial(fn, arg, **kwargs)
        else:
            return fn(arg, coll, **kwargs)
    return wrapper


def list_or_seq(coll):
    if not isinstance(coll, list):
        return Seq(coll)
    else:
        return coll
