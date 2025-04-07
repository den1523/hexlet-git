# BEGIN (write your solution here)
def is_power_of_three(natural):
    i = 1
    while i <= natural:
        char = 3 ** i
        if natural == 1:
            return True
        if char == natural and natural % 3 == 0:
            return True
        i += 1
    return False
# END

#2-й вариант

def is_power_of_three(num):
    i = 0
    if i == 1:
        return True
    while i < num:
        if pow(3, i) == num:
            return True
        i += 1
    return False
