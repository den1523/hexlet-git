# BEGIN (write your solution here)
def fib(num):
    f1 = 1
    f2 = 1
    i = 0
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        while i < num - 2:
            sum_fib = f1 + f2
            f1 = f2
            f2 = sum_fib
            i += 1
        return f2
# END
