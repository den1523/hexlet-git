def encrypt(text):
    result = ''
    i = 1
    while i < len(text):
        result = result + text[i] + text[i - 1]
        i += 2
    if len(text) % 2 != 0:
        return result + text[-1]
    return result

#2-й вариант
def encrypt(text):
    result = ''
    char = ''
    i = 2
    while i <= len(text):
        char = text[i-2:i]
        result += char[::-1]
        i += 2
    if len(text) % 2 != 0:
            result += text[-1]
    return result
