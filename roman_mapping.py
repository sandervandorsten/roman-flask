import sys
import logging
import set_logging
from operator import itemgetter

LOGGER = logging.getLogger('roman.mapping')


def num2roman(n: int, roman_val=''):
    """Converts a positive arabic number into a roman numeral. #numberArt

    :param n: a positive integer you're interested in
    :param roman_val: just don't bother
    :return: a string representing the roman numeral of n
    """
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

    LOGGER.debug(f"numeral = {n}, roman = {roman_val}")

    if n == 0:
        return roman_val
    elif n < 0:
        raise ValueError("Romans didn't have negative numbers.")

    for key, value in sorted(mapping.items(), reverse=True):
        if n >= key:
            roman_val = roman_val + value
            n = n - key
            return num2roman(n, roman_val)


def roman2num(s: str, n: int = 0):
    """Translate roman numbers into numeric

    :param s: a string with a roman numeral you want to convert
    :param n: don't bother plz
    :return: the arabic number of your roman numeral
    """
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

    LOGGER.debug(f"roman = {s}, n = {n}")
    if s == "":
        return n
    s = s.upper()

    for key, value in sorted(mapping.items(), key=itemgetter(1), reverse=True):
        if s.startswith(key):
            # check if s is is descending order
            if 0 < n < value:
                raise ValueError("You didn't provide a correct input")
            n += value
            s = s.replace(key, "", 1)
            return roman2num(s, n)
    # if the letter is not in the dictionary raise an error
    raise ValueError("You didn't provide a correct input.")


if __name__ == "__main__":
    LOGGER = set_logging.setup_logger(verbose=True)
    to_be_translated = sys.argv[1]
    try:
        to_be_translated = int(to_be_translated)
        num2roman(to_be_translated)
    except ValueError:
        roman2num(to_be_translated)
