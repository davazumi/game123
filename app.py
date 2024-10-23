from random import randint

ROW_HEADER = '\n  a  b  c  d  e  f  g  h'
LETTERS = 'abcdefgh'
NUMBERS = '12345678'
ERROR_MESSAGE = 'Некорректный ввод!\nТолько буквы: abcdefgh\nИли цифры: 12345678\n'
FIRST_WIN = '\nИгрок 1 победил!'
SECOND_WIN = '\nИгрок 2 победил!'
FIRST_TURN = '\nИгрок 1 вводит координаты:'
SECOND_TURN = '\nИгрок 2 вводит координаты:'

# Шахматная доска в виде вложенного списка
board = [[], [], [], [], [], [], [], []]

# Заполняем доску фишками. 1 - есть фишка, 0 - нет
for el in board:
  for i in range(8):
      el.append(randint(0, 1))

# Функция отрисовки доски   
def draw_board():
  print(ROW_HEADER)
  for idx, i in enumerate(board):
    print((chr(ord('1') + idx)) + str(i))

# Обнуляем строку/столбец на основе введённого символа
def clear_line(input_char):
    if input_char in LETTERS:
        for i in board:
            i[LETTERS.index(input_char)] = 0
    elif input_char in NUMBERS:
        board[NUMBERS.index(input_char)] = [0] * 8
    draw_board()
  
# Проверка на пустоту доски
def board_is_empty():
    for board_line in board:
        if 1 in board_line:
            return False
    return True

print('Добро пожаловать в Супер ним!')
draw_board()

result_message = ''
while True:
    if not board_is_empty():
        input_char = input(FIRST_TURN)
        if input_char not in LETTERS and input_char not in NUMBERS:
            print(ERROR_MESSAGE)
            continue
        clear_line(input_char)
        result_message = FIRST_WIN
    if not board_is_empty():
        input_char = input(SECOND_TURN)
        if input_char not in LETTERS and input_char not in NUMBERS:
            print(ERROR_MESSAGE)
            continue
        clear_line(input_char)
        result_message = SECOND_WIN
    else:
        print(result_message)
        exit()
