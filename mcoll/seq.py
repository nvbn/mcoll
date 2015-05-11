from itertools import islice, chain


class Seq(object):
    def __init__(self, col):
        self._col = iter(col)
        self._realised = []
        self._iterated = False

    def __iter__(self):
        for item in self._realised:
            yield item
        for item in self._col:
            self._realised.append(item)
            yield item

    def __len__(self):
        return len(list(self.__iter__()))

    def __getitem__(self, item):
        if isinstance(item, slice):
            if item.step > 0 or item.step is None:
                return Seq(islice(self, item.start, item.stop, item.step))
            else:
                return Seq(list(self)[item])
        elif item < 0:
            return list(self)[item]
        elif item < len(self._realised):
            return self._realised[item]
        else:
            for i, x in enumerate(self):
                if i == item:
                    return x
            raise IndexError('list index out of range')

    def __add__(self, other):
        return Seq(chain.from_iterable([self, other]))

    def __radd__(self, other):
        return Seq(chain.from_iterable([other, self]))

    def __eq__(self, other):
        return list(self) == list(other)

    def _(self, fn):
        return fn(self)

    def __str__(self):
        return 'seq{}'.format(list(self))

    def __repr__(self):
        return 'seq{}'.format(list(self))
