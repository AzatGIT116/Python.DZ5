# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line = input('Введите строку из слов: ')
words = line.split(' ')
fragment = 'абв'
new_words = []
for word in words:
    if fragment not in word:
        new_words.append(word)
print(' '.join(new_words))


print(' '.join(filter(lambda x: not 'абв' in x, 'Мы неабв очень любим Питон иабв !'.split())))



# 2.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


def player_number(t,move):
    if t ==0:
        if move ==-1:
            player = 1
        else:
            player = 2
        return player
    if t ==1:
        if move ==-1:
            player = 1
        else:
            player = "bot"
        return player

def enter_control(x):
        candy_for_player = 0
        while not( 0< candy_for_player < 29) or candy_for_player > x:
            candy_for_player = int(input(f"Игрок {player_number(t,move)}, укажите количество конфет, которые хотите взять (до 28): "))
            if candy_for_player > x:
                print(f"Количество должно быть до {x}")
            elif not( 0< candy_for_player < 29):
                print("Количество должно быть до 28")          
        return(candy_for_player)

def bot_control(x):
    b = 0
    if x < 29:
        b = x
    elif x < 57:
        b = x - 29
    while not( 0< b < 29):
        b = random.randint(1, 29)
    return b
t = int(input("Выберите тип игры 0 - человек / человек, 1 - человек/бот: "))

candy = 150
if t == 0:
    import random
    move = random.choice([-1,1])
    print(f"На столе {candy} конфет")
    print(f"Первый ход за игроком {player_number(t,move)}")
    while candy > 0:
        player_number(t,move)
        candy = candy - enter_control(candy)
        print(f"На столе осталось {candy} конфет")
        move = move*-1
    move = move*-1
    print(f"Победил игрок {player_number(t,move)}")

if t == 1:
    import random
    move = random.choice([-1,1])
    print(f"На столе {candy} конфет")
    print(f"Первый ход за игроком {player_number(t,move)}")
    while candy > 0:
        player_number(t,move)
        if player_number(t,move) == 1:
            candy = candy - enter_control(candy)
        else:
            bot = bot_control(candy)
            print(f"Bot забрал {bot} конфет")
            candy = candy - bot
        print(f"На столе осталось {candy} конфет")
        move = move*-1
    move = move*-1
    print(f"Победил игрок {player_number(t,move)}")



# 3. Создайте программу для игры в ""Крестики-нолики"".


print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def encode(s): 
    encoding = "" 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding 
if __name__ == '__main__':
    s = input('Введите повторяющиеся буквы: ')
    print(encode(s)) 
 