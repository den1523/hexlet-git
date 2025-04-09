def is_perfect(number):
    i = 2
    count = 0
    result = 0
    if number <= 0:
        return False
    while i <= number:
        if number % i == 0:
            result = number // i
            count += result
        i += 1
    return count == number

#2-й вариант

def is_perfect(number):
    amout = 0
    if number <= 0:
        return False
    for i in range(1, number):
        if number % i == 0:
            amout += i
    return amout == number
