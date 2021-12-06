import sys
sys.path.append("..")
from helper import get_lines, time_func

def process():
    lines = get_lines()
    lantern_fish = [int(num) for num in lines[0].split(",")]

    new_fish = []
    for day in range(80):
        for fish_index in range(len(lantern_fish)):
            fish = lantern_fish[fish_index]
            if fish == 0:
                lantern_fish[fish_index] = 6
                new_fish.append(8)
            else:
                lantern_fish[fish_index] -= 1
        else:
            lantern_fish = lantern_fish + new_fish
            new_fish = []
    else:
        print("Total Fish after 80 Days: ", len(lantern_fish))

if __name__ == "__main__":
    time_func(process)