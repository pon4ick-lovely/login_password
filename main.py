
class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    def __init__(self, username, password,repit_password):
        self.username = username
        if password == repit_password:
            self.password = password
        else:
            raise ValueError("Passwords do not match")

if __name__ == '__main__' :
    db = Database()
    user = User(input('Введите логин: '),input('Введите пароль: '),input('Повторите пароль: '))
    db.add_user(user.username, user.password)