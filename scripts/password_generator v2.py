import requests
def clearning(list_of_data):
    for i in range(0, len(list_of_data)):
        if '@' in list_of_data[i]:
            list_of_data[i] = list_of_data[i][:list_of_data[i].find('@')]
    return list_of_data
def generator_psw(list_of_data):
    length = 0
    state = 0
    base = len(list_of_data)
    while True:
        password = ''
        temp_state = state
        while temp_state > 0:
            ceil = temp_state // base
            rest = temp_state % base
            password = list_of_data[rest] + password
            temp_state = ceil
        password = list_of_data[0] * (length - len(password)) + password
        print(state, password)
        state += 1
        if password == list_of_data[-1] * length:
            length += 1
            state = 0
        if len(password) >= 20:
            break
artem = ['rodinart@gmail.com', 'artem', 'rodin', '25031998']
generator_psw(clearning(artem))
