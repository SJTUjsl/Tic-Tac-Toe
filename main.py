# write your code here
import sys


def convert_to_matrix(input_list):
    """

    :param input_list:Get the string the user input as parameter
    :return: Reshape the string to a matrix and return the matrix
    """
    input_list.strip()
    field_matrix = [[], [], []]
    for i in range(9):
        field_matrix[i // 3].append(input_list[i])
    return field_matrix


def check_winner(matrix):
    """

    :param matrix: the game matrix presented by 'X' and 'O'
    :return: return a list of winner names
    If everything goes OK, the winner should only contain one
    string ('X' or 'O')

    """
    winner = []

    for i in range(3):
        row_head = matrix[i][0]  # check row
        if matrix[i][1] == row_head and matrix[i][2] == row_head:
            if row_head != '_':
                winner.append(row_head)

        column_head = matrix[0][i]  # check column
        if matrix[1][i] == column_head and matrix[2][i] == column_head:
            if column_head != '_':
                winner.append(column_head)
    if matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2] \
            and matrix[0][0] != '_':  # check diagonal
        winner.append(matrix[0][0])
    if matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0] \
            and matrix[0][2] != '_':
        winner.append(matrix[0][2])
    return winner


def check_number(input_list):
    """

    :param input_list: the input string
    :return: If the number error exist, which means the difference between
    'O' and 'X' is greater than 1, return True, otherwise, return False
    """
    input_list.strip()
    x_count = input_list.count('X')
    o_count = input_list.count('O')
    if abs(x_count - o_count) > 1:
        print('Impossible')
        return True
    else:
        return False


def print_field(input_list):
    """

    :param input_list: The input string
    Print the field in correct form
    """
    input_list.strip()
    print('---------')
    print('| ' + ' '.join(input_list[:3]) + ' |')
    print('| ' + ' '.join(input_list[3:6]) + ' |')
    print('| ' + ' '.join(input_list[6:]) + ' |')
    print('---------')


# program starts here
field = input('Enter cells: ')
space = '_' in field
print_field(field)
number_err = check_number(field)
if number_err:
    sys.exit()

game_matrix = convert_to_matrix(field)
winner_names = check_winner(game_matrix)
if len(winner_names) == 0:
    if space:
        print('Game not finished')
    else:
        print('Draw')
    sys.exit()

if len(winner_names) == 2:
    print('Impossible')
    sys.exit()

if len(winner_names) == 1:
    print(f'{winner_names[0]} wins')
