from plates import is_valid

def test_punc():
    assert is_valid("as1!2") == False
    assert is_valid("as12`") == False
    assert is_valid('"as12"') == False
    assert is_valid("as 12") == False

def test_nums():
    assert is_valid("as12a") == False
    assert is_valid("ab123") == True
    assert is_valid("cs05") == False
    assert is_valid("cs50P") == False

def test_start_letters():
    assert is_valid("1256") == False
    assert is_valid("50cs") == False
    assert is_valid("_cs50") == False
    assert is_valid("AB") == True

def test_len():
    assert is_valid("h") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("ABCDEF") == True