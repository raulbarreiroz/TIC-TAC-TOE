# tic_tac_toe

import random

def draw_board(board):
  # This function prints out the board that it was passed

  # "board" is a list of 10 strings representing the board (ignore index 0)
  print(f"   |   |")
  print(f" {board[7]} | {board[8]} | {board[9]}")
  print(f"   |   |")
  print('-----------')
  print(f"   |   |")
  print(f" {board[4]} | {board[5]} | {board[6]}")
  print(f"   |   |")
  print('-----------')
  print(f"   |   |")
  print(f" {board[1]} | {board[2]} | {board[3]}")
  print(f"   |   |")

def input_player_letter():
  # Lets the player type wich letter they want to be
  # Returns a list with the player's letter as the first item, 
  #   and the computer's letter as the second
  letter = ''
  while not (letter == 'X' or letter == 'O'):
    print('Do you want to be X or O?')
    letter = input().upper()

  # the first element in the list is the player's letter, 
  #  the second is the computer0s letter  
  return ['X', 'O'] if letter == 'X' else ['O', 'X']

def who_goes_first():
  # Randomly choose the player who goes first
  return 'computer' if random.randint(0, 1) == 0 else 'player'

def play_again():
  # This function returns True if the player wants to play again,
  #  otherwise returns False
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')

def make_move(board, letter, move):
  board[move] = letter

def is_winner(board, letter):
  # Given a board and a plyer's letter, this function returns
  #  True if that player has won
  return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal

def get_board_copy(board):
  # Make a duplicate of the board list and return it the duplicate
  return [b for b in board]

def is_space_free(board, move):
  # Return true if the passed move is free on the passed board
  return board[move] == ' '

def get_player_move(board):
  # Let the player type in their move
  move = ' '
  while move not in '1 2 3 4 5 6 7 8 9'.split(' ') or not is_space_free(board, int(move)):
    print('What is your next move? (1-9)')
    move = input()
  return int(move)

def choose_random_move_from_list(board, moves_list):
  # Returns a valid move from the passed list on the passed board
  # Returns None if there is no valid move
  possible_moves = [move for move in moves_list if is_space_free(board, move)]

  return None if len(possible_moves) == 0 else random.choice(possible_moves)

def get_computer_move(board, computter_letter):
  # Given a board and the computer's letter, determine where to
  #  move and return that move
  player_letter = 'X' if computter_letter == 'O' else 'O'

  # Here is our algorithm for our Tic Tac Toe AI:
  # First, check if we can win in the next move
  for i in range(1, 10):
    copy = get_board_copy(board)
    if is_space_free(copy, i):
      make_move(copy, computter_letter, i)
      if is_winner(copy, computter_letter):
        return i
      
  # Check if the player could win on their next move, 
  #  and block them
  for i in range(1, 10):
    copy = get_board_copy(board)
    if is_space_free(copy, i):
      make_move(copy, player_letter, i)
      if is_winner(copy, player_letter):
        return i
      
  # Try yo take one of the corners, if they are free
  move = choose_random_move_from_list(board, [1, 3, 7, 9])
  if move != None:
    return move
  
  # Try to take the center, if it is free
  if is_space_free(board, 5):
    return 5
  
  # Move on one of the sides
  return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
  # ReturnTrue if every space on the board has been taken.
  # Otherwise return False
  for i in range(1, 10):
    if is_space_free(board, i):
      return False
  return True

print('Welcome to Tic Tac Toe!')

while True:
  #Reset the board
  the_board = [' '] * 10
  player_letter, computer_letter = input_player_letter()
  turn = who_goes_first()
  print(f"The {turn} will go first")
  game_is_playing = True

  while game_is_playing:
    if turn == 'player':
      # player's turn
      draw_board(the_board)
      move = get_player_move(the_board)
      make_move(the_board, player_letter, move)
      
      if is_winner(the_board, player_letter):
        draw_board(the_board)
        print('The player won the game')
        game_is_playing = False
      else:
        if is_board_full(the_board):
          draw_board(the_board)
          print("The game is a tie!")
          break
        else:
          turn = 'computer'
    else:
      # computer's turn
      move = get_computer_move(the_board, computer_letter)
      make_move(the_board, computer_letter, move)

      if is_winner(the_board, computer_letter):
        draw_board(the_board)
        print("The computer has beaten you! You Lose.")
        game_is_playing = False
      else:
        if is_board_full(the_board):
          draw_board(the_board)
          print('The game is a tie!')
          break
        else:
          turn = 'player'

  if not play_again():
    break  