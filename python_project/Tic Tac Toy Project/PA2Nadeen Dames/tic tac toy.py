
#
# Global variables
#

# Game board
board = [''] * 10

# Players
player1 = 'X'
player2 = 'O'

# Keep track of the game status
is_running = False

# Keep track of the current player
global current_player
current_player = player1

# Won
x_won='X won!'
o_won='O won!'

# Score
global scoreX
scoreX=0
global scoreY
scoreY=0
#
# Functions
#

# print_board(board) - Pretty printing of the game board


def print_board(board):
    print(f"\n\n\t|\t|\t")
    print(f"\t{board[6]}\t|\t{board[7]}\t|\t{board[8]}\t")
    print(f"\t|\t|\t")
    print(f"\t{board[3]}\t|\t{board[4]}\t|\t{board[5]}")
    print(f"\t|\t|\t")
    print(f"\t{board[0]}\t|\t{board[1]}\t|\t{board[2]}")
    print(f"\t|\t|\t")

    print(board)


# ask_for_move(player) - Ask user to provide input for move

def ask_for_move(player):
    position = int(input(f"{player}'s turn. Choose a position (1-9):"))
    if position in range(1, 10):
        while not make_move(player, position):
            position = int(input(f"{player}'s turn. Choose a position (1-9):"))

        # Print the board after the move
        print_board(board)

        # Check if player won
        if check_win(board, player) == player:
            global is_running
            is_running = False
            global scoreX
            scoreX+=1
            print(f"Congratulations {x_won} and Score : {scoreX}")
            start_game()   
        elif check_win(board,player)==player:
            #global is_running
            is_running = False
            global scoreY
            scoreY+=1
            print(f"Congratulations {o_won} and Score : {scoreY}")
            
            start_game()   

          
        else:
            # Switch the players
            swtich_player()

    else:
        print("Invalid input. Choose position from (1-9).")
        ask_for_move(player)

# swtich_player()


def swtich_player():
    global current_player
    if current_player is player1:
        current_player = player2
    else:
        current_player = player1

# make_move()


def make_move(player, position):
    if board[position-1] == '':
        board[position-1] = player
        return True
    else:
        print("Invalid position. Try again.")
        return False

# check_win()


def check_win(board, player):

    if (board.count(player1) + board.count(player2)) >= 3:
        # Rows
        if (board[0] and board[1] and board[2]) == player or (board[3] and board[4] and board[5]) == player or (board[6] and board[7] and board[8]) == player:
            return player
        # Coloumns
        elif (board[0] and board[3] and board[6]) == player or (board[1] and board[4] and board[7]) == player or (board[2] and board[5] and board[8]) == player:
            return player
        # Diagonals
        elif (board[0] and board[4] and board[8]) == player or (board[2] and board[4] and board[6]) == player:
            return player
        else:
            return None

# start_game()


def start_game():
    print("Welcome...Dear ! Are you ready playing Tic-Tac-Toe")
    #board.clear()

    is_running = True

    while is_running:
        ask_for_move(current_player)
        
        print("Thanks for using our Tic-Tac-Toe. Bye!")
    
    


# main
start_game()
