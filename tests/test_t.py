import operator
from mcoll import t


def _list_equal(*args):
    lists = [list(x) for x in args]
    for x in lists:
        if x != lists[0]:
            return False
    return True


def _set_equal(*args):
    sets = [set(x) for x in args]
    for x in sets:
        if x != sets[0]:
            return False
    return True


def test_map():
    assert _list_equal(t.map(lambda x: x ** 2, range(3)),
                       t.map(lambda x: x ** 2)(range(3)),
                       [0, 1, 4])


def test_filter():
    assert _list_equal(t.filter(lambda x: x > 2, range(5)),
                       t.filter(lambda x: x > 2)(range(5)),
                       [3, 4])


def test_reduce():
    assert t.reduce(operator.add, range(5)) == \
           t.reduce(operator.add)(range(5)) == 10
    assert t.reduce(operator.add, range(5), initial=2) == \
           t.reduce(operator.add, initial=2)(range(5)) == 12


def test_zip():
    assert _list_equal(t.zip(range(5), range(5, 10), right=True),
                       t.zip(range(5), right=True)(range(5, 10)),
                       [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)])
    assert _list_equal(t.zip(range(5), range(5, 10)),
                       t.zip(range(5))(range(5, 10)),
                       [(5, 0), (6, 1), (7, 2), (8, 3), (9, 4)])


def test_flatten():
    assert _list_equal(t.flatten([[1, 2], [3, 4]]),
                       [1, 2, 3, 4])


def test_reversed():
    assert _list_equal(t.reversed(range(5)),
                       range(5)[::-1])


def test_dict_keys():
    assert _set_equal(t.dict_keys({'a': 1, 'b': 2}),
                      ['a', 'b'])


def test_dict_values():
    assert _set_equal(t.dict_values({'a': 1, 'b': 2}),
                      [1, 2])


def test_dict_items():
    assert _set_equal(t.dict_items({'a': 1, 'b': 2}),
                      [('a', 1), ('b', 2)])


def test_merge():
    assert _list_equal(t.merge(range(2), range(3), right=True),
                       t.merge(range(2), right=True)(range(3)),
                       [0, 1, 0, 1, 2])
    assert _list_equal(t.merge(range(2), range(3)),
                       t.merge(range(2))(range(3)),
                       [0, 1, 2, 0, 1])


def test_slice():
    assert _list_equal(t.slice(2, range(10), stop=9, step=3),
                       t.slice(2, stop=9, step=3)(range(10)),
                       range(10)[2:9:3],
                       t.slice(2, iter(range(10)), stop=9, step=3),
                       t.slice(2, stop=9, step=3)(iter(range(10))))
    assert _list_equal(t.slice(-2, range(10), stop=-9, step=-3),
                       t.slice(-2, stop=-9, step=-3)(range(10)),
                       range(10)[-2:-9:-3],
                       t.slice(-2, iter(range(10)), stop=-9, step=-3),
                       t.slice(-2, stop=-9, step=-3)(iter(range(10))))


def test_nth():
    assert t.nth(5, range(10)) == t.nth(5)(range(10)) == range(10)[5] == \
           t.nth(5, iter(range(10))) == t.nth(5)(iter(range(10)))
    assert t.nth(-5, range(10)) == t.nth(-5)(range(10)) == range(10)[-5] == \
           t.nth(-5, iter(range(10))) == t.nth(-5)(iter(range(10)))


def test_into():
    assert t.into(dict, (('a', 1), ('b', 2))) == \
           t.into(dict)((('a', 1), ('b', 2))) == {'a': 1, 'b': 2}
    assert t.into([dict], (('a', 1), ('b', 2))) == \
           t.into([dict])((('a', 1), ('b', 2))) == {'a': 1, 'b': 2}
