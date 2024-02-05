"""
    Tic Tac Toe Game
    Student Name: Kritish Dhakal
    Student ID: 2408573
"""


import random
import os.path
import json
random.seed()

ENCODING = "utf-8"


def draw_board(board):
    """
    Prints the tictactoe board

            Parameters:
                    board (list)

            Returns:
                    None
    """
    print('\n')
    for i in range(len(board)):
        print('  ----------- ')
        for j in range(len(board)):
            print(' | ', end="")
            print(board[i][j], end='')
        print(" | ")
    print('  ----------- ')


def welcome(board):
    """
    Prints the welcome message and the tictactoe board

            Parameters:
                    board (list)

            Returns:
                    None
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below: ')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')


def initialise_board(board):
    """
    Makes all elements of the board an empty space ' '

            Parameters:
                    board (list)

            Returns:
                    board (list)
    """
    for row_index, row in enumerate(board):
        for col_index, _ in enumerate(row):
            board[row_index][col_index] = ' '

    return board


def get_player_move(board):
    """
    Gets players move as input and converts it to row and col

            Parameters:
                    board (list)

            Returns:
                    row, col (tuple)
    """
    while 1:
        print('\n')
        print("\t\t    1  2  3 ")
        print("\t\t    4  5  6 ")
        square = int(input("Choose your square: 7  8  9 : "))

        if square not in [1,2,3,4,5,6,7,8,9]:
            square = 0

        # ? Getting the row
        if square in [1,2,3]:
            row = 0
        elif square in [4,5,6]:
            row = 1
        elif square in [7,8,9]:
            row = 2

        if square in [1,4,7]:
            col = 0
        elif square in [2,5,8]:
            col = 1
        elif square in [3,6,9]:
            col = 2

        if board[row][col] != ' ' or square == 0:
            print('\nInvalid cell selected! Please input a valid cell.')
        else:
            break

    return row, col


def choose_computer_move(board):
    """
    Gets computers move in row and col

            Parameters:
                    board (list)

            Returns:
                    row, col (tuple)
    """
    #? Looks for cells that are ' ' and stores indexes of that cell row and col as a tuple
    empty_cells = [
        (i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == ' '
    ]

    if empty_cells:
        row, col = random.choice(empty_cells)
    else:
        row, col = None, None

    return row, col


def check_for_win(board, mark):
    """
    Checks if the given mark has won or not

            Parameters:
                    board (list)
                    mark (str)

            Returns:
                    Boolean
    """
    #? Check rows to see if mark has won
    for row in board:
        win = True

        for cell in row:
            #? If one of the cell isnt mark then hasn't won
            if cell != mark:
                win = False

        #? If all of the cell is mark then mark has won
        if win:
            return True

    #? Check columns to see if mark has won
    for col in range(3):
        win = True

        for row in range(3):
            if board[row][col] != mark:
                win = False

        if win:
            return True

    #? Check diagonally to see if mark has won (\ /)
    if (board[0][0] == board[1][1] == board[2][2] == mark or
        board[0][2] == board[1][1] == board[2][0] == mark):
        return True

    return False


def check_for_draw(board):
    """
    Checks if the game has drawn or not

            Parameters:
                    board (list)

            Returns:
                    Boolean
    """
    for row in board:
        for cell in row:
            if cell == ' ':
                return False

    return True


def play_game(board):
    """
    Starts the game

            Parameters:
                    board (list)

            Returns:
                    (int)
    """
    print('\nGAME START!')
    initialise_board(board)
    draw_board(board)

    while 1:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print('You won!')
            return 1

        if check_for_draw(board):
            print('Draw!')
            return 0

        print('Computers turn...')
        row, col = choose_computer_move(board)
        board[row][col] = '0'
        draw_board(board)

        if check_for_win(board, '0'):
            print('Computer Won!')
            return -1

        if check_for_draw(board):
            print('Draw!')
            return 0

    return 0


def menu():
    """
    Prints the menu and takes user input for what they want to do

            Parameters:
                    None

            Returns:
                    choice (str)
    """
    print('\nEnter one of the following options:')
    print('\t\t 1 - Play the game')
    print('\t\t 2 - Save your score in the leaderboard')
    print('\t\t 3 - Load and display the leaderboard')
    print('\t\t q - End the program')

    choice = input('\n1, 2, 3 or q? ')

    return choice


def load_scores():
    """
    Opens the leaderboard file and retrieves the data as a dictionary

            Parameters:
                    None

            Returns:
                    leaders (dictionary)
    """
    filename = 'leaderboard.txt'

    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding = ENCODING) as file:
                leaders = json.load(file)

        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}

    return leaders


def save_score(score):
    """
    Opens the leaderboard file and saves user score in the file

            Parameters:
                    score (int)

            Returns:
                    None
    """
    if not score:
        score = 0

    name = input("Please enter your name: ")
    filename = 'leaderboard.txt'

    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding = ENCODING) as file:
                leaders = json.load(file)

        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}

    if leaders[name]:
        leaders[name] += score
    else:
        leaders[name] = score

    with open(filename, 'w', encoding = ENCODING) as file:
        json.dump(leaders, file)
        print('Updated the leaderboard!')


def display_leaderboard(leaders):
    """
    Prints the leaderboard from the leaderboard.txt file

            Parameters:
                    score (int)

            Returns:
                    None
    """
    leaders_list = list(leaders.items())
    sorted_leaders = []

    while leaders_list:
        high_score = leaders_list[0]

        for item in leaders_list:
            if item[1] > high_score[1]:
                high_score = item

        leaders_list.remove(high_score)
        sorted_leaders.append(high_score)

    for item in sorted_leaders:
        print(f"{item[0]}: {item[1]}")
