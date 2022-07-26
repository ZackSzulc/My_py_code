from bank import value

def test_Hstart():
    assert value("  HAPPY EVENING") == 20
    assert value("H2O IS Reccomended") == 20
    assert value("h!") == 20
    assert value("      hell o to all") == 20

def test_HELLOstart():
    assert value("  HELLO") == 0
    assert value("Hello, Kind Sir") == 0
    assert value("HEllo!") == 0
    assert value("heLLoTherePerson") == 0

def test_OTHERstart():
    assert value("_hello") == 100
    assert value(" Diff letter") == 100
    assert value("Jim, hello") == 100
    assert value("GOOD EVENING") == 100