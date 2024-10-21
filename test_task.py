import pytest
from task import staircase

def test_1():
    assert staircase(3) == "__#\n_##\n###"

def test_2():
    assert staircase(7) == "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"

def test_3():
    assert staircase(2) == "_#\n##"

def test_4():
    assert staircase(1) == "#"

def test_5():
    assert staircase(-8) == "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"

def test_6():
    assert staircase(-1) == "#"

def test_7():
    assert staircase(-2) == "##\n_#"