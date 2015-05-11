from mcoll import t


coll = range(10)
r = t.into([t.map(lambda x: x ** 2),
            t.filter(lambda x: x % 2),
            t.slice(2, step=5),
            t.merge(range(10), right=True),
            t.nth(-1)], coll)


print(r)
