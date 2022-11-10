import json
from logging import exception

FILE = 'jsondb/users.json'
class RegistrMixin:
    # 'Миксин для регистрации юзера'
    def validate_password(self, password, password2):
        if len(password) < 8:
            raise ValueError('Пароль должен содержать больше или равно 8 символов!')
        elif password.isdigit() or password.isalpha():
            raise ValueError('Пароль должен содержать буквы и цифры!')
        elif password2 != password:
            raise ValueError('Пароли не совпадают!')
const = 

    def sign_up(self, name, password, password2):
        self.validate_password(password, password2)
        self.name = name
        with open(FILE, 'r') as file:
            try:
                data = json.load(file)
                id = data[-1]['id'] + 1
            except (IndexError, ValueError):
                id = 1
                data = []

        with open(FILE, 'w') as file:
            if data:
                is_name_used = any([x['name'] == name for x in data])
                if is_name_used:
                    json.dump(data, file)
                    raise ValueError('Такой юзернейм уже есть!')
            data.append({'id': id, 'name': name, 'password': password})
            json.dump(data, file)
            return {'status': 201, 'msg': 'Successfully registered!'}

class LoginMixin:
    # 'Миксин для логина'
    def sign_in(self, name, password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registred = any([x['name'] == name for x in data])
            if not is_registred:
                raise Exception('Нет такого пользователя!')

            user_data = list(filter(lambda x: x['name'] == name, data))[0]
            if user_data['password'] != password:
                raise ValueError('Неверный пароль!')

            return {'status': 200, 'msg': 'Successfully logged in!', 'user': user_data['name']}

class User(RegistrMixin, LoginMixin):
    pass


user = User()
# print(user.sign_up('z.azat00@gmail.com', 'aZaT2o0o', 'aZaT2o0o'))
print(user.sign_in('z.azat00@gmail.com', 'aZaT2o0o'))