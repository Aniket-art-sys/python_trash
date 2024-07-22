import random


def create_board():
    return [0] * 9
def print_board(board,type):
    def convert(board,id):
        if(board[id]==1):
            return "X"
        elif(board[id]==-1):
            return "O"
        else:
            return " "
    for _ in range(0,7,3):
        if(type):
            print(convert(board,_),"|",convert(board,_+1),"|",convert(board,_+2))
        else:
            print(_,"|", _+1,"|",_+2)
def plays(board,no,ai):
    if ai and no%2==1 :
        board[ai_move(board,no)]=-1
    else:
        while (True):
            try:
                board_input = int(input("enter pos according to the map"))
            except ValueError:
                print("Invalid input try again 0-8")
                continue

            if (board_input > 8 or board_input < 0):
                print("Invalid input try again 0-8")
            elif (board[board_input] != 0):
                print("already occupied")
            else:
                board[board_input] = (1 if no % 2 == 0 else -1 if no % 2 == 1 else 0)
                break
def check(board):
    win_con = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win_con:
        if board[a] == board[b] == board[c] and board[a] != 0:
            return board[a]
    return 0
def ai_move(board,no):
    if no == 1:
        for i in [4, 0, 2, 6, 8]:
            if board[i] == 0:
                return i
    elif no % 2 == 1:
        pos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        pos2 = [
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in pos:
            if sum([board[a], board[b], board[c]]) == -2:
                if board[a] == 0:
                    return a
                if board[b] == 0:
                    return b
                if board[c] == 0:
                    return c
            elif sum([board[a], board[b], board[c]]) == 2:
                if board[a] == 0:
                    return a
                if board[b] == 0:
                    return b
                if board[c] == 0:
                    return c
        for a, b, c in pos2:
            if board[a] == 1 and board[b] == -1 and board[c] == 1:
                for i in [1, 3, 5, 7]:
                    if board[i] == 0:
                        return i
        for a, b, c in pos2:
            if (board[a] == -1 and board[b] == 1 and board[c] == 1) or (
                    board[a] == 1 and board[b] == 1 and board[c] == -1):
                for i in [0, 2, 6, 8]:
                    if board[i] == 0:
                        return i
        while True:
            u = random.randrange(0, 9)
            if board[u] == 0:
                return u


def play():
    board = create_board()
    for _ in range(9):
        print("mapping for the board")
        print_board(board,False)
        print("status of the board")
        print_board(board,True)
        plays(board,_,True)
        if(check(board)==1):
            print_board(board, True)
            print("X has won")
            break
        elif(check(board)==-1):
            print_board(board, True)
            print("O has won")
            break
    else:
        print_board(board, True)
        print("It's a tie!")
while(True):
    play()
