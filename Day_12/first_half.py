import sys
sys.path.append("..")
from helper import get_lines, time_func

def process():
    lines = get_lines()

if __name__ == "__main__":
    time_func(process)