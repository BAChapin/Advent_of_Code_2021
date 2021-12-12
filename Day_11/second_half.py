import sys
sys.path.append("..")
from helper import get_lines, time_func

octopuse_matrix = []

def get_surrounding_indices(point):
    row, column = point
    matrix_length = len(octopuse_matrix) - 1
    row_length = len(octopuse_matrix[row]) - 1
    index_array = []
    if row > 0:                                     # Up
        new_point = (row - 1, column)
        index_array.append(new_point)
        if column > 0:                              # Up-Left
            new_point = (row - 1, column - 1)
            index_array.append(new_point)
        if column < row_length:                     # Down-Left
            new_point = (row - 1, column + 1)
            index_array.append(new_point)

    if row < matrix_length:                         # Down
        new_point = (row + 1, column)
        index_array.append(new_point)
        if column > 0:                              # Up-Right
            new_point = (row + 1, column - 1)
            index_array.append(new_point)
        if column < row_length:                     # Down-Right
            new_point = (row + 1, column + 1)
            index_array.append(new_point)

    if column > 0:                                  # Left
        new_point = (row, column - 1)
        index_array.append(new_point)

    if column < row_length:                         # Right
        new_point = (row, column + 1)
        index_array.append(new_point)

    return index_array

def flash(point):
    flashes = 1
    array = get_surrounding_indices(point)
    for row, column in array:
        octopuse_matrix[row][column] += 1
        if octopuse_matrix[row][column] > 9 and \
           octopuse_matrix[row][column] < 11:
           array_point = (row, column)
           flashes += flash(array_point)
    else:
        return flashes

def step():
    flashes = 0
    matrix_length = len(octopuse_matrix)
    for row in range(matrix_length):
        row_length = len(octopuse_matrix[row])
        for column in range(row_length):
            octopuse_matrix[row][column] += 1
            if octopuse_matrix[row][column] > 9 and \
                octopuse_matrix[row][column] < 11:
                point = (row, column)
                flashes += flash(point)
    return flashes

def reset_matrix():
    matrix_length = len(octopuse_matrix)
    syncronized = True
    for row in range(matrix_length):
        row_length = len(octopuse_matrix[row])
        for column in range(row_length):
            if octopuse_matrix[row][column] > 9:
                octopuse_matrix[row][column] = 0
            else:
                syncronized = False
    return syncronized

def get_octopuse_matrix(lines):
    for line in lines:
        line_array = [int(x) for x in line.strip("\n")]
        octopuse_matrix.append(line_array)

def process():
    lines = get_lines()
    get_octopuse_matrix(lines)
    flashes = 0
    rounds = 0
    synced = False

    while (not synced):
        flashes += step()
        synced = reset_matrix()
        rounds += 1
    print("Answer: ", rounds)


if __name__ == "__main__":
    time_func(process)