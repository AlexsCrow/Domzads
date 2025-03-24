s = 0


def outer(a, b, c)
    def inner(i, j)
        repr(i * j)

    global s
    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))


outer(2, 4, 6)
print(s)
outer(5, 8, 2)
outer()