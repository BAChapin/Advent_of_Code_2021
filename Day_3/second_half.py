
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
        if most_common >= (input_len / 2):
            if return_most:
                return ones_list
            else:
                return zeros_list
        else:
            if return_most:
                return zeros_list
            else:
                return ones_list


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
        running_oxygen = lines
        running_co2 = lines
        oxygen_rating = ""
        co2_rating = ""

        for index in range(0, len(lines[0]) - 1):
            if len(running_co2) == 1:
                co2_rating = running_co2[0]
            else:
                running_co2 = split_lists(index, running_co2, False)

            if len(running_oxygen) == 1:
                oxygen_rating = running_oxygen[0]
            else:
                running_oxygen = split_lists(index, running_oxygen, True)
        else:
            print("Raw Oxegen: ", oxygen_rating)
            print("Raw CO2: ", co2_rating)
            oxygen = int(oxygen_rating, 2)
            co2 = int(co2_rating, 2)
            print("Life Support Rating: ", oxygen * co2)
