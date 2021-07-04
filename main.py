# Nicholas J. Grosso 7/4/2021
import numpy as np

#global variables
in_session = True; # is the game still in progress?
round = 0 # Empty slot is 0
HUMAN = 1 # Human is a 1
ALG = 2 # Algorithm is a 2
COLMS = 7; # Set up colms used
ROWS = 6; # Set up rows used

def create_board():
	board = np.zeros((ROWS, COLMS))
	return board

board = create_board();

def insert(board, action, row, player):
	update = row + 1
	board[ROWS-update][action] = player

def fupq(board, action): # fupq - filled up ?
	return board[0][action] == 0

def won(board, piece):
	#check all same 4 pieces each colm
	for i in range(COLMS):
		continue
	#check all same 4 pieces each row
	#verticle
	return null

while in_session:
	#its player 1s turn
	if round == 0:
		print("Human make your move: ")
		a = int(input())
		a -= 1 # correcting colm location (Ex. If input is 1 it chooses 1st colm instead of needing to input 0 for first colm)
		if fupq(board, a):
			for row in range(ROWS):
				update = row + 1
				n = ROWS - update
				if board[n][a] == 0:
					#print("going to insert")
					insert(board, a, row, HUMAN)
					break
		else:
			print("!!! ERROR NOT VALID MOVE !!!")
			round += 1 # restarts a new round again for the same player
	else:
		b = int(input())
		b -= 1 # correcting colm location
		if fupq(board, b):
			for row in range(ROWS):
				update = row + 1
				n = ROWS - update
				if board[n][b] == 0:
					#print("going to insert")
					insert(board, b, row, ALG)
					break
		else:
			print("!!! ERROR NOT VALID MOVE !!!")
			round += 1 # restarts a new round again for the same player

	print(board)
	round += 1
	round = round % 2
