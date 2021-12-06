import sys
sys.path.append("..")
from helper import get_lines

def get_points(line):
    points = line.split(" -> ")
    first_point = points[0].split(",")
    second_point = points[1].split(",")
    return int(first_point[0]), int(first_point[1]), \
           int(second_point[0]), int(second_point[1])

def generate_point_array():
    point_array = []

    for x in range(1000):
        row = []
        for y in range(1000):
            row.append(0)
        point_array.append(row)
    else:
        return point_array

if __name__ == "__main__":
    lines = get_lines()
    point_array = generate_point_array()

    # X will be rows
    # Y will be columns

    for line in lines:
        x1, y1, x2, y2 = get_points(line)

        if x1 == x2 or y1 == y2:
            if x1 > x2:
                for row_index in range(x2, x1 + 1):
                    point_array[row_index][y1] += 1
            elif x1 < x2:
                for row_index in range(x1, x2 + 1):
                    point_array[row_index][y1] += 1
            elif y1 > y2:
                for column_index in range(y2, y1 + 1):
                    point_array[x1][column_index] += 1
            elif y1 < y2:
                for column_index in range(y1, y2 + 1):
                    point_array[x1][column_index] += 1

    overlapping_points = 0

    for row_index in range(1000):
        for column_index in range(1000):
            item = point_array[row_index][column_index]
            if item > 1:
                overlapping_points += 1

    print("Answer: ", overlapping_points)
