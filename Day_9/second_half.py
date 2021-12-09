import sys
from math import prod
sys.path.append("..")
from helper import get_lines, time_func

def get_numbers(line):
    numbers = []
    for i in range(len(line)):
        if line[i] != "\n":
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

def surrounding_low_points(point, number_matrix):
    row, column = point
    points = []

    if row > 0 and number_matrix[row - 1][column] != 9:
        points.append((row - 1, column))

    if row < len(number_matrix) - 1 and number_matrix[row + 1][column] != 9:
        points.append((row + 1, column))

    if column > 0 and number_matrix[row][column - 1] != 9:
        points.append((row, column - 1))

    if column < len(number_matrix[row]) - 1 and number_matrix[row][column + 1] != 9:
        points.append((row, column + 1))

    return points
        

def basin_size(point, number_matrix):
    unique_points = set(surrounding_low_points(point, number_matrix))
    old_size = 0
    new_size = len(unique_points)

    while new_size > old_size:
        new_points = set()
        for point in unique_points:
            new_points.update(surrounding_low_points(point, number_matrix))
        else:
            unique_points.update(new_points)
            old_size = new_size
            new_size = len(unique_points)

    return len(unique_points)

def lowest_points(number_matrix):
    points = []

    for row in range(len(number_matrix)):
        for column in range(len(number_matrix[row])):
            check = number_matrix[row][column]
            if check != 9:
                numbers_surrounding = surrounding_numbers(row, column, number_matrix)
                for number in numbers_surrounding:
                    if check >= number:
                        break
                else:
                    points.append((row, column))

    return points

def process():
    lines = get_lines()
    number_matrix = []

    for line in lines:
        number_matrix.append(get_numbers(line))

    low_points = lowest_points(number_matrix)
    basin_sizes = []

    for point in low_points:
        basin = basin_size(point, number_matrix)
        basin_sizes.append(basin)
    else:
        basin_sizes.sort(reverse=True)
        largest_three = basin_sizes[0:3]
        answer = prod(largest_three)
        print("Answer: ", answer)

if __name__ == "__main__":
    time_func(process)