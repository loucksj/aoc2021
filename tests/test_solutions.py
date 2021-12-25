from src.scripts import day01, day02

def test_day01():
    assert day01.part01('day01_example.txt') == 7
    assert day01.part01('day01_input.txt') == 1215
    assert day01.part02('day01_example.txt') == 5
    assert day01.part02('day01_input.txt') == 1150

def test_day02():
    assert day02.part_1('day02_example.txt') == 150
    assert day02.part_1('day02_input.txt') == 1480518
    assert day02.part_2('day02_example.txt') == 900
    assert day02.part_2('day02_input.txt') == 1282809906