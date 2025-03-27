def binary_sum(a, b):
    return '{0:b}'.format(int(a, 2) + int(b, 2))

##2-й вариант
def binary_sum(a, b):
    sum = int(a, 2) + int(b, 2)
    return bin(sum)[2:]
