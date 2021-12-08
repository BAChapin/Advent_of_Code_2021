import sys
sys.path.append("..")
from helper import get_lines, time_func

#   1:      4:      7:      8:
#  ....    ....    aaaa    aaaa
# .    c  b    c  .    c  b    c
# .    c  b    c  .    c  b    c
#  ....    dddd    ....    dddd
# .    f  .    f  .    f  e    f
# .    f  .    f  .    f  e    f
#  ....    ....    ....    gggg

def getKeysAndDigits(line):
    split_line = line.split("|")
    keys = split_line[0].strip().split(" ")
    digits = split_line[1].strip().split(" ")
    return keys, digits

def process():
    lines = get_lines()
    values = [getKeysAndDigits(line) for line in lines]

    UNIQUE_LENGTH = [2, 4, 3, 7]
    unique_values = 0

    for keys, digits in values:
        for digit in digits:
            length = len(digit)
            if length in UNIQUE_LENGTH:
                unique_values += 1
    else:
        print("Answer: ", unique_values)

if __name__ == "__main__":
    time_func(process)