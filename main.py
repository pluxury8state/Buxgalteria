from application.people import people
from application.salry import salary
from datetime import datetime

if __name__ == '__main__':
    Polsovatel = people('Евгений', salary)
    Polsovatel.show_user_and_salary()
    print('функция была вызвана :', datetime.today())


