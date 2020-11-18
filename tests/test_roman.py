from romanflask.roman_mapping import num2roman, roman2num


def test_num2roman():
    assert num2roman(9) == "IX"
    assert num2roman(490) == "CDXC"
    assert num2roman(80) == "LXXX"
    assert num2roman(1873) == "MDCCCLXXIII"


def test_roman2num():
    assert roman2num("MMMDCCCLVI") == 3856
    assert roman2num("LIX") == 59
    assert roman2num("CMXVI") == 916
