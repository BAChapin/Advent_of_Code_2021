import sys
sys.path.append("..")
from helper import get_lines

def create_board(number, lines):
    numbers = dict()

    for row_index in range(0, len(lines)):
        line = lines[row_index]
        split_line = line.split(" ")
        for item in split_line:
            if item == "":
                split_line.remove(item)
        for column_index in range(0, len(split_line)):
            if split_line[column_index] != "":
                value = int(split_line[column_index])
                new_entry = {column_index : value}
                if numbers.get(row_index) is not None:
                    numbers[row_index].update(new_entry)
                else:
                    numbers[row_index] = new_entry
    else:
        return {number : numbers}

def call(number, board):
    board = board
    for row_index in range(0, 5):
        for column_index in range(0, 5):
            row = board.get(row_index)
            item = row.get(column_index)
            if item == number:
                board[row_index][column_index] = None
                bingo = is_bingo(board)
                return board, bingo
    else:
        return board, False

def is_bingo(board):
    rows = [0, 0, 0, 0, 0]
    columns = [0, 0, 0, 0, 0]

    for row_index in range(0, 5):
        for column_index in range(0, 5):
            if board[row_index][column_index] is None:
                rows[row_index] += 1
                columns[column_index] += 1
    
                if rows[row_index] == 5 or columns[column_index] == 5:
                    return True
    
    return False

def calculate_score(last_number, board):
    running_total = 0
    for row_index in range(0, 5):
        for column_index in range(0, 5):
            item = board[row_index].get(column_index)
            if item:
                running_total += item
    else:
        return running_total * last_number


if __name__ == "__main__":
    lines = get_lines()
    number_line = lines[0]
    called_numbers = number_line.split(",")
    boards = dict()
    bingo_board = None

    start_index = 2
    for index in range(2, len(lines)):
        if lines[index] == "\n":
            num_boards = len(boards) + 1
            board_lines = lines[start_index : index]
            new_board = create_board(num_boards, board_lines)
            start_index = index + 1
            boards.update(new_board)
    
    bingo_board = None
    last_called = None
    has_bingo = False

    for value in called_numbers:
        number = int(value)
        for board_num in range(1, 101):
            board = boards[board_num]
            new_board, bingo = call(number, board)
            boards[board_num].update(new_board)
            if bingo:
                bingo_board = new_board
                print("Bingo!")
                has_bingo = True
                last_called = number
                break

        if has_bingo:
            break

    print("Answer: ", calculate_score(last_called, bingo_board))

