# Nicholas J. Grosso 7/4/2021
import numpy as np
import pygame
import math
import sys
import tkinter
import random

# Global variables
top = tkinter.Tk() # Prompt variable
top.title("Select mode: ") # Title for prompt window
top.geometry("250x100") # Prompt window size
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
# Values for board construction
HUMAN = 1 # Human is a 1
ALG = 2 # Algorithm is a 2
COLMS = 7 # Set up colms used
ROWS = 6 # Set up rows used

#Functions for prompt
def byeBF():
	global AI 
	AI = False
	top.destroy()
def byeBT():
	global AI 
	AI = True
	top.destroy()

# First button for prompt window for PVP
B1 = tkinter.Button(top, text ="Player vs Player", command = byeBF).pack()
# Second button for prompt window for alg
B2 = tkinter.Button(top, text = "Player vs MinMax", command = byeBT).pack()
top.mainloop() # Keeps prompt live until button destroys it
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

# def ask():
# 	a = int(input())
# 	if a <= 0 or a > COLMS:
# 		print("CANNOT BE LESS MIN COLMS OR GREATER THAN MAX COLMS")
# 		return ask()
# 	a -= 1 # correcting colm location (Ex. If input is 1 it chooses 1st colm instead of needing to input 0 for first colm)
# 	return a

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
	# Verticle check
	for i in range(COLMS):
		for j in range(ROWS-3):
			if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:
				return True
	# Check all same 4 pieces horizantal
	for i in range(COLMS-3):
		for j in range(ROWS):
			if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:
				return True
	# Check diag going upward
	for i in range(COLMS-3):
		for j in range(ROWS-3, ROWS):
			if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
				return True
	# Check diag going downward
	for i in range(COLMS-3):
		for j in range(ROWS-3):
			if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
				return True
	draw_board(board)

while in_session == True:
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
			if round == 0: # Its player 1 (or humans) turn
				posx = event.pos[0]
				colmSelected = int(math.floor(posx/SQUARESIZE))
				print("Human make your move: ")
				if fupq(board, colmSelected):
					for row in range(ROWS):
						update = row + 1
						n = ROWS - update
						if board[n][colmSelected] == 0:
							insert(board, colmSelected, row, HUMAN)
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
					round += 1 # Restarts a new round again for the same player
			elif AI == False and round == 1:
				posx = event.pos[0]
				colmSelected = int(math.floor(posx/SQUARESIZE))
				if fupq(board, colmSelected):
					for row in range(ROWS):
						update = row + 1
						n = ROWS - update
						if board[n][colmSelected] == 0:	
							insert(board, colmSelected, row, ALG)
							if won(board, 2):
								draw_board(board)
								label = myfont.render("PLAYER 2 WINS!!!", 1, YELLOW)
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
					round += 1 # Restarts a new round again for the same player
	if AI == True and round == 1: # If MinMax is selected
		colmSelected = random.randint(0, COLMS-1)
		if fupq(board, colmSelected):
			for row in range(ROWS):
				update = row + 1
				n = ROWS - update
				if board[n][colmSelected] == 0:	
					insert(board, colmSelected, row, ALG)
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
			round += 1 # Restarts a new round again for the same player
