"""игра угадай число
компьютер сам загадывает и угадывает число"""

import numpy as np


def random_predict():
    number = np.random.randint(1,101)
    count = 0
    num_max=101
    num_min=1

    while True:
        count+=1
        predict_number=np.random.randint(num_min, num_max)
        if predict_number<number: 
            num_min=predict_number
        elif predict_number>number:
            num_max=predict_number
        elif predict_number==number:
            print(f'Ваш код угадал число за {count} попыток, загаданное число {predict_number}')
            break
    return count



def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

score_game(random_predict)

# RUN
if __name__ == '__main__':
    score_game(random_predict)