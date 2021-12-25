PATH = './input/'

def read_lines(filename: str):
    return open(PATH + filename, 'r').readlines()

def strip_lines(filename: str) -> list:
    return [s.strip() for s in read_lines(filename)]

def split_lines(filename: str, at=' '):
    return [line.split(at) for line in strip_lines(filename)]

def split_str_int_pairs(filename: str):
    return [[_, int(n)] for _, n in split_lines(filename)]

def int_lines(filename: str) -> list:
    return [int(s) for s in strip_lines(filename)]