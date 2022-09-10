#!/usr/bin/python3
import json
from sys import argv

users_and_pass = {
    "Gaspy" : 1234,
    "Cin" : 5984,
    "Niki" : 7756,
}

arg = argv[1]
arg2 = argv[2]

all__users = {}
all__pass = {}

for key, value in users_and_pass.items():
    if argv[1] == key:
        print('Error')
    elif argv[1] != key:
        users_and_pass[arg] = arg2
        print('Correct')
        print(users_and_pass)

"""for key, value in users_and_pass.items():
    if arg:
        all__users.append(key)
        print(all__users)
    else:
        print('El nombre {} ya existe')"""