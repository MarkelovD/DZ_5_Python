# board = list(range(1,17))

# def print_board (board): # метод создания игрального поля
#     print("-"*21)
#     for i in range(4):
#         if i<=1:
#             print("|",board[0+i*4]," |",board[1+i*4]," |",board[2+i*4]," |",board[3+i*4]," |")
#         elif i==2:
#             print("| ",board[0+i*4],"|",board[1+i*4],"|",board[2+i*4],"|",board[3+i*4],"|")
#         else:
#             print("|",board[0+i*4],"|",board[1+i*4],"|",board[2+i*4],"|",board[3+i*4],"|")
#         print("-"*21)

# def input_item(player_item): # метод ввода данных
#     valid = False 
#     while not valid:
#         player_question = int(input("введите число где будет поставлен "+ player_item + "? "))
#         if player_question>=1 and player_question<=16: 
#             if (str(board[player_question-1])not in "XO"): # проверка на занятость 
#                 board[player_question-1] = player_item
#                 valid = True
#             else:
#                 print("клетка занята")
#         else:
#             print("число вышло за границы, введите число от 1 до 16")

# def win (board): # метод проверки на победу
#     win_result = ((0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15),(0,4,8,12),(1,5,9,13),(2,6,10,14),(3,7,11,15),(0,5,10,15),(3,6,9,12)) # условия победы
#     for item in win_result:
#         if board[item[0]] ==board[item[1]] ==board[item[2]] ==board[item[3]]:
#             return board[item[0]]
#     return False


# def main(board):
#     counter =0
#     win_result= False
#     while not win_result:
#         print_board(board)
#         if counter%2==0:
#             input_item("X")
#         else:
#             input_item("O")
#         counter += 1
#         if counter >5:
#             tmp = win(board)
#             if tmp:
#                 print(tmp, "выиграл!")
#                 win_result = True
#                 break
#         if counter == 16:
#             print ("Ничья!")
#             break
#     print_board(board)
# main(board)

# задача с конфетами 

candy = 221
limit = 28
user1_name = input("введите имя первого игрока: ")
user2_name = input("введите имя второго игрока: ")
while candy>0:
   valid_user_1 = False
   while not valid_user_1:
      user1_candy = int(input(f"{user1_name}_введите количесто вонфет которое возбмете: "))
      if user1_candy<=candy and 1<=user1_candy<=limit:
         candy=candy-user1_candy
         valid_user_1=True
      else:
         print("повторите")
      if candy == 0:
         print(user1_name + " WiN")
   print("осталось конфет "+str(candy))
   valid_user_2 = False
   while not valid_user_2:
      user2_candy = int(input(f"{user2_name}_введите количесто вонфет которое возбмете: "))
      if user2_candy<=candy and 1<=user2_candy<=limit:
         candy=candy-user2_candy
         valid_user_2=True
      else:
         print("повторите")
      if candy == 0:
         print(user2_name + " WiN")
   print("осталось конфет "+str(candy))