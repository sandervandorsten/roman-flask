from roman_mapping import translate


def test_translate():
    assert translate(9) == 'IX'
    assert translate(490) == 'CDXC'
    assert translate(80) == "LXXX"
    assert translate(1873) == 'MDCCCLXXIII'