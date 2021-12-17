# A big thank you and credit to be given to plan-x64 on Github. I used much of
# their solution to work this out. I was very stumped, so thank you!
# https://github.com/plan-x64/advent-of-code-2021/blob/main/advent/day12.py

from collections import defaultdict, deque
import sys
sys.path.append("..")
from helper import get_lines, time_func

def generate_map(lines):
    graph = defaultdict(set)
    for connection in lines:
        v1, v2 = tuple(connection.strip().split("-"))
        graph[v1].add(v2)
        graph[v2].add(v1)
    return graph

def part1_filter(possible_vertex, current_path):
    return possible_vertex.isupper() or possible_vertex not in current_path

def find_all_paths(graph, path_filter):
    paths = deque([['start']])

    valid_paths = []
    while paths:
        current_path = paths.pop()
        current_vertex = current_path[-1]
        print(current_vertex)

        if current_vertex == 'end':
            valid_paths.append(current_path)
            print("end")
            continue
            
        for connected_vertex in graph[current_vertex]:
            if path_filter(connected_vertex, current_path):
                paths.append(current_path + [connected_vertex])
    
    return valid_paths

def process():
    lines = get_lines()
    graph = generate_map(lines)
    paths = find_all_paths(graph, part1_filter)

    print("Answer: ", len(paths))

if __name__ == "__main__":
    time_func(process)