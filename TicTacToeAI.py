#code under progress
list1 = [1 , [2 , 4 , 5]]
list2 = [2 , [1 , 3 , 5]]
list3 = [3 , [2 , 5 , 6]]
list4 = [4 , [1 , 5 , 7]]
list5 = [5 , [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]]
list6 = [6 , [3 , 5 , 9]]
list7 = [7 , [4 , 5 , 8]]
list8 = [8 , [5 , 7 , 9]]
list9 = [9 , [5 , 6 , 8]]
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
print("Tic Tac Toe Board:\n")
print("_|_|_")
print(f"{list1[0]}|{list2[0]}|{list3[0]}")
print("_|_|_")
print(f"{list4[0]}|{list5[0]}|{list6[0]}")
print("_|_|_")
print(f"{list7[0]}|{list8[0]}|{list9[0]}")
print("_|_|_")
print(" | |")
a = 0
b = 0
c = 0
d = 0
human_input = [a , b  , c , d]
a1 = 0
b1 = 0
c1 = 0
d1 = 0
bot_choice = 0
human_input_values = [a1 , b1 , c1 , d1]
human_xoro = str(input("Enter your choice. X or O:\n"))
if human_xoro.lower() == "x":
  human_input[0] = int(input("Enter position for X:\n"))
  human_input_values[0] = values[human_input[0]]
  if human_input[0] != 5:
    bot_choice = 5
    human_input[1] = int(input("Enter posiiton for X:\n"))
    human_input_values[1] = values[human_input[1]]
    if human_input[0] == list1[0]:
      if human_input[1] in list1[1]:
        pass
      else:
        pass
    elif human_input[0] == list2[0]:
      if human_input[1] in list2[1]:
        pass
      else:
        pass
    elif human_input[0] == list3[0]:
      pass
    elif human_input[0] == list4[0]:
      pass
    elif human_input[0] == list5[0]:
      pass
    elif human_input[0] == list6[0]:
      pass
    elif human_input[0] == list7[0]:
      pass
    elif human_input[0] == list8[0]:
      pass
    elif human_input[0] == list9[0]:
      pass
  else:
    bot_choice = 8
    human_input[1] = int(input("Enter posiiton for X:\n"))
    human_input_values[1] = values[human_input[1]]
else:
  pass
