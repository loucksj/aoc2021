from src.scripts import day01, day02, day03, day04, day05

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

def test_day04():
    assert day04.part_1('day04_ex.txt') == 4512
    assert day04.part_1('day04.txt') == 87456

    assert day04.part_2('day04_ex.txt') == 1924
    assert day04.part_2('day04.txt') == 15561

def test_day05():
    assert day05.part_1('day05_ex.txt') == 5
    assert day05.part_1('day05.txt') == 5608
    assert day05.part_2('day05_ex.txt') == 12
    assert day05.part_2('day05.txt') == 20299