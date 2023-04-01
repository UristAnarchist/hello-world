import random
left_up_corner, up_midle, right_up_corner = '*', '-', '*'
left_midle, midle_midle, right_midle = '-', '+', '-'
left_down_corner, down_midle, right_down_corner = '*', '-', '*'

sign_dict = {11: left_up_corner, 12: up_midle, 13: right_up_corner,
             21: left_midle, 22: midle_midle, 23: right_midle,
             31: left_down_corner, 32: down_midle, 33: right_down_corner}
def board_print():
    print('0', '1', '2', '3', sep=' | ')
    print('-'*15)
    print(f'1 | {sign_dict[11]} | {sign_dict[12]} | {sign_dict[13]}')
    print('-'*15)
    print(f'2 | {sign_dict[21]} | {sign_dict[22]} | {sign_dict[23]}')
    print('-'*15)
    print(f'3 | {sign_dict[31]} | {sign_dict[32]} | {sign_dict[33]}')

def win_check():
    win_list = ((sign_dict[11], sign_dict[12], sign_dict[13]),
                (sign_dict[21], sign_dict[22], sign_dict[23]),
                (sign_dict[31], sign_dict[32], sign_dict[33]),
                (sign_dict[11], sign_dict[21], sign_dict[31]),
                (sign_dict[12], sign_dict[22], sign_dict[32]),
                (sign_dict[13], sign_dict[23], sign_dict[33]),
                (sign_dict[11], sign_dict[22], sign_dict[33]),
                (sign_dict[13], sign_dict[22], sign_dict[31]))
    for combination in win_list:
        if combination[0] == combination[1] == combination[2]:
            print('')
            return True

def turn(turn_sign):
    change = input('Введите координаты ')
    try:
        change = int(change)
    except:
        print('Следует ввести число')
    if str(change) in '3112132233' and sign_dict[int(change)] not in 'X0':
        sign_dict[change] = turn_sign
    elif str(change) in '3112132233' and sign_dict[int(change)] in 'X0':
        print('Эта ячейка уже занята')
        turn(turn_sign)
    else:
        print('Тут нет ячейки с такими координатами')
        turn(turn_sign)

print('Перед вами поле для игры в "Крестики-нолики"'
      '\nдля совершения хода вводите координаты ячейки'
      '\nдвузначным числом - сначала цифра по боковой строке, '
      '\nпотом по верхней строке (без пробела)')
print('Выберите между собой, кто какой знак будет ставить - кто крестик, кто нолик')

print('')
board_print()
print('')

#очередность
sign1 = 'X'
sign2 = "0"
turn_list = [sign1, sign2]
turn_sign1 = random.choice(turn_list)
turn_list.remove(turn_sign1)
turn_sign2 = turn_list[0]
new_turn_list = [turn_sign1, turn_sign2]

print(f'первым ход делает игрок, выбравший {turn_sign1}, второй игрок, соответственно,'
      f'\nставит {turn_sign2}')

counter = 0
winner = ''
turn_index = 0

while win_check() is not True:
    if counter != 9:
        turn(new_turn_list[turn_index])
        counter += 1
        board_print()
        if win_check() is True:
            winner = new_turn_list[turn_index]
            print(f'Победа за {winner}-ком')
            break
        if turn_index == 0:
            turn_index +=1
        else:
            turn_index -=1
    else:
        win_check() is True
        print('Ничья! Победила дружба)')
        break
print(f'Игра окончена')
