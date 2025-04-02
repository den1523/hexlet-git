# BEGIN (write your solution here)
triple = ('A', 'B', 'C')


def rotate_left(triple):
    (first, second, third) = triple
    (first, second, third) = (third, first, second)
    triple = (third, first, second)
    return triple


def rotate_right(triple):
    (first, second, third) = triple
    (first, second, third) = (second, third, first)
    triple = (second, third, first)
    return triple
# END
