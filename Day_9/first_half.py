import sys
sys.path.append("..")
from helper import get_lines, time_func

def get_numbers(line):
    numbers = []
    for i in range(len(line) - 1):
        numbers.append(int(line[i]))
    
    return numbers

def surrounding_numbers(row, column, number_matrix):
    numbers = []
    if row > 0:
        numbers.append(number_matrix[row - 1][column])

    if row < len(number_matrix) - 1:
        numbers.append(number_matrix[row + 1][column])

    if column > 0:
        numbers.append(number_matrix[row][column - 1])

    if column < len(number_matrix[row]) - 1:
        numbers.append(number_matrix[row][column + 1])

    return numbers
    

def process():
    lines = get_lines()
    number_matrix = []

    for line in lines:
        number_matrix.append(get_numbers(line))

    lowest_points = []

    for row in range(len(number_matrix)):
        for column in range(len(number_matrix[row])):
            check = number_matrix[row][column]
            if check != 9:
                numbers_surrounding = surrounding_numbers(row, column, number_matrix)
                for number in numbers_surrounding:
                    if check >= number:
                        break
                else:
                    lowest_points.append(check)

    points_sum = sum(lowest_points) + len(lowest_points)
    print("Answer: ", points_sum)

if __name__ == "__main__":
    time_func(process)