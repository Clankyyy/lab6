from random import randint

MIN_NUM = 1
MAX_NUM = 100

def start_game():
    answer_num = randint(MIN_NUM, MAX_NUM)

    print("Введите число")
    while(True):
        user_input = input()
    
        if not user_input.isdigit():
            print("Введите корректное число")
            continue

        user_input = int(user_input)
        if(user_input < answer_num):
            print("Загаданное число больше, введите новое")
            continue
        elif(user_input > answer_num):
            print("Загаданное число меньше, введите новое")
            continue
        else:
            print("Вы угадали!, загаданное число:", answer_num)
            break
        



if __name__ == "__main__":
    start_game()

