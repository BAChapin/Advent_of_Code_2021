import sys
sys.path.append("..")
from helper import get_lines, time_func

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

def direction(x1, y1, x2, y2):
    # 60,28 -> 893,861 (-833, -833)
    x_vector = x1 - x2
    y_vector = y1 - y2

    x = 0
    y = 0

    if x_vector > 0:
        x = -1
    elif x_vector < 0:
        x = 1

    if y_vector > 0:
        y = -1
    elif y_vector < 0:
        y = 1

    return x, y

def process():
    lines = get_lines()
    point_array = generate_point_array()

    # X will be rows
    # Y will be columns

    for line in lines:
        x1, y1, x2, y2 = get_points(line)
        x_direction, y_direction = direction(x1, y1, x2, y2)

        moving_x = x1
        moving_y = y1

        while (True):
            point_array[moving_x][moving_y] += 1
            if moving_x == x2 and moving_y == y2:
                break
            moving_x += x_direction
            moving_y += y_direction

    overlapping_points = 0

    for row_index in range(1000):
        for column_index in range(1000):
            item = point_array[row_index][column_index]
            if item > 1:
                overlapping_points += 1\

    print("Answer: ", overlapping_points)

if __name__ == "__main__":
    time_func(process)
