import random
from colorama import *
def board_is_full():
   for row in board:
       for value in row:
           if value == ' ':
               return False
   return True

def print_board():
    for row in board:
        print(Fore.CYAN+'-'*10)
        print(Fore.BLUE+'|', end="")
        for value in row:
            print(value,'|',end="")
        print()
    print(Fore.CYAN+'-'*10)

def winner():
    counter = 0
    diag1 = []
    diag2 = []
    for i in range(len(board)):
        diag1.append(board[counter][counter])#ghotre asli(main diagonal)
        diag2.append(board[2-counter][counter])#ghotre farei(second diagonal)
        counter += 1
        row=""
        col=""
        for j in range(len(board)): #winner in row or column
            row+=board[i][j]
            col+=board[j][i]
        if row in ("XXX","OOO") or col in ("XXX","OOO") or  diag1 in (['X','X','X'],['O','O','O']) or  diag2 in (['X','X','X'],['O','O','O']):
            return True
    return False
def changeplayer():
  global player
  player = player % 2 +1

def set_position():
    position =input(Fore.LIGHTRED_EX+"enter position 1-9:")
    while position not in ["1","2","3","4","5","6","7","8","9"]:
         position = input(Fore.LIGHTRED_EX + "enter position 1-9:")
    position=int(position)
    row_ = (position - 1) // 3
    col_ = (position - 1) % 3
    if board[row_][col_] != " ":
        print("This place is taken,plz try again!!!")
    else:
        board[row_][col_] = 'X' if player == 1 else 'O'

if __name__ == '__main__':
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    random_list = (1, 2)#choose player randomly at first
    player = random.choice(random_list)
    while winner() == False and board_is_full()==False:
        print(Fore.YELLOW+"Player Number " + str(player) + "'s Turn!!")
        print_board()
        set_position()
        changeplayer()
    if winner():
        print(Fore.MAGENTA+"we have a winner.")
    else:
        print(Fore.MAGENTA+"No winner!!!")