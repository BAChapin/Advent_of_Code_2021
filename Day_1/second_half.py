import sys
sys.path.append("..")
from helper import time_func

def generate_sums(lines: list):
    new_list = list(map(int, lines))
    sums = []
    for index in range(1, len(lines) - 1):
        new_sum = new_list[index - 1] + new_list[index] + new_list[index + 1]
        sums.append(new_sum)
    else:
        return sums

def process():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        sums = generate_sums(lines)
        increase_num = 0

        for index in range(1, len(sums)):
            previous_sum = sums[index - 1]
            current_sum = sums[index]

            if current_sum > previous_sum:
                increase_num += 1
        else:
            print("Number of Sum Increases: ", increase_num)

if __name__ == "__main__":
    time_func(process)
