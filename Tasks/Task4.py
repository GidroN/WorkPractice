roman_numerals = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
special_numerals = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


def convert_roman_to_human(string: str) -> int:
    for i in special_numerals.keys():
        if i in string:
            string = string.replace(i, f"+{special_numerals[i]}+")
    for i in string:
        if not i.isdigit() and i != '+':
            string = string.replace(i, f"+{roman_numerals[i]}+")
    
    lst = string[1:-1].replace("++", "+").split("+")
    return sum(map(int, lst))

print(convert_roman_to_human("XLIX"))
            
        


