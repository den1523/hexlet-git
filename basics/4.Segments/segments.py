# BEGIN (write your solution here)


def is_degenerated(line):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    if x1 == x2 and y1 == y2:
        return True
    return False


def is_vertical(line):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    return x1 == x2 and y1 != y2


def is_horizontal(line):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    return x1 != x2 and y1 == y2


def is_inclined(line):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    return x1 != x2 and y1 != y2
# END
