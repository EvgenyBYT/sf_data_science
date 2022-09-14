import numpy as np
number = np.random.randint(1,101)
count=0
while True:
    count+=1
    predict_number=int(input('Угадай число от 1 до 100'))
    if predict_number<number: 
        print('загаданное число больше')
    elif predict_number>number:
        print('загаданное число меньше')
    else:
        print(f'Вы угадали за {count} попыток')
        break