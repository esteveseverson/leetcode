def remove_substring(s: str, part: str) -> str:
    
    lenght = len(s)

    for i in range(lenght):        
        if part in s:
            s = s.replace(part, '', 1)

    return s

s = 'aabababa'
print(remove_substring(s, 'aba'))