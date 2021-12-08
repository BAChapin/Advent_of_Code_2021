import sys
sys.path.append("..")
from helper import time_func

def process():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        horizontal_position = 0
        depth = 0
        aim = 0

        for line in lines:
            split_line = line.split(" ")
            direction = split_line[0]
            units = int(split_line[1])

            if direction.lower() == "forward":
                horizontal_position += units
                depth += (aim * units)
            elif direction.lower() == "up":
                aim -= units
            elif direction.lower() == "down":
                aim += units
        else:
            print("Puzzle Answer: ", horizontal_position * depth)

if __name__ == "__main__":
    time_func(process)