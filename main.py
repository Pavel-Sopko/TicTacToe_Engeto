import random

def print_board(a):
    print(a[1], "  |  ", a[2], "  |  ", a[3])
    print("-------------------")
    print(a[4], "  |  ", a[5], "  |  ", a[6])
    print("-------------------")
    print(a[7], "  |  ", a[8], "  |  ", a[9])


def is_board_full(board):
    return board.count(" ") == 1


def is_free(board, pos):
    return board[pos] == " "


def insert_letter(board, l, move):
    board[move] = l


def player_move(board, let):
    flag = True
    while flag:
        move = input("Enter player move from 1-9: ")
        try:
            move = int(move)

            if move > 0 and move < 10:
                if is_free(board, move):
                    flag = False
                    insert_letter(board, let, move)
                else:
                    print("No vacant space")
            else:
                print("Enter valid input in range of 1-9.")
        except:
            print("Enter valid input.")


def is_winner(board, le):
    return (board[1] == le and board[2] == le and board[3] == le) or (
            board[4] == le and board[5] == le and board[6] == le) or (
                   board[7] == le and board[8] == le and board[9] == le) or (
                   board[1] == le and board[4] == le and board[7] == le) or (
                   board[2] == le and board[5] == le and board[8] == le) or (
                   board[9] == le and board[6] == le and board[3] == le) or (
                   board[7] == le and board[5] == le and board[3] == le) or (
                   board[9] == le and board[5] == le and board[1] == le)


def select_random(a):
    r = random.randrange(0, len(a))
    return a[r]


def comp_move(board):
    poss_moves = [i for i, j in enumerate(board) if j == " " and i > 0]
    move = 0

    for let in ['X', 'O']:
        for i in poss_moves:
            a = board[:]
            a[i] = let
            if is_winner(a, let):
                move = i
                return move
    open_corners = []
    for i in poss_moves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    if len(open_corners) > 0:
        move = select_random(open_corners)
        return move
    if 5 in poss_moves:
        return 5
    if len(poss_moves) > 0:
        move = select_random(poss_moves)
    return move


board = [" " for x in range(10)]


def main():
    Oddelovac = "=" * 40
    Oddelovac_mini = "-" * 40
    print(f"""
    {"Welcome to Tic Tac Toe":^40}
    {Oddelovac}
    {"GAME RULES:":^40}
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row
    {Oddelovac}
    {"Lets start the game!":^40}
    {Oddelovac_mini}
    """)
    print(f"{'1 - player vs player':^40}")
    print(f"{'2 - player vs computer':^40}")
    print(f"{'3 - computer vs computer':^40}")
    p = 0
    l = ["Player vs player mode. Let's go.", "Player vs computer mode. Let's go.", "Computer vs computer mode."]
    flag = True
    while flag:
        print()
        p = input("Enter the mode game, please: ")
        try:
            p = int(p)
            if p in [1, 2, 3]:
                flag = False
                print("You have selected: ", l[p - 1])
            else:
                print("Please select correct option in range of [1,2,3].")

        except:
            print("Enter valid number.")

    print_board(board)

    while not (is_board_full(board)):
        if not is_winner(board, 'O'):

            if p != 3:
                print("Player turn.")
                player_move(board, 'O')
            else:
                move = comp_move(board)
                if move == 0:
                    print("Tie game.")
                else:
                    print("Computer placed at ", move, " position.")
                    insert_letter(board, 'O', move)
                # printBoard(board)
            print_board(board)

            if is_winner(board, 'O'):
                print("O\'s won the game '")
                break
        else:
            print("O\'s won the game")
            break
        if not is_winner(board, 'X'):
            if p != 1:
                move = comp_move(board)
                if move == 0:
                    print("tie game")
                else:
                    print("computer placed at ", move, " position")
                    insert_letter(board, 'X', move)

            else:
                print("player turn")
                player_move(board, 'X')
            if is_winner(board, 'O'):
                print("X\'s won the game '")
                break
            print_board(board)
        else:
            print("X\'s won the game'")
            break

    if is_board_full(board):
        print("Tie game.")


main()
