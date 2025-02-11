def clearDigits(s: str) -> str:
    
    lenght = len(s)
    result = ''

    for i in range(lenght):

        if s[i].isalpha():
            result += s[i]

        if s[i].isdigit():
            result = result[::-1].replace(result[-1], '', 1)[::-1]

    return result

string = 'gbysb5'
print(clearDigits(string))