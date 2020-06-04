
robot_marker = '0'
player_marker = 'X'
game_on = True
player_turn = True
robot_turn = False
start = True

def display_board(board):

    print(board[1] + "|" + board[2] + "|" + board[3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])
    pass

# test_board = ['#','X','O','X','O','X',' ',' ','O','X']
# print(display_board(test_board))


def win_check(board, mark):
    return((board[1] == board[2] == board[3] == mark) or
           (board[1] == board[4] == board[7] == mark) or
           (board[1] == board[5] == board[9] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[3] == board[5] == board[7] == mark) or
           (board[7] == board[8] == board[9] == mark) or
           (board[3] == board[6] == board[9] == mark))
    pass

def place_marker(board, marker, position):
    board[position] = marker
    pass

def robot_pref(board, robot_marker):
    if board[5] == ' ':
        place_marker(board, robot_marker, 5)
    elif board[1] == ' ':
        place_marker(board, robot_marker, 1)
    elif board[3] == ' ':
        place_marker(board, robot_marker, 3)
    elif board[7] == ' ':
        place_marker(board, robot_marker, 7)
    elif board[9] == ' ':
        place_marker(board, robot_marker, 9)
    elif board[2] == ' ':
        place_marker(board, robot_marker, 2)
    elif board[4] == ' ':
        place_marker(board, robot_marker, 4)
    elif board[6] == ' ':
        place_marker(board, robot_marker, 6)
    elif board[8] == ' ':
        place_marker(board, robot_marker, 8)
    pass


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]
    pass


def replay():
    wanna_play_again = (input("Do you want to play again? y/n")).upper()
    while wanna_play_again == "Y" or wanna_play_again == " N ":
        if wanna_play_again == " Y ":
            return True
        else:
            return False


while start:
    the_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if player_turn:

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player_marker, position)
            if win_check(the_board, player_marker):
                display_board(the_board)
                print("The player won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    player_turn = False
                    robot_turn = True
        else:
            display_board(the_board)
            robot_pref(the_board, robot_marker)

            if win_check(the_board, robot_marker):
                display_board(the_board)
                print('The robot has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    player_turn = True
                    robot_turn = False

    start = replay()
