from src.scripts.day01 import part01, part02

def test_part01():
    assert part01('day01_example.txt') == 7
    assert part01('day01_input.txt'), 1215

def test_part02():
    assert part02('day01_example.txt') == 5
    assert part02('day01_input.txt') == 1150