from src.scripts import day01, day02, day03

def test_day01():
    assert day01.part_one('day01_ex.txt') == 7
    assert day01.part_one('day01.txt') == 1215
    assert day01.part_two('day01_ex.txt') == 5
    assert day01.part_two('day01.txt') == 1150

def test_day02():
    assert day02.part_one('day02_ex.txt') == 150
    assert day02.part_one('day02.txt') == 1480518
    assert day02.part_two('day02_ex.txt') == 900
    assert day02.part_two('day02.txt') == 1282809906

def test_day03():
    assert day03.part_one('day03_ex.txt') == 198
    assert day03.part_one('day03.txt') == 3242606
    assert day03.part_two('day03_ex.txt') == 230
    assert day03.part_two('day03.txt') == 4856080