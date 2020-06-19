class people:
    def __init__(self, str,salary):
        self.user_name = str
        self.salary = salary
    def show_user_and_salary(self):
        print(f'пользователь: {self.user_name} имеет зарплату  в размере :{self.salary}')


if __name__ == '__main__':
    user = people('Макс',100031)

    user.show_user_and_salary()