import numpy as np
import pygame
import sys
import math

# rules : if a player can make a capture, he has make the capture
# 		  if a player cannot make a move or loses all his pieces, he loses

# still need to implement the king mecanics and the "Lose because cant move feature"
# some bugs with lower rows (row 9)


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

def create_board():
	board = np.zeros((10,10))

	for i in range(0,9):
		board[0, i] = i
		board[i, 0] = i 
		board[9, i] = i 
		board[i, 9] = i 

	for row in range(1,4):
		for col in range(1,9):
			if (its_a_valid_space(row, col)): #if both are even numbers
				board[row][col] = 2 #2 are the black pieces

		for row in range(6,9):
			for col in range(1,9):
				if (its_a_valid_space(row, col)):
					board[row][col] = 1

	return board 


def its_a_valid_space(row,col): #verify if its a space that is used in the game
	if not (row == 0 or row == 9 or col == 0 or col == 9):	

		if ( its_even(row) and not its_even(col)) or (not its_even(row) and its_even(col)): 
			return True
	return False

def move_piece(board, piece, piece_row, piece_col, next_row, next_col):


	#did_a_valid_move = False
	#while not(did_a_valid_move):

		#piece_row, piece_col = [int(x) for x in input("Select the piece you want to move with row and col (0-7):").split()]
		#print('row:', piece_row, 'col:', piece_col)

		#next_row, next_col = [int(x) for x in input("Select the place you want to put the piece with row and col (0-7):").split()]
		#print('place row:', next_row, 'place col:', next_col)

		# print ("click on the piece you want to move")
		# #piece_row = 0
		# #piece_col = 0
		# list_of_pos = [-1, -1]
		# #list_of_pos.append(-1)
		# while not (list_of_pos[0] == -1):
		# 	list_of_pos = get_mouse_click() # waits mouse click
		# piece_row = list_of_pos[0]
		# piece_col = list_of_pos[1]
		# print( "piece_row:", piece_row, "piece_col:", piece_col)

		# #piece_row, piece_col = get_mouse_click()

		# print ("click on the space you want to move the piece")
		# list_of_pos = [-1, -1]
		# #list_of_pos.append(-1)
		# while not (list_of_pos[0] == -1):
		# 	list_of_pos = get_mouse_click() # waits mouse click
		
		# next_row = list_of_pos[0]
		# next_col = list_of_pos[1]
		# print( "piece_row", piece_row, "piece_col:", piece_col)

		# #next_row, next_col = get_mouse_click()

	if move_is_valid(board, piece_row, piece_col, next_row, next_col, piece):
		board[next_row][next_col] = piece
		board[piece_row][piece_col] = 0
		did_a_valid_move = True
		return True

	else:
		#print ("Not a Valid Move")
		return False

def move_is_valid(board, actual_row, actual_col, next_row, next_col, piece):
	if (its_a_valid_space(actual_row, actual_col) and its_a_valid_space(next_row, next_col) and (board[actual_row][actual_col] == piece)): # first basic check
		if (piece == 1): 
			if ((actual_row - next_row == 1) and (abs(actual_col - next_col) == 1) and (the_place_is_empty(board, next_row, next_col))):  #move foward
				return True
			else:
				#print ("Not a valid place to put the piece")
				pass
		elif (piece == 2):
			if ((next_row - actual_row == 1) and (abs(actual_col - next_col) == 1) and (the_place_is_empty(board, next_row, next_col))):  #move foward
				return True
			else:
				#print ("Not a valid place to put the piece")
				pass
		elif (piece == 11):
			pass
		elif (piece == 22):
			pass
	else:
			#print ("Not a valid space")
			pass
	return False

def the_place_is_empty(board, next_row, next_col):
	if (board[next_row][next_col] == 0):
		return True
	else:
		return False


def can_make_a_capture(board, piece, enemy_piece):

	for i in range(1, 9):
		for j in range(1, 9):
			if (its_a_valid_space(i, j) and (board[i][j] == piece)): # look to all player pieces
				if piece == 1:
					if (there_is_capturable_enemies_nearby(board, enemy_piece, i, j) or there_is_capturable_enemies_nearby(board, 22, i, j)): # if there are enemies nearby
						#print ("can make a capture i , j:", i, j)
						return True
				if piece == 2:
					if (there_is_capturable_enemies_nearby(board, enemy_piece, i, j) or there_is_capturable_enemies_nearby(board, 11, i, j)): # if there are enemies nearby
						#print ("can make a capture i , j:", i, j)
						return True

		#for i in range(1, 9):
		#	for j in range(1, 9):
		#		if (its_a_valid_space(i, j) and ((board[i][j] == 11) or (board[i][j] == 22))): # look to all player pieces
		#			if board[i][j] == 11:

	
			
	return False

def there_is_capturable_enemies_nearby(board, enemy_piece, actual_row, actual_col):
	for i in range(actual_row-1, actual_row+2): 
		for j in range (actual_col-1, actual_col+2):
			if ((its_a_valid_space(i, j) and board[i][j] == enemy_piece)):


				move_row = ((i - actual_row) * 2) + actual_row
				move_col = ((j - actual_col) * 2) + actual_col

				if(board[move_row][move_col] == 0):


					#print("the valid piece to capture is i, j:", i, j)
					return True
			
	return False

def make_a_capture(board, piece, enemy_piece, piece_row, piece_col, enemy_row, enemy_col):
	
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
		board[move_row][move_col] = piece

		#make_a_capture = True

		# verify if the same piece can capture again

		if there_is_capturable_enemies_nearby(board, enemy_piece, move_row, move_col):
			ls = [move_row, move_col]
			return ls # python i love u, this way i can control 
		else:
			return True
	else:
		#print ("Not valid")
		return False

def capture_is_valid(board, piece, enemy_piece, actual_row, actual_col, enemy_row, enemy_col):
	if (piece == 1 or piece == 2):
		if (its_a_valid_space(actual_row, actual_col) and its_a_valid_space(enemy_row, enemy_col)):
			if((board[actual_row][actual_col] == piece) and (board[enemy_row][enemy_col] == enemy_piece)):
				if((abs(actual_row - enemy_row) == 1) and (abs(actual_col - enemy_col) == 1)):
					move_row = ((enemy_row - actual_row) * 2) + actual_row
					move_col = ((enemy_col - actual_col) * 2) + actual_col
					if (board[move_row][move_col] == 0):
						return True
	return False


def draw_board(board, click_row, click_col):
	for i in range (10):
		for j in range (10):
			# drawing the squares
			if (i == 0 or i == 9 or j == 0 or j == 9):
				pygame.draw.rect(screen, GREY, (i*SQUARESIZE, j*SQUARESIZE, SQUARESIZE, SQUARESIZE)) # no J ele faz j* sqyaresize + squaresize
			elif (its_a_valid_space(i,j)):
				pygame.draw.rect(screen, BLACK, (i*SQUARESIZE, j*SQUARESIZE, SQUARESIZE, SQUARESIZE)) # no J ele faz j* sqyaresize + squaresize
			else:
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
	
	pygame.draw.circle(screen, YELLOW, (int(click_col*SQUARESIZE + SQUARESIZE / 2), int(click_row*SQUARESIZE + SQUARESIZE / 2)), RADIUS - 25)
	pygame.display.update()

def get_mouse_click(row, col):
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			#print(event.pos)
			posx = event.pos[0]
			col = int(math.floor(posx / SQUARESIZE))
			posy = event.pos[1]
			row = int(math.floor(posy / SQUARESIZE))

			#print("row:", row, "col:", col)
			list_of_pos = [row, col]
			return  list_of_pos
		else: 
			list_of_pos = [-1, 0]
			return list_of_pos

def is_game_over(points_player1, points_player2, board):
	if points_player1 == 12: 
		print("Player 1 achieves 12 points and Wins", points_player1)
		return True
	elif points_player2 == 12:
		print("Player 2 achieves 12 points and Wins!", points_player2)
		return True
	#elif player_cannot_move(board):
		#return True
	return False

def player_cannot_move(board):
	#for player 1
	if not can_make_a_capture(board, 1, 2) and not can_make_a_move(board, 1):
		print("Player 2 Wins - Player 1 Cant make a move")
		return True
	elif not can_make_a_capture(board, 2, 1) and not can_make_a_move(board, 2):
		print("Player 1 Wins - Player 2 Cant make a move")
		return True
	return False

def can_make_a_move(board, piece):
	for i in range(1, 9):
		for j in range(1, 9):
			if (its_a_valid_space(i, j) and (board[i][j] == piece)): # look to all player pieces
				if (there_is_zero(board, i, j)): 
					return True
	#print(piece, "cant move")
	return False

def there_is_zero(board, actual_row, actual_col):
	#print("entrou aqui 2")
	if (piece == 1):
		i = actual_row + 1
	elif (piece == 2):
		i = actual_row - 1
		#print ("entrou aqui 3")
	for j in range (actual_col-1, actual_col+2):
		#print("board [i][j]:", board[i][j], i, j)
		if ((its_a_valid_space(i, j) and board[i][j] == 0)):
			#print ("entrou aqui 4")
			return True
	return False

def transform_king(board):
	for i in range (1, 9):
		if (board[1][i] == 1):
			board[1][i] = 11
		if (board[8][i] == 2):
			board[8][i] = 22


board = create_board()

turn = 0

game_over = False 

pygame.init()
SQUARESIZE = 80
width = 10 * SQUARESIZE
size = (width, width)
RADIUS = int(SQUARESIZE / 2 -  5)
screen = pygame.display.set_mode(size)

draw_board(board, 0, 0)

pygame.display.update()

points_player1 = 0
points_player2 = 0

cont_clicks = -1

avance_turn = False

row = row_2 = 0
col = col_2 = 0

was_capture_streak = False

while not game_over:
	#pygame.event.get()

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			cont_clicks += 1
			

			if(its_even(cont_clicks) and not was_capture_streak):
				#print(event.pos)
				#print ("first click")
				posx = event.pos[0]
				col = int(math.floor(posx / SQUARESIZE))
				posy = event.pos[1]
				row = int(math.floor(posy / SQUARESIZE))
				#print("row:", row, "col:", col)
				row_2 = col_2 = 0
			else:
				#print(event.pos)
				#print ("second click")
				posx = event.pos[0]
				col_2 = int(math.floor(posx / SQUARESIZE))
				posy = event.pos[1]
				row_2 = int(math.floor(posy / SQUARESIZE))
				#print("row:", row_2, "col:", col_2)


			#ask for player 1 Input
			if turn == 0:
				print ("Player 1-White Turn")
				piece = 1
				enemy_piece = 2	

				if not can_make_a_capture(board, piece, enemy_piece): #can just move the piece
					avance_turn =  move_piece(board, piece, row, col, row_2, col_2)
				else: #has to make the capture
					#print("You can make a capture, and have to")
					avance_turn = make_a_capture(board, piece, enemy_piece, row, col, row_2, col_2)

					print ("avance_turn:", avance_turn)
					#if not isinstance (avance_turn, bool):
					if not (type(avance_turn) is bool): #capture streak
						print("there was capture streak")
						was_capture_streak = True
						points_player1 += 1
						print ("player1 point", points_player1)
						row = avance_turn[0]
						col = avance_turn[1]


					elif(avance_turn):
						points_player1 += 1
						print ("player1 point", points_player1)
						was_capture_streak = False

			#ask for player 2 Input
			else:
				print ("Player 2-Red Turn")
				piece = 2
				enemy_piece = 1	

				if not can_make_a_capture(board, piece, enemy_piece): #can just move the piece
					avance_turn =  move_piece(board, piece, row, col, row_2, col_2)
				else: #has to make the capture
					#print("You can make a capture, and have to")
					avance_turn = make_a_capture(board, piece, enemy_piece, row, col, row_2, col_2)

					print ("avance_turn", avance_turn)
					#if not isinstance (avance_turn, bool):
					if not (type(avance_turn) is bool): #capture streak
						print("there was capture streak")
						was_capture_streak = True
						points_player2 += 1
						print ("player2 point", points_player2)
						row = avance_turn[0]
						col = avance_turn[1]


					elif(avance_turn):
						was_capture_streak = False
						points_player2 += 1
						print ("player2 point", points_player2)

			game_over = is_game_over(points_player1, points_player2, board)

			print(board)
			if(its_even(cont_clicks)):
				draw_board(board, row, col)
			else:
				draw_board(board, row_2, col_2)

			if ((type(avance_turn) is bool) and avance_turn):	
				turn += 1
				turn = turn % 2

			transform_king(board)
pygame.quit()