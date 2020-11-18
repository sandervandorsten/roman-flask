import sys

from romanflask import set_logging
from romanflask.roman_mapping import num2roman, roman2num


def main():
    LOGGER = set_logging.setup_logger(verbose=True)
    to_be_translated = sys.argv[1]
    try:
        to_be_translated = int(to_be_translated)
        return num2roman(to_be_translated)
    except ValueError:
        return roman2num(to_be_translated)


if __name__ == "__main__":
    print(main())
