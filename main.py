# Nicholas J. Grosso 7/4/2021
import numpy as np
import pygame
import math
import sys

# Global variables

# Colors
BLUE = (0,0,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Test for in game and for what version, 2 people or AI
in_session = True # is the game still in progress?
first_round = True # Bool value to see if we are in the first round
AI = False # Bool to see if the game was started up to play with AI instead
round = 0 # Empty slot is 0

HUMAN = 1 # Human is a 1
ALG = 2 # Algorithm is a 2
COLMS = 7 # Set up colms used
ROWS = 6 # Set up rows used

pygame.init()
myfont = pygame.font.SysFont("monospace", 75)
SQUARESIZE = 100
width = COLMS * SQUARESIZE
height = ( ROWS + 1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
radius = int(SQUARESIZE/2 - 5)

def draw_board(board):
	for i in range(COLMS):
		for j in range(ROWS):
			pygame.draw.rect(screen, BLUE, (i*SQUARESIZE, j*SQUARESIZE+SQUARESIZE , SQUARESIZE, SQUARESIZE))
			if board[j][i] == 0:
				pygame.draw.circle(screen, BLACK, (int(i*SQUARESIZE+SQUARESIZE/2), int(j*SQUARESIZE+SQUARESIZE/2)), radius)
			elif board[j][i] == 1:
				pygame.draw.circle(screen, RED, (int(i*SQUARESIZE+SQUARESIZE/2), int(j*SQUARESIZE+SQUARESIZE/2)), radius)
			elif board[j][i] == 2:
				pygame.draw.circle(screen, YELLOW, (int(i*SQUARESIZE+SQUARESIZE/2), int(j*SQUARESIZE+SQUARESIZE/2)), radius)
	pygame.display.update()

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
draw_board(board)
pygame.display.update()

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
		for j in range(ROWS-3, ROWS):
			if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
				return True
	#check diag going downward
	for i in range(COLMS-3):
		for j in range(ROWS-3):
			if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
				return True
	draw_board(board)

while in_session == True and AI == False:
	if first_round:
		first_round = False
		if len(sys.argv) > 1:
			if sys.argv[1] == "AI":
				AI = True
				break
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if round == 0:
				 pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), radius)
			else:
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), radius)
		pygame.display.update()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#its player 1s turn
			if round == 0:
				posx = event.pos[0]
				a = int(math.floor(posx/SQUARESIZE))
				print("Human make your move: ")
				#a = ask()
				if fupq(board, a):
					for row in range(ROWS):
						update = row + 1
						n = ROWS - update
						if board[n][a] == 0:
							insert(board, a, row, HUMAN)
							if won(board, 1):
								draw_board(board)
								label = myfont.render("PLAYER 1 WINS!!!", 1, RED)
								screen.blit(label, (40,10))
								pygame.display.flip()
								pygame.event.pump()
								pygame.time.delay(3000)
								in_session = False
							break
					round += 1
					round = round % 2
					print(board)
					draw_board(board)
				else:
					print("!!! ERROR NOT VALID MOVE !!!")
					round += 1 # restarts a new round again for the same player
			else:
				posx = event.pos[0]
				b = int(math.floor(posx/SQUARESIZE))
				#b = ask()
				if fupq(board, b):
					for row in range(ROWS):
						update = row + 1
						n = ROWS - update
						if board[n][b] == 0:	
							insert(board, b, row, ALG)
							if won(board, 2):
								draw_board(board)
								label = myfont.render("PLAYER 2 WINS!!!", 1, YELLOW)
								screen.blit(label, (40,10))
								pygame.display.flip()
								pygame.event.pump()
								pygame.time.delay(3000)
								in_session = False
							break
					print(board)
					draw_board(board)
					round += 1
					round = round % 2
				else:
					print("!!! ERROR NOT VALID MOVE !!!")
					round += 1 # restarts a new round again for the same player
