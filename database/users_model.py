
class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.login_status = False


    def check_login_status(self):
        return self.login_status

    def __str__(self):
        return f"User{self.user_id, self.name}"
