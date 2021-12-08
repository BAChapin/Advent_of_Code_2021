
def process(lines, at_index):
    threshold = len(lines) / 2
    most_common_pos = 0

    for line in lines:
        pos_int = int(line[at_index])
        most_common_pos += pos_int
    else:
        if most_common_pos >= threshold:
            return "1", "0"
        else:
            return "0", "1"

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
        most_common = ""
        least_common = ""

        for position in range(0, len(lines[0]) - 1):
            most_common_pos, least_common_pos = process(lines, position)
            most_common += most_common_pos
            least_common += least_common_pos
        else:
            decimal_gamma = int(most_common, 2)
            decimal_epsilon = int(least_common, 2)
            print("Answer: ", decimal_epsilon * decimal_gamma)

