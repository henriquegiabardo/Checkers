import numpy as np
import pygame
import sys
import math

# Jogo de Damas

# Challenge Qulture Rocks

# Autor Henrique Geribello 
# Data 01/05/2020]

# useful/used videos:
# how to play checkers www.youtube.com/watch?v=ScKIdStgAfU
# pygame checkers www.youtube.com/watch?v=ScKIdStgAfU	
# conect 4 tutorial pygames www.youtube.com/watch?v=XpYz-q1lxu8																		

# rules : if a player can make a capture, he has make the capture
# 		  if a player cannot make a move or loses all his pieces, he loses


# still need to implement the king mecanics and the "Lose because cant move feature"
# some bugs with lower rows (row 9)


# things to improve: 
# instead use parameter "Piece" (1 or 2) i should change for "Player", since i always pass 1 or 2 and i check inside the functions if the piece on the board is an 1 or 11 (pawn or king)

# colors that will be used on the game
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0)
DARK_RED = (155, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (210, 210, 210)
YELLOW = (255, 255, 0)

def its_even(i):
	if (i % 2) == 0:
		return True
	else:
		return False

def create_board(): # create and prepare the board
	board = np.zeros((10,10))

	for i in range(0,9): # these are the borders
		board[0, i] = i
		board[i, 0] = i 
		board[9, i] = i 
		board[i, 9] = i 

	for row in range(1,4): # put the RED pieces in their place
		for col in range(1,9):
			if (its_a_valid_space(row, col)): 
				board[row][col] = 2 #2 are the RED pieces

		for row in range(6,9): # put the WHITE pieces in their place
			for col in range(1,9):
				if (its_a_valid_space(row, col)):
					board[row][col] = 1 # 1 are the white pieces 

	return board 


def its_a_valid_space(row,col): # verify if its a space that is used in the game
	if not (row == 0 or row == 9 or col == 0 or col == 9): # if its not a border
		if ( its_even(row) and not its_even(col)) or (not its_even(row) and its_even(col)): # its a BLACK space
			return True
	return False

def move_piece(board, piece, piece_row, piece_col, next_row, next_col): # move a piece to an empty (0) space

	# before i used a input by writing in the terminal, the code is comentted
	#did_a_valid_move = False
	#while not(did_a_valid_move):
		#piece_row, piece_col = [int(x) for x in input("Select the piece you want to move with row and col (0-7):").split()]
		#print('row:', piece_row, 'col:', piece_col)
		#next_row, next_col = [int(x) for x in input("Select the place you want to put the piece with row and col (0-7):").split()]
		#print('place row:', next_row, 'place col:', next_col)

		
	if move_is_valid(board, piece_row, piece_col, next_row, next_col, piece):
		board[next_row][next_col] = piece
		board[piece_row][piece_col] = 0
		did_a_valid_move = True
		return True

	else:
		#print ("Not a Valid Move") used for debug
		return False

def move_is_valid(board, actual_row, actual_col, next_row, next_col, piece):
	if (its_a_valid_space(actual_row, actual_col) and its_a_valid_space(next_row, next_col) and (board[actual_row][actual_col] == piece)): # first basic check
		if (piece == 1): 
			if ((actual_row - next_row == 1) and (abs(actual_col - next_col) == 1) and (the_place_is_empty(board, next_row, next_col))):  # if its 1 can only move "up"
				return True
			else:
				#print ("Not a valid place to put the piece") used for debug
				pass
		elif (piece == 2):
			if ((next_row - actual_row == 1) and (abs(actual_col - next_col) == 1) and (the_place_is_empty(board, next_row, next_col))):  # if its 2 can only move "down"
				return True
			else:
				#print ("Not a valid place to put the piece") used for debug
				pass
		elif (piece == 11): # when i start dev the king piece come back here
			pass
		elif (piece == 22):
			pass
	else:
			#print ("Not a valid space") used for debug
			pass
	return False

def the_place_is_empty(board, next_row, next_col): # verify if its empty (0)
	if (board[next_row][next_col] == 0):
		return True
	else:
		return False


def can_make_a_capture(board, piece, enemy_piece): # verify if the player can make a captura
	for i in range(1, 9):
		for j in range(1, 9): # look all the board
			if (its_a_valid_space(i, j) and (board[i][j] == piece)): # look to all player pieces
				if piece == 1:
					if (there_is_capturable_enemies_nearby(board, enemy_piece, i, j) or there_is_capturable_enemies_nearby(board, 22, i, j)): # if there are enemies nearby
						#print ("can make a capture i , j:", i, j) used for debug
						return True
				if piece == 2:
					if (there_is_capturable_enemies_nearby(board, enemy_piece, i, j) or there_is_capturable_enemies_nearby(board, 11, i, j)): # if there are enemies nearby
						#print ("can make a capture i , j:", i, j) used for debug
						return True

		#for i in range(1, 9): # used for the king piece not ready yet
		#	for j in range(1, 9):
		#		if (its_a_valid_space(i, j) and ((board[i][j] == 11) or (board[i][j] == 22))): # look to all player pieces
		#			if board[i][j] == 11:	
	return False

def there_is_capturable_enemies_nearby(board, enemy_piece, actual_row, actual_col):
	for i in range(actual_row-1, actual_row+2): 
		for j in range (actual_col-1, actual_col+2): # "search in X" if there are enemies
			if ((its_a_valid_space(i, j) and board[i][j] == enemy_piece)): # if there is an enemy nearby # need to add the King piece here

				move_row = ((i - actual_row) * 2) + actual_row
				move_col = ((j - actual_col) * 2) + actual_col

				if(its_a_valid_space(move_row, move_col) and board[move_row][move_col] == 0): # look if its possible to jump (if its valid and empty)
					#print("the valid piece to capture is i, j:", i, j) used for debu
					return True
	return False

def make_a_capture(board, piece, enemy_piece, piece_row, piece_col, enemy_row, enemy_col):
	
		# before i used a input by writing in the terminal, the code is comentted
		# i know the identation is "strange" but i dont remember what was before
		#make_a_capture = False
		#while not make_a_capture:

			#piece_row, piece_col = [int(x) for x in input("Select the piece you want to use to capture with row and col (0-7):").split()]
			#print('row:', piece_row, 'col:', piece_col)

			#enemy_row, enemy_col = [int(x) for x in input("Select the enemy piece you want to capture with row and col (0-7):").split()]
			#print('enemy row:', enemy_row, 'enemy col:', enemy_col)

	if capture_is_valid(board, piece, enemy_piece, piece_row, piece_col, enemy_row, enemy_col):
		board[piece_row][piece_col] = 0 
		board[enemy_row][enemy_col] = 0 # destroy enemy piece
		move_row = ((enemy_row - piece_row) * 2) + piece_row
		move_col = ((enemy_col - piece_col) * 2) + piece_col
		board[move_row][move_col] = piece # move piece

		#make_a_capture = True

		# verify if the same piece can capture again
		if there_is_capturable_enemies_nearby(board, enemy_piece, move_row, move_col):
			ls = [move_row, move_col] # list of coordenates of the piece that captured, since only it can be moved (to capture) again
			return ls # python i love u, because i can return anything and test. I dont know if this is the most correct way of doing it however
		else:
			return True # the piece captured and CANT CAPTURE AGAIN IN THE SAME TURN 
	else:
		#print ("Not valid") used for debu
		return False # capture wasnt valid

def capture_is_valid(board, piece, enemy_piece, actual_row, actual_col, enemy_row, enemy_col):
	if (piece == 1 or piece == 2): # this check is not necessary, since i always pass 1 or 2 to show the PLAYER and not the piece
		if (its_a_valid_space(actual_row, actual_col) and its_a_valid_space(enemy_row, enemy_col)): # basic check
			if((board[actual_row][actual_col] == piece) and (board[enemy_row][enemy_col] == enemy_piece)): # second basic check
				if((abs(actual_row - enemy_row) == 1) and (abs(actual_col - enemy_col) == 1)): # checks if the 2 pieces are close
					move_row = ((enemy_row - actual_row) * 2) + actual_row
					move_col = ((enemy_col - actual_col) * 2) + actual_col
					if (board[move_row][move_col] == 0):
						return True # if the place the piece will jump after the capture is empty, its a valid capture
	return False


def draw_board(board, click_row, click_col):
	for i in range (10):
		for j in range (10):
			# drawing the squares
			if (i == 0 or i == 9 or j == 0 or j == 9): # borders 
				pygame.draw.rect(screen, GREY, (i*SQUARESIZE, j*SQUARESIZE, SQUARESIZE, SQUARESIZE)) # no J ele faz j* sqyaresize + squaresize
			elif (its_a_valid_space(i,j)): # valid spaces are BLACK
				pygame.draw.rect(screen, BLACK, (i*SQUARESIZE, j*SQUARESIZE, SQUARESIZE, SQUARESIZE)) # no J ele faz j* sqyaresize + squaresize
			else: # spaces that are not valid neither border are White
				pygame.draw.rect(screen, WHITE, (i*SQUARESIZE, j*SQUARESIZE, SQUARESIZE, SQUARESIZE)) # no J ele faz j* sqyaresize + squaresize
			

	for i in range (10):
		for j in range (10):
			#drawing the pieces / circles
			if (its_a_valid_space(i,j)):
				if (board[i][j] == 1): 
					pygame.draw.circle(screen, WHITE, (int(j*SQUARESIZE + SQUARESIZE / 2), int(i*SQUARESIZE + SQUARESIZE / 2)), RADIUS)
				elif (board[i][j] == 2):
					pygame.draw.circle(screen, RED, (int(j*SQUARESIZE + SQUARESIZE / 2), int(i*SQUARESIZE + SQUARESIZE / 2)), RADIUS)
				elif (board[i][j] == 11):
					pygame.draw.circle(screen, GREY, (int(j*SQUARESIZE + SQUARESIZE / 2), int(i*SQUARESIZE + SQUARESIZE / 2)), RADIUS)
				elif (board[i][j] == 22):
					pygame.draw.circle(screen, DARK_RED, (int(j*SQUARESIZE + SQUARESIZE / 2), int(i*SQUARESIZE + SQUARESIZE / 2)), RADIUS)

	# i draw this circle to know where was the last player click
	pygame.draw.circle(screen, YELLOW, (int(click_col*SQUARESIZE + SQUARESIZE / 2), int(click_row*SQUARESIZE + SQUARESIZE / 2)), RADIUS - 25)
	pygame.display.update()

# not used function, it didnt work. I made this one when started dev click instead input by keyboard
# def get_mouse_click(row, col):
# 	for event in pygame.event.get():
# 		if event.type == pygame.MOUSEBUTTONDOWN:
# 			#print(event.pos)
# 			posx = event.pos[0]
# 			col = int(math.floor(posx / SQUARESIZE))
# 			posy = event.pos[1]
# 			row = int(math.floor(posy / SQUARESIZE))

# 			#print("row:", row, "col:", col)
# 			list_of_pos = [row, col]
# 			return  list_of_pos
# 		else: 
# 			list_of_pos = [-1, 0]
# 			return list_of_pos

def is_game_over(points_player1, points_player2, board): # verify end of the game
	# each player has 12 pieces, so if he looses all his pieces, the other has 12 points
	if points_player1 == 12: 
		print("Player 1 achieves 12 points and Wins", points_player1)
		return True
	elif points_player2 == 12:
		print("Player 2 achieves 12 points and Wins!", points_player2)
		return True
	#elif player_cannot_play(board):
		#return True
	return False

def player_cannot_play(board):
	#for player 1
	if ((not can_make_a_capture(board, 1, 2)) and (not can_make_a_move(board, 1))):
		print("Player 2 Wins - Player 1 Cant do anything")
		return True
	elif ((not can_make_a_capture(board, 2, 1)) and (not can_make_a_move(board, 2))):
		print("Player 1 Wins - Player 2 Cant do anything")
		return True
	return False

def can_make_a_move(board, piece):

	# still need to dev the King piece 11 and 22

	# its not efichency, since it look the board 2 times do do the same thing, only for diferents pieces

	for i in range(1, 9):
		for j in range(1, 9): # look to all board
			if (its_a_valid_space(i, j) and (board[i][j] == piece)): # look to all player pieces
				if (there_is_zero_forward(board, i, j, piece)): # if there is a zero forward can move
					return True
	#print(piece, "cant move") used for debug 
	return False

def there_is_zero_forward(board, actual_row, actual_col, piece):
	#print("entrou aqui 2") used for debug
	if (piece == 1):
		i = actual_row - 1
	elif (piece == 2):
		i = actual_row + 1
		#print ("entrou aqui 3") used for debug
	for j in range (actual_col-1, actual_col+2):
		#print("board [i][j]:", board[i][j], i, j)
		if ((its_a_valid_space(i, j) and board[i][j] == 0)):
			#print ("entrou aqui 4") used for debug
			return True
	return False

def transform_king(board):
	for i in range (1, 9): # look in the edge 
		if (board[1][i] == 1):
			board[1][i] = 11
		if (board[8][i] == 2):
			board[8][i] = 22


# starts variables
board = create_board()
turn = 0
game_over = False 
points_player1 = 0
points_player2 = 0
cont_clicks = -1 # used this one to save 2 clicks at the same time. logic below. it starts at -1 so your first click is the click 0
avance_turn = False
row = row_2 = 0
col = col_2 = 0
was_capture_streak = False

# starts pygame variables
pygame.init()
SQUARESIZE = 80
width = 10 * SQUARESIZE
size = (width, width)
RADIUS = int(SQUARESIZE / 2 -  5)
screen = pygame.display.set_mode(size)

draw_board(board, 0, 0)
pygame.display.update()

while not game_over:
	# pygame.event.get() used to stop a bug 
	# all the commented prints below were used to debug

	for event in pygame.event.get(): # loop that is needeed to used the mouse to click and select
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			cont_clicks += 1
			
			if(its_even(cont_clicks) and not was_capture_streak): # save the even click in row and col
				#print(event.pos)
				#print ("first click")
				posx = event.pos[0]
				posy = event.pos[1]
				row = int(math.floor(posy / SQUARESIZE))
				col = int(math.floor(posx / SQUARESIZE))
				#print("row:", row, "col:", col)
				row_2 = col_2 = 0 # this solves a bug that the player couldnt choose the piece he wanted to capture, if there were more than one
								  # the because the "target" of it was the last used piece of the other player
			else:
				#print(event.pos)
				#print ("second click")
				posx = event.pos[0]
				posy = event.pos[1]
				row_2 = int(math.floor(posy / SQUARESIZE))
				col_2 = int(math.floor(posx / SQUARESIZE)) 
				#print("row:", row_2, "col:", col_2)

			#PLAYER 1 TURN
			if turn == 0:
				print("Player 1-White Turn")
				piece = 1 
				enemy_piece = 2	

				if not can_make_a_capture(board, piece, enemy_piece): #can just move the piece
					avance_turn =  move_piece(board, piece, row, col, row_2, col_2) # avance turn only when the player moved a piece successfully
				else: # has to make the capture
					#print("You can make a capture, and have to")
					avance_turn = make_a_capture(board, piece, enemy_piece, row, col, row_2, col_2) # avance turn only when the player captured a piece successfully
					#print ("avance_turn:", avance_turn)

					#if not isinstance (avance_turn, bool): # another if that can work
					if not (type(avance_turn) is bool): # if there was a capture streak
						#print("there was capture streak")
						was_capture_streak = True
						points_player1 += 1
						#print ("player1 point", points_player1)
						row = avance_turn[0] # this make the only piece that can be moved again to capture is the last used
						col = avance_turn[1]

					elif(avance_turn): # if the avance_turn in this case a bool, if its true the capture was done and the turn is over. if its false, the play wasnt valid
						points_player1 += 1
						#print ("player1 point", points_player1)
						was_capture_streak = False # its the end of the capture streak

			# PLAYER 2 TURN
			# same logic that player 1 has
			else:
				print("Player 2-Red Turn")
				piece = 2
				enemy_piece = 1	

				if not can_make_a_capture(board, piece, enemy_piece): #can just move the piece
					avance_turn =  move_piece(board, piece, row, col, row_2, col_2)
				else: # has to make the capture
					#print("You can make a capture, and have to")
					avance_turn = make_a_capture(board, piece, enemy_piece, row, col, row_2, col_2)
					#print ("avance_turn", avance_turn)

					#if not isinstance (avance_turn, bool):
					if not (type(avance_turn) is bool): #capture streak
						#print("there was capture streak")
						was_capture_streak = True
						points_player2 += 1
						#print ("player2 point", points_player2)
						row = avance_turn[0]
						col = avance_turn[1]


					elif(avance_turn):
						points_player2 += 1
						#print ("player2 point", points_player2)
						was_capture_streak = False

			print("Player 1 Points:", points_player1)
			print("Player 2 Points:", points_player2)
			game_over = is_game_over(points_player1, points_player2, board)
			transform_king(board) # verify if there is any pawn that can be a king

			print(board)
			if(its_even(cont_clicks)): # its used to print the yellow circle of the last click
				draw_board(board, row, col)
			else:
				draw_board(board, row_2, col_2)

			if ((type(avance_turn) is bool) and avance_turn): # makes turn goes 0 1 0
				turn += 1
				turn = turn % 2

			
pygame.quit()