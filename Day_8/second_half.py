import sys
sys.path.append("..")
from helper import get_lines, time_func

def getKeysAndDigits(line):
    split_line = line.split("|")
    keys = split_line[0].strip().split(" ")
    digits = split_line[1].strip().split(" ")
    return keys, digits

def uniqueValues(check, input_b):
    unique = ""

    if check and input_b:
        for a in check:
            if a not in input_b:
                unique += a
        
    return unique
    
def containsAllValues(check, value):
    for x in check:
        if x not in value:
            return False
    else:
        return True

class SevenSegmentDisplay(object):
    ONE_COUNT = 2
    FOUR_COUNT = 4
    SEVEN_COUNT = 3
    EIGHT_COUNT = 7

    digits = []
    keys = []

    zero_key = None
    one_key = ""
    two_key = None
    three_key = None
    four_key = ""
    five_key = None
    six_key = None
    seven_key = ""
    eight_key = ""
    nine_key = None

    def __init__(self, keys, digits):
        self.digits = digits

        for key in keys:
            length = len(key)
            if length == self.ONE_COUNT:
                self.one_key = sorted(key)
            elif length == self.FOUR_COUNT:
                self.four_key = sorted(key)
            elif length == self.SEVEN_COUNT:
                self.seven_key = sorted(key)
            elif length == self.EIGHT_COUNT:
                self.eight_key = sorted(key)
            else:
                self.keys.append(key)
        else:
            self.__processRemainingKeys()

    def numberFromInput(self):
        value = ""

        for digit in self.digits:
            digit = sorted(digit)
            if digit == self.one_key:
                value += "1"
            elif digit == self.two_key:
                value += "2"
            elif digit == self.three_key:
                value += "3"
            elif digit == self.four_key:
                value += "4"
            elif digit == self.five_key:
                value += "5"
            elif digit == self.six_key:
                value += "6"
            elif digit == self.seven_key:
                value += "7"
            elif digit == self.eight_key:
                value += "8"
            elif digit == self.nine_key:
                value += "9"
            elif digit == self.zero_key:
                value += "0"

        return int(value)

    def __processRemainingKeys(self):
        still_processing = True
        loop_count = 0
        # 1, 4, 7, 8
        while (still_processing):
            loop_count += 1
            if not self.nine_key:
                for key in self.keys:
                    if len(key) == 6 and containsAllValues(self.four_key, key):
                        self.nine_key = sorted(key)
                        self.keys.remove(key)
                        break
            elif not self.three_key:
                for key in self.keys:
                    if len(key) == 5 and containsAllValues(self.seven_key, key):
                        self.three_key = sorted(key)
                        self.keys.remove(key)
                        break
            elif not self.five_key:
                for key in self.keys:
                    if len(key) == 5 and uniqueValues(self.nine_key, key) in self.one_key:
                        self.five_key = sorted(key)
                        self.keys.remove(key)
                        break
            elif not self.six_key:
                for key in self.keys:
                    if len(key) == 6 and uniqueValues(self.nine_key, key) in self.one_key:
                        self.six_key = sorted(key)
                        self.keys.remove(key)
                        break
            elif not self.two_key:
                for key in self.keys:
                    if len(key) == 5 and uniqueValues(key, self.six_key) in self.one_key:
                        self.two_key = sorted(key)
                        self.keys.remove(key)
                        break
            else:
                if len(self.keys) == 1:
                    self.zero_key = sorted(self.keys[0])
                    self.keys.remove(self.keys[0])
                    still_processing = False

def process():
    lines = get_lines()
    values = [getKeysAndDigits(line) for line in lines]
    segments = [SevenSegmentDisplay(keys, digits) for keys, digits in values]

    running_total = 0

    for segment in segments:
        running_total += segment.numberFromInput()
    
    print("Answer: ", running_total)

if __name__ == "__main__":
    time_func(process)