"""Игра угадай  число меньше чем  за 20 попыток"""

import numpy as np
def random_predict(number:int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101) #предполагаемое число
    count = 0
    min = 1
    max = 100
    
    while True:
        count += 1
       
        if predict_number > number:
            max = predict_number - 1 
            predict_number = (max + min) // 2
        elif predict_number < number:
            min = predict_number + 1
            predict_number = (max + min) // 2
        else:    
            break
    return(count)
print(f'Количество попыток{random_predict()}')

def score_random(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
count_ls = []
np.random.seed(1)
random_array = np.random.randint(1, 101, size=(1000))
for number in random_array:
    count_ls.append(random_predict(number))

score = int(np.mean(count_ls)) # находим среднее количество попыток

print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')


#RUN
if __name__ == '__main__':
    score_random(random_predict)