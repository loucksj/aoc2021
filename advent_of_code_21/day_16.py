def part_1(file: str) -> int:
    lines = open(file, 'r').readlines()
    line = lines[0].strip()

    binary = bin(int(line, 16))
    binary = binary[2:]
    
    versions = 0
    type_id = -1
    length_id = -1
    length = -1
    p = -1
    for i, bit in enumerate(binary):
        p += 1
        if p == 0:
            version = int(binary[i:i+3], 2)
            versions += version
        elif p == 3:
            type_id = int(binary[i:i+3])
        
        if type_id == 4: #literal
            if p == 6:
                a = int(binary[i:i+5], 2)
            elif p == 11:
                a = int(binary[i:i+5], 2)
            elif p == 16:
                a = int(binary[i:i+5], 2)
            elif p == 23:
                p = 0
        else: # operator
            if p == 6:
                length_id = binary[i]
            elif p == 7:
                if length_id == 0:
                    length = int(binary[i:i+15], 2)
                else:
                    length = int(binary[i:i+11], 2)

    return 0

if __name__ == '__main__':
    assert part_1('day_16_literal.txt') == 16
    #assert part_1('day_16_operator1.txt') == 12
    #assert part_1('day_16_operator2.txt') == 23
    #assert part_1('day_16.txt') == 31

    #assert part_2('day_16_test.txt') == 0
    #assert part_2('day_16.txt') == 0