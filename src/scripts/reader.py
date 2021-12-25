PATH = './inputs/'

def read(filename: str):
    return open(PATH + filename, 'r').readlines()

def strip_lines(filename: str) -> list:
    return [s.strip() for s in read(filename)]

def split_lines(filename: str):
    return [line.split() for line in strip_lines(filename)]

def split_str_int_pairs(filename: str, split_at: str):
    return [[_, int(n)] for _, n in split_lines(filename, split_at)]

def int_lines(filename: str) -> list:
    return [int(s) for s in strip_lines(filename)]