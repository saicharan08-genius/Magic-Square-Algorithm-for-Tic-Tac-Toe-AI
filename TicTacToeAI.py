human_input = [0 , 0 , 0 , 0]
human_input_values = [0 , 0 , 0 , 0]
human_input1 = [0 , 0 , 0 , 0 , 0]
human_input1_values = [0 , 0 , 0 , 0 , 0]
values = {
  1 : 2,
  2 : 7,
  3 : 6,
  4 : 9,
  5 : 5,
  6 : 1,
  7 : 4,
  8 : 3,
  9 : 8
}
values1 = {
  2 : 1,
  7 : 2,
  6 : 3,
  9 : 4,
  5 : 5,
  1 : 6,
  4 : 7,
  3 : 8,
  8 : 9
}
print("Tic Tac Toe Board:\n")
def printboard(game_board):
  print(str(game_board[0])+'|'+str(game_board[1])+'|'+str(game_board[2]))
  print(str(game_board[3])+'|'+str(game_board[4])+'|'+str(game_board[5]))
  print(str(game_board[6])+'|'+str(game_board[7])+'|'+str(game_board[8]))
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
printboard(board)
print("(Each number denote the position of the shell)\n")
board_values = [2 , 7 , 6 , 9 , 5 , 1 , 4 , 3 , 8]
a = 0
b = 0
def board_values(a):
  board_value = int(values[a])
  return board_value
def board(b):
  board_value1 = int(values1[b])
  return board_value1
bot_choice = 0
human_xoro = str(input("Hey! Do you choose X or O?:\n"))
if human_xoro.lower() == "x":
  human_input[0] = int(input("Enter Position for X:\n"))
  if human_input[0] != 5:
    bot_choice = 5
  else:
    bot_choice = 9 
    
else:
  pass
