# This is a warm up exercise on generators


def gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n



a =gen()

next(a)
next(a)
next(a)
next(a)