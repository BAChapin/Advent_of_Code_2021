import sys
sys.path.append("..")
from helper import get_lines, time_func

def process():
    lines = get_lines()
    increase_num = 0

    for index in range(1, len(lines)):
        previous_depth = int(lines[index -1])
        current_depth = int(lines[index])

        if current_depth > previous_depth:
            increase_num += 1
    else:
        print("Number of Increases: ", increase_num)

if __name__ == "__main__":
    time_func(process)
