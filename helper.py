from time import time

def get_lines():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

def time_func(func):
    start_time = time()
    func()
    end_time = time()
    print(end_time - start_time)