def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


# BEGIN (write your solution here)
def is_happy_number(number):
    count = 0
    while number != 1 and count < 10:
        number = sum_of_square_digits(number)
        count += 1
    return number == 1
# END
