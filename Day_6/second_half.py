import sys
sys.path.append("..")
from helper import get_lines, time_func

def process_fish(lantern_fish):
    fish_matrix = {}
    for fish in lantern_fish:
        if fish_matrix.get(fish):
            fish_matrix[fish] += 1
        else:
            fish_matrix[fish] = 1
    else:
        return fish_matrix

def process_day(lantern_fish):
    fish_matrix = {}

    for day in range(9):
        fish = lantern_fish.get(day)
        if fish and day == 0:
            fish_matrix[6] = fish
            fish_matrix[8] = fish
        elif fish:
            if fish_matrix.get(day - 1):
                fish_matrix[day - 1] += fish
            else:
                fish_matrix[day - 1] = fish
    else:
        return fish_matrix

def total_fish(lantern_fish):
    running_total = 0

    for key in lantern_fish.keys():
        running_total += lantern_fish[key]
    else:
        return running_total

def process():
    lines = get_lines()
    lantern_fish = [int(num) for num in lines[0].split(",")]
    lantern_fish = process_fish(lantern_fish)

    for day in range(256):
        lantern_fish = process_day(lantern_fish)
    else:
        print("Total Fish after 256 Days: ", total_fish(lantern_fish))



if __name__ == "__main__":
    time_func(process)