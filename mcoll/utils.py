from functools import partial, wraps


class Transformer(object):
    def __init__(self, fn):
        self._dispatches = []
        self.register(object)(fn)

    def register(self, cls):
        def decorator(fn):
            self._dispatches.append((cls, fn))
            return fn
        return decorator

    def _get_matched(self, coll):
        for cls, fn in self._dispatches[::-1]:
            if isinstance(coll, cls):
                return fn

    def __call__(self, arg, coll=None, **kwargs):
        if coll is None:
            return partial(self, arg, **kwargs)
        else:
            return self._get_matched(coll)(arg, coll, **kwargs)


class NoArgTransformer(Transformer):
    def __call__(self, coll):
        return self._get_matched(coll)(coll)


def trans(fn=None, no_arg=False):
    if fn is None:
        return partial(trans, no_arg=no_arg)
    else:
        cls = NoArgTransformer if no_arg else Transformer
        return wraps(fn)(cls(fn))
