import sys
sys.path.append("..")
from helper import get_lines, time_func

def setup(lines):
    polymer_string = ""
    rules = {}

    for index in range(len(lines)):
        if index == 0:
            polymer_string = lines[index].strip('\n')
        else:
            if " -> " in lines[index]:
                line_components = lines[index].strip("\n").split(" -> ")
                rules[line_components[0]] = line_components[1]

    return polymer_string, rules

def mutate_polymer(polymer, rules):
    new_polymer = ""

    for index in range(len(polymer)):
        if index > 0:
            check = polymer[index -1] + polymer[index]
            rule = rules.get(check, None)
            if rule:
                new_polymer += rule + polymer[index]
            else:
                new_polymer += polymer[index]
        else:
            new_polymer += polymer[index]

    return new_polymer

def count_chars(string):
    char_dict = {}

    for char in string:
        if char_dict.get(char, None):
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def min_max(values):
    max_char = ""
    max_count = 0
    min_char = ""
    min_count = 0

    for key in values.keys():
        count = values[key]
        if count > max_count:
            max_count = count
            max_char = key
        if min_count == 0:
            min_count = count
            min_char = key
        else:
            if count < min_count:
                min_count = count
                min_char = key
    
    return min_char, max_char

def process():
    lines = get_lines()
    starting_polymer, rules = setup(lines)
    loop_times = 10
    mutated_polymer = starting_polymer

    for _ in range(loop_times):
        mutated_polymer = mutate_polymer(mutated_polymer, rules)

    counted_chars = count_chars(mutated_polymer)
    min_char, max_char = min_max(counted_chars)

    difference = counted_chars[max_char] - counted_chars[min_char]

    print("Answer: ", difference)
    

if __name__ == "__main__":
    time_func(process)