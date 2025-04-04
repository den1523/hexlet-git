# BEGIN (write your solution here)
def diff(first, second):
    res1 = abs(first - second)
    res2 = (2 * 180 - res1) % 360
    return min(res2, res1)
# END

#2-й вариант
def diff(a, b):
    res1 = abs(b - a)
    res2 = 360 - res1
    return min(res1, res2)
