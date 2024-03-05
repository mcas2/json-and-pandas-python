import json

import pandas as pd


def loadJSON():
    try:
        with open("secure-users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


secure_users = loadJSON()
ids = []
passwords = []
for s_user in secure_users:
    ids.append(s_user['userId'])
    passwords.append(s_user['password'])

df = pd.DataFrame({'userId': ids, 'passwords': passwords})

df.to_excel('usuarios.xlsx')
