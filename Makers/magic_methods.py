import json

class Users:
    def sign_up(self):
        self.nickname = input('Введите ваше имя: ')
        self.age = int(input('Введите ваш возраст: '))
        self.universe = input('Введите ваш университет: ')
        self.__name = input('Введите логин: ')
        self.__password = input('Введите пароль: ')
        check_pass = input('Повторите пароль: ')
        if check_pass == self.__password:
            print(f'Добро пожаловать на наш сайт, {self.nickname}')
        else:
            print('Пароли не совпадают!')

    def save(self):
        users_info = {
            'nickname': self.nickname,
            'age': self.age,
            'universe': self.universe,
            'name': self.__name,
            'password': self.__password
        }
        with open('users.json', 'a') as sign_up_info:
            result = json.dumps(users_info)
            sign_up_info.write(result + '\n')
            print('Вы успешно зарегистрировались на наш сайт!')

    def sign_in(self):
        name = input('Введите логин: ')
        password = input('Введите пароль: ')
        with open('users.json', 'r') as file:
            sign_check = file.load()
            if name in sign_check and password in sign_check:
                print(f'Здравствуйте, {self.__nickname}. Рад вас видеть!')

user = Users()
user.sign_up()
user.save()
# user.sign_in()
    
            