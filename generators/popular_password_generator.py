class Generator:
    def __init__(self):
        with open("generators/pop_psw.txt") as passwords_file:
            passwords = passwords_file.readlines()
        self.password_list = [password[:-1] for password in passwords]
        self.index = 0
    def next(self):
        if self.index < len(self.password_list):
            result = self.password_list[self.index]
            self.index += 1
        else:
            result = None
        return result