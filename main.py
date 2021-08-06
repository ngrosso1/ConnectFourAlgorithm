# Nicholas J. Grosso 7/4/2021
import numpy as np

# global variables
in_session = True; # is the game still in progress?
round = 0 # Empty slot is 0
HUMAN = 1 # Human is a 1
ALG = 2 # Algorithm is a 2
COLMS = 7; # Set up colms used
ROWS = 6; # Set up rows used

def ask():
	a = int(input())
	if a <= 0 or a > COLMS:
		print("CANNOT BE LESS MIN COLMS OR GREATER THAN MAX COLMS")
		return ask()
	a -= 1 # correcting colm location (Ex. If input is 1 it chooses 1st colm instead of needing to input 0 for first colm)
	return a

def create_board():
	board = np.zeros((ROWS, COLMS))
	return board

board = create_board()

def insert(board, action, row, player):
	update = row + 1
	board[ROWS-update][action] = player

def fupq(board, action): # fupq - filled up ?
	return board[0][action] == 0

def won(board, piece):
	#verticle check
	for i in range(COLMS):
		for j in range(ROWS-3):
			if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:
				return True
	#check all same 4 pieces horizantal
	for i in range(COLMS-3):
		for j in range(ROWS):
			if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:
				return True
	#check diag going upward
	for i in range(COLMS-3):
		for j in range(ROWS-3):
			if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
				return True
	return False

while in_session:
	#its player 1s turn
	if round == 0:
		print("Human make your move: ")
		a = ask()
		if fupq(board, a):
			for row in range(ROWS):
				update = row + 1
				n = ROWS - update
				if board[n][a] == 0:
					insert(board, a, row, HUMAN)
					if won(board, 1):
						print("PLAYER 1 WINS!!!")
						in_session = False
					break
		else:
			print("!!! ERROR NOT VALID MOVE !!!")
			round += 1 # restarts a new round again for the same player
	else:
		b = ask()
		if fupq(board, b):
			for row in range(ROWS):
				update = row + 1
				n = ROWS - update
				if board[n][b] == 0:	
					insert(board, b, row, ALG)
					break
		else:
			print("!!! ERROR NOT VALID MOVE !!!")
			round += 1 # restarts a new round again for the same player
	print(board)
	round += 1
	round = round % 2
 # merge two arrays using binary sorted

 #def merge(