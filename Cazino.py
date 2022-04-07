import random
import time

time.sleep(2)
print('Добро пожаловать в числовую угадайку!')
time.sleep(2)

limit = int(input('Для начала игры введите предел значений: '))
digit = random.randint(1, limit)
count_vars = 1
time.sleep(2)


def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= limit:
        return True
    return False


while True:
    num = input('Выберите ваше число: ')
    if is_valid(num) is False:
        print(f'А может быть все-таки введем целое число от 1 до {limit}?')
        # num = input('Выберите число: ')
        count_vars += 1
    elif is_valid(num) is True:
        num = int(num)
        if num > digit:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count_vars += 1
        elif num < digit:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count_vars += 1
        elif num == digit:
            print('Вы угадали, поздравляем!', f'Для того чтобы угадать вам понадобилось {count_vars} попыток!',
                  sep='\n')
            next_game = input('Если желаете сыграть еще раз, нажмите "д". Если хотите уйти, нажмите "н": ')
            if next_game.lower() == 'д':
                limit = int(input('Для начала игры введите предел значений: '))
                digit = random.randint(1, limit)
                count_vars = 1
                continue

            elif next_game.lower() == 'н':
                print('Приходите еще в наше казино. До свидания!')
                break
