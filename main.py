import os
import time
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        date_now = datetime.datetime.now()
        start = time.time()
        return_value = old_function(*args, **kwargs)
        end = time.time()
        benchmark = end-start
        print(f'[*] Время выполнения: {benchmark} секунд, дата и время {date_now}, имя функции {old_function.__name__} аргументы {args} {kwargs}, результат {return_value}')
        with open('main.log', 'a', encoding='utf-8') as record:
            record.write(f'[*] Время выполнения: {benchmark} секунд, дата и время {date_now}, имя функции {old_function.__name__}, аргументы {args} {kwargs}  результат {return_value}\n')
        return return_value

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'

@logger
def hw4_4():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    max_sales = 0
    big_channel = None
    for channel, sale in stats.items():
      if sale > max_sales:
         big_channel = channel
         max_sales = sale
    print(f'Больше всего продаж у {big_channel}')

if __name__ == '__main__':
    test_1()
    hw4_4()

