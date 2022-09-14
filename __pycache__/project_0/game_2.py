"""игра угадай число
компьютер сам загадывает и угадывает число"""

from tkinter import N
import numpy as np

number = np.random.randint(1,101)#загадываем число от 1 до 100

def random_predict():#задаем функцию
    
    count = 0           #создаем переменную в которой будем счиатать число попыток угадывания 
    num_max=101         #задаем максимальный диапазон для угадвания компьютером
    num_min=1           #задаем минимальный диапазон для угадвания компьютером

    while True:
        count+=1        #прибавляем 1 в каждой итерации к счетчику попыток
        predict_number=np.random.randint(num_min, num_max) # компьютер угадывает число в заданом диапазоне
        if predict_number<number: 
            num_min=predict_number     # если предполагаемое число меньше загаданного, то меняем минимальную границу угадывания 
        elif predict_number>number:
            num_max=predict_number     # если предполагаемое число больше загаданного, то меняем максимальную границу угадывания
        elif predict_number==number:   # если угадали, то прерываем цикл
            break
    return count # функция возвращает количество попыток угадывания
print(random_predict())
