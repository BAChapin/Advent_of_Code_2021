import sys
sys.path.append("..")
from helper import get_lines, time_func

def calculate_fuel_consumption(distance):
    consumed = 0

    for travel in range(1, distance + 1):
        consumed += travel
    else:
        return consumed

def fuel_costs_to_position(average, crabs):
    total_consumed = 0

    for position in crabs:
        total_consumed += calculate_fuel_consumption(abs(average - position))

    return total_consumed

def process():
    lines = get_lines()
    crab_positions = [int(num) for num in lines[0].split(",")]
    average = int(sum(crab_positions) / len(crab_positions))
    consumed_fuel = fuel_costs_to_position(average, crab_positions)

    print("Answer: ", consumed_fuel)

if __name__ == "__main__":
    time_func(process)
