def fizz_buzz(begin, end):
    result = ''
    if begin > end:
        return result
    if begin == end:
        return f'{end}'
    while begin <= end:
        if begin % 3 == 0 and begin % 5 != 0:
            result = result + 'Fizz' + ' '
        elif begin % 15 == 0:
            result = result + 'FizzBuzz' + ' '
        elif begin % 5 == 0:
            result = result + 'Buzz' + ' '
        else:
            result = result + str(begin) + ' '
        begin += 1
    return result.strip()
    