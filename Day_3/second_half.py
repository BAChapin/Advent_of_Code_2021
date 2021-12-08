import sys
sys.path.append("..")
from helper import time_func

def split_lists(at_index, given_list, return_most):
    input_len = len(given_list)
    most_common = 0
    ones_list = []
    zeros_list = []

    for item in given_list:
        num_value = int(item[at_index])
        most_common += num_value

        if item[at_index] == "0":
            zeros_list.append(item)
        else:
            ones_list.append(item)
    else:
        if most_common >= (input_len / 2) and return_most:
            return ones_list
        elif most_common < (input_len / 2) and return_most:
            return zeros_list
        elif most_common >= (input_len / 2) and not return_most:
            return zeros_list
        elif most_common < (input_len / 2) and not return_most:
            return ones_list

def process():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        oxygen_readings = lines
        co2_readings = lines

        for index in range(0, len(lines[0]) - 1):
            if len(oxygen_readings) > 1:
                oxygen_readings = split_lists(index, oxygen_readings, True)

            if len(co2_readings) > 1:
                co2_readings = split_lists(index, co2_readings, False)
        else:
            oxygen = int(oxygen_readings[0], 2)
            co2 = int(co2_readings[0], 2)
            print("Life Support Rating: ", oxygen * co2)

if __name__ == "__main__":
    time_func(process)
