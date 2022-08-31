import random

letters = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
numbers = list('1234567890')
symbols = list('!#$%&*()+')

print('Welcome to Password Generator!')
n_letter = int(input('How many letters would you like in your pwd? '))
n_number = int(input('How many numbers would you like in your pwd? '))
n_symbol = int(input('How many symbols would you like in your pwd? '))

pwd = []
pwd.extend(random.choices(letters, k=n_letter))
pwd.extend(random.choices(numbers, k=n_number))
pwd.extend(random.choices(symbols, k=n_symbol))

random.shuffle(pwd)

print('Your password is: ',''.join(pwd))

