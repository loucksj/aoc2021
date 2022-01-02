import _key  # solutions hidden

from scripts import (day01, day02, day03, day04, day05, day06, day07, day08, day09, day10,
                     day11, day12, day13, day14, day15, day16)


def test_day01():
    assert day01.part_one('day01_ex.txt') == 7
    assert day01.part_one('day01.txt') == _key.DAY01_1
    assert day01.part_two('day01_ex.txt') == 5
    assert day01.part_two('day01.txt') == _key.DAY01_2


def test_day02():
    assert day02.part_one('day02_ex.txt') == 150
    assert day02.part_one('day02.txt') == _key.DAY02_1
    assert day02.part_two('day02_ex.txt') == 900
    assert day02.part_two('day02.txt') == _key.DAY02_2


def test_day03():
    assert day03.part_one('day03_ex.txt') == 198
    assert day03.part_one('day03.txt') == _key.DAY03_1
    assert day03.part_two('day03_ex.txt') == 230
    assert day03.part_two('day03.txt') == _key.DAY03_2


def test_day04():
    assert day04.part_one('day04_ex.txt') == 4512
    assert day04.part_one('day04.txt') == _key.DAY04_1
    assert day04.part_two('day04_ex.txt') == 1924
    assert day04.part_two('day04.txt') == _key.DAY04_2


def test_day05():
    assert day05.part_one('day05_ex.txt') == 5
    assert day05.part_one('day05.txt') == _key.DAY05_1
    assert day05.part_two('day05_ex.txt') == 12
    assert day05.part_two('day05.txt') == _key.DAY05_2


def test_day06():
    assert day06.part_one('day06_ex.txt') == 5934
    assert day06.part_one('day06.txt') == _key.DAY06_1
    assert day06.part_two('day06_ex.txt') == 26984457539
    assert day06.part_two('day06.txt') == _key.DAY06_2


def test_day07():
    assert day07.part_one('day07_ex.txt') == 37
    assert day07.part_one('day07.txt') == _key.DAY07_1
    assert day07.part_two('day07_ex.txt') == 168
    assert day07.part_two('day07.txt') == _key.DAY07_2


def test_day08():
    assert day08.part_one('day08_ex.txt') == 26
    assert day08.part_one('day08.txt') == _key.DAY08_1
    assert day08.part_two('day08_ex_short.txt') == 5353
    assert day08.part_two('day08_ex.txt') == 61229
    assert day08.part_two('day08.txt') == _key.DAY08_2


def test_day09():
    assert day09.part_one('day09_ex.txt') == 15
    assert day09.part_one('day09.txt') == _key.DAY09_1
    assert day09.part_two('day09_ex.txt') == 1134
    assert day09.part_two('day09.txt') == _key.DAY09_2


def test_day10():
    assert day10.part_one('day10_ex.txt') == 26397
    assert day10.part_one('day10.txt') == _key.DAY10_1
    assert day10.part_two('day10_ex.txt') == 288957
    assert day10.part_two('day10.txt') == _key.DAY10_2


def test_day11():
    assert day11.part_one('day11_ex.txt') == 1656
    assert day11.part_one('day11.txt') == _key.DAY11_1
    assert day11.part_two('day11_ex.txt') == 195
    assert day11.part_two('day11.txt') == _key.DAY11_2


def test_day12():
    assert day12.part_one('day12_ex_short.txt') == 10
    assert day12.part_one('day12_ex.txt') == 19
    assert day12.part_one('day12_ex_long.txt') == 226
    assert day12.part_one('day12.txt') == _key.DAY12_1
    assert day12.part_two('day12_ex_short.txt') == 36
    assert day12.part_two('day12_ex.txt') == 103
    assert day12.part_two('day12_ex_long.txt') == 3509
    assert day12.part_two('day12.txt') == _key.DAY12_2


def test_day13():
    assert day13.part_one('day13_ex.txt') == 17
    assert day13.part_one('day13.txt') == _key.DAY13_1
    assert day13.part_two('day13.txt') == _key.DAY13_2


def test_day14():
    assert day14.part_one('day14_ex.txt') == 1588
    assert day14.part_one('day14.txt') == _key.DAY14_1
    assert day14.part_two('day14_ex.txt') == 2188189693529
    assert day14.part_two('day14.txt') == _key.DAY14_2


def test_day15():
    assert day15.part_one('day15_ex.txt') == 40
    assert day15.part_one('day15.txt') == _key.DAY15_1
    assert day15.part_two('day15_ex.txt') == 315
    #assert day15.part_two('day15.txt') == _key.DAY15_2 # correct, but slow


def test_day16():
    pass
    #assert day16.part_one('day16_ex_literal.txt') == 6
    #assert day16.part_one('day16_ex_operator.txt') == 1
    #assert day16.part_one('day16_ex1.txt') == 16
    #assert day16.part_one('day16_ex2.txt') == 12
    #assert day16.part_one('day16_ex3.txt') == 23
    #assert day16.part_one('day16_ex4.txt') == 31
    #assert day16.part_1('day16.txt') == 0
    #assert day16.part_2('day16_ex.txt') == 0
    #assert day16.part_2('day16.txt') == 0
