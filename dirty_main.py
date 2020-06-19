from application import *

#вот что вышло, но тут можно использовать alt+enter , чтобы импортировать нужные объекты


if __name__ == '__main__':
    Polsovatel = people('Евгений', salary)
    Polsovatel.show_user_and_salary()
    print('функция была вызвана :', datetime.today())

