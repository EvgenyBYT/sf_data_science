import numpy as np

number = np.random.randint(1,101)
print(f'компьютер загадал {number}')
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