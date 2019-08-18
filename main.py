import datetime
import countries
import os

def parametrized_log(pathlog):
    def log(old_function):
        def new_function(*args, **kwargs):
            nonlocal pathlog
            dt = datetime.datetime.now()
            filename = dt.strftime('%Y_%m_%d___%H_%M_%S')
            filename = f'{old_function.__name__}-{filename}.txt'
            pathlog = os.path.join(pathlog, filename)
            old_function(*args, **kwargs)
            for k, v in kwargs.items():
                output = v
            with open(pathlog, 'w', encoding="utf-8") as file:
                file.write('Дата и время вызова функции: {}\nНазвание функции: {}\nАргументы: {}\nВыходной результат: {}'.format(dt, old_function.__name__, args, output))
        return new_function
    return log

@parametrized_log('D:\Studies\Python\Advanced Python\Decorators\logs')
def country(input, pathfile):
    countries.countries_wiki(input, pathfile)


if __name__ == '__main__':
    country(countries.countries_url, pathfile='countries_wiki.txt')