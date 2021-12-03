
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
        most_common = ""
        least_common = ""
        input_len = len(lines)
        line_len = len(lines[0])

        for position in range(0, line_len - 1):
            most_common_pos = 0
            for line in lines:
                pos_int = int(line[position])
                most_common_pos += pos_int
            else:
                if most_common_pos >= (input_len / 2):
                    most_common += "1"
                    least_common += "0"
                else:
                    most_common += "0"
                    least_common += "1"
        else:
            print("Raw Gamma Rate - ", most_common)
            print("Raw Epsilon Rate - ", least_common)

            decimal_gamma = int(most_common, 2)
            decimal_epsilon = int(least_common, 2)
            print("Answer: ", decimal_epsilon * decimal_gamma)

