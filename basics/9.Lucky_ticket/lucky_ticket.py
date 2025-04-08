def is_happy_ticket(ticket):
    i = 0
    count_left = 0
    count_right = 0
    half = int(len(ticket) / 2)
    while i < half and half < len(ticket):
        count_left += int(ticket[i])
        count_right += int(ticket[half])
        half += 1
        i += 1
    return count_left == count_right

#2-й вариант

def is_happy_ticket(ticket):
    if len(ticket) % 2 != 0:
        return False
    i = 0
    sum_left = 0
    sum_rigth = 0
    middle = int(len(ticket) / 2)
    while i < len(ticket):
        if i >= middle:
            sum_rigth += int(ticket[i])
        elif i < middle:
            sum_left += int(ticket[i])
        i += 1
    return sum_left == sum_rigth
