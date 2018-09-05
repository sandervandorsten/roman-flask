

def num2roman(n, roman_val=''):
    mapping = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'}
    print(f" n= {n}, roman = {roman_val}")

    if n == 0:
        return roman_val

    for key, value in sorted(mapping.items(), reverse=True):
        if n >= key:
            roman_val = roman_val + value
            n = n - key
            return num2roman(n, roman_val)


def roman2num(s:str, n:int = 0):
    """ Translate roman numbers into numeric"""
    mapping = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000}

    print(f"roman = {s}, n = {n}")
    if s == "":
        return n

    for key, value in sorted(mapping.items(), key= lambda x: x[1], reverse=True):
        if s.startswith(key):
            n += value
            s = s.replace(key, "", 1)
            return roman2num(s, n)


if __name__ == "__main__":
    print(num2roman(2018))
    print(roman2num("MMXVIII"))