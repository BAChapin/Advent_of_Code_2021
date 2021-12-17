from collections import Counter
from more_itertools import windowed
import sys
from time import time
sys.path.append("..")
from helper import time_func

def setup(file):
    template, insertions = file.read().split("\n\n")
    template = list(template)
    insertions = insertions.strip().split("\n")
    rules = {}
    for insertion in insertions:
        pair, split_insertion = insertion.rstrip().split(" -> ")
        rules[pair] = split_insertion

    return template, rules

def insert_elements_smart(pair_count, element_count, rules):
    new_pair_count = pair_count.copy()
    for key in pair_count:
        pair = list(key)
        insert_element = rules[key]
        element_count[insert_element] += pair_count[key]
        new_pair_count[''.join([pair[0], insert_element])] += pair_count[key]
        new_pair_count[''.join([insert_element, pair[1]])] += pair_count[key]
        new_pair_count[key] -= pair_count[key]
    return new_pair_count, element_count

def process_polymer(polymer, rules, steps):
    element_count = Counter(polymer)
    pair_count = Counter(dict.fromkeys(rules.keys(), 0))
    for pair in windowed(polymer, 2):
        pair_count[''.join(pair)] += 1
    for i in range(steps):
        pair_count, element_count = insert_elements_smart(pair_count, element_count, rules)
    return max(element_count.values()) - min(element_count.values())
    
def process():
    file = open("input.txt", "r")
    starting_polymer, rules = setup(file)
    file.close()
    answer = process_polymer(starting_polymer, rules, 40)
    print("Answer: ", answer)



if __name__ == "__main__":
    time_func(process)