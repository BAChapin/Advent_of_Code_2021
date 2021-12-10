import sys
sys.path.append("..")
from helper import get_lines, time_func

def match_for(bracket):
    matches = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>'
    }
    if bracket in matches.keys():
        return matches[bracket]
    else:
        return None

def is_end_delimeter(bracket):
    delimeters = [')', '}', ']', '>']
    return bracket in delimeters

def remove_matches(line):
    line = line
    while (True):
        remove_indices = []
        for index in range(len(line)):
            item = line[index]
            if index < len(line) - 1:
                check = line[index + 1]
                if match_for(item) == check:
                    remove_indices.append(index)
                    remove_indices.append(index + 1)
        else:
            if len(remove_indices) == 0:
                return line
            else:
                new_line = []
                for index in range(len(line)):
                    if index not in remove_indices:
                        new_line.append(line[index])
                line = new_line
                
def find_expected(line):
    for index in range(len(line)):
        if index < len(line) - 1:
            check = line[index + 1]
            if is_end_delimeter(check):
                return check

def process():
    lines = get_lines()
    error_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    error_score = 0
    
    for line in lines:
        line = [char for char in line]

        unique = remove_matches(line)
        expected = find_expected(unique)
        if expected:
            error_score += error_scores[expected]

    print("Answer: ", error_score)

if __name__ == "__main__":
    time_func(process)