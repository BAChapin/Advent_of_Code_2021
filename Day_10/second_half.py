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

def contains_end_delimeter(line):
    delimeters = [')', '}', ']', '>']
    for delimeter in delimeters:
        if delimeter in line:
            return True
    return False

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
                if not contains_end_delimeter(line):
                    return line
                else:
                    return None
            else:
                new_line = []
                for index in range(len(line)):
                    if index not in remove_indices:
                        new_line.append(line[index])
                line = new_line

def process():
    lines = get_lines()
    error_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    line_scores = []
    
    for line in lines:
        line = [char for char in line]

        unique = remove_matches(line)
        if unique:
            line_score = 0
            unique.reverse()
            for char in unique:
                if char != "\n":
                    matching_delimeter = match_for(char)
                    line_score *= 5
                    line_score += error_scores[matching_delimeter]
            line_scores.append(line_score)

    line_scores.sort()
    middle_index = int(len(line_scores) / 2)

    print("Answer: ", line_scores[middle_index])

if __name__ == "__main__":
    time_func(process)