def invert_case(string):
    result = ''
    i = 0
    while i <= len(string) - 1:
        if string[i] != string[i].upper():
            result += string[i].upper()
        elif string[i] != string[i].lower():
            result += string[i].lower()
        elif string[i] == ' ' or string[i] == '!' or string[i] == ',':
            result += string[i]
        i = i + 1
    return result

#2 вариант
def invert_case(text):
    result = ''
    for char in text:
        if char == char.lower():
            result += char.upper()
        elif char == char.upper():
            result += char.lower()
    return result[::-1]
