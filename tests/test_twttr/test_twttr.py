from twttr import shorten

def test_shorten_upper():
    assert shorten("COUP12") == "CP12"
    assert shorten("AEIOU") == ""
    assert shorten("ADD A SPACE_!") == "DD  SPC_!"
    assert shorten("TWTTR") == "TWTTR"


def test_shorten_lower():
    assert shorten("coup12") == "cp12"
    assert shorten("aeiou") == ""
    assert shorten("add a space_!") == "dd  spc_!"
    assert shorten("twttr") == "twttr"