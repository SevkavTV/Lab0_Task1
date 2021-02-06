'''
Lab 0, Task 1. Archakov Vsevolod.
GitHub link: https://github.com/SevkavTV/Lab0_Task1.git
'''


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    """
    board = []
    with open(path, 'r') as file:
        for line in file:
            board.append(line.split('\n')[0])

    return board


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 4)
    False
    """
    board_str = input_line[1:-1]
    last_biggest = -1
    count_bigger = 0

    for elem in board_str:
        curr_num = int(elem)
        if curr_num > last_biggest:
            last_biggest = curr_num
            count_bigger += 1

    if pivot == count_bigger:
        return True

    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5',\
'*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        if '?' in line:
            return False

    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """
    for index, line in enumerate(board):
        if index not in (0, len(board) - 1):
            board_line = line[1:-1]
            for elem in board_line:
                if board_line.count(elem) > 1:
                    return False

    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """
    if check_not_finished_board(board) and check_uniqueness_in_rows(board):
        for index, line in enumerate(board):
            if index not in (0, len(board) - 1):
                if line[0] != '*':
                    if not left_to_right_check(line, int(line[0])):
                        return False

                if line[len(line)-1] != '*':
                    if not left_to_right_check(line[::-1], int(line[len(line)-1])):
                        return False

        return True

    return False


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
'*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
'*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*',\
'*41532*', '*2*1***'])
    False
    """
    inverted_board = [[] for _ in range(0, len(board))]

    for line in board:
        for index_column, value in enumerate(line):
            inverted_board[index_column].append(value)

    if check_horizontal_visibility(inverted_board):
        return True

    return False


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)

    if check_horizontal_visibility(board) and check_columns(board):
        return True

    return False


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
