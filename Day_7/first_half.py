import sys
sys.path.append("..")
from helper import get_lines, time_func

def cheapest_fuel_cost(positions, unique_positions):
    fuel_costs = []

    for unique in unique_positions:
        fuel_cost = 0
        for position in positions:
            fuel_cost += abs(unique - position)
        fuel_costs.append(fuel_cost)
    
    cheapest_cost = None

    for fuel_cost in fuel_costs:
        if not cheapest_cost:
            cheapest_cost = fuel_cost
        else:
            if cheapest_cost > fuel_cost:
                cheapest_cost = fuel_cost

    return cheapest_cost

def process():
    lines = get_lines()
    crab_positions = [int(num) for num in lines[0].split(",")]
    positions = set(crab_positions)
    fuel_spent = cheapest_fuel_cost(crab_positions, positions)

    print("Answer: ", fuel_spent)


if __name__ == "__main__":
    time_func(process)

