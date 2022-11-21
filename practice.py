import os
import time
import datetime
# from datetime import date

def logger(old_function):
    def new_function(*args, **kwargs):
        date_now = datetime.datetime.now()
        start = time.time()
        return_value = old_function(*args, **kwargs)
        end = time.time()
        benchmark = end-start
        print(f'[*] Время выполнения: {benchmark} секунд, дата и время {date_now}, имя функции {old_function.__name__} аргументы {args} {kwargs}')
        # with open('main.log', 'a', encoding='utf-8') as record:
        #     record.write(f'[*] Время выполнения: {benchmark} секунд, дата и время {date_now}, имя функции {old_function.__name__}\n')
        return return_value

    return new_function

def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@logger
def hello_world():
    print('Hello world!')

hello_world()

@logger
def summator(a, b=0):
    return a + b

@logger
def div(a, b):
    return a / b

summator(3, 4)

div(6, 3)