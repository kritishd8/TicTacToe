"""
    Tic Tac Toe Game
    Student Name: Kritish Dhakal
    Student ID: 2408573
"""

from noughtsandcrosses_2408573 import *


def main():
    board = [ ['1','2','3'], ['4','5','6'], ['7','8','9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


if __name__ == '__main__':
    main()
