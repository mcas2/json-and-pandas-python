# 'ID Biblioteca 	ID Libro 	Título 	Editorial 	Año de publicación 	ID Usuario 	Nombre completo''
import json

import pandas as pd


def loadJSON():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

libraryId = []
bookId = []
bookTitle = []
bookEditorial = []
bookPublication = []
userId = []
userName = []

usuarios = loadJSON()
for usuario in usuarios:
    for book in usuario['books']:
        libraryId.append(book['libraryId'],)
        bookId.append(book['bookId'],)
        bookTitle.append(book['bookTitle'],)
        bookEditorial.append(book['bookEditorial'],)
        bookPublication.append(book['bookPublication'],)
        userId.append(usuario['userId'],)
        userName.append(usuario['userName'] + " " + usuario['userSurname'])


df = pd.DataFrame({
    "libraryId" : libraryId,
    "bookId" : bookId,
    "bookTitle" : bookTitle,
    "bookEditorial" : bookEditorial,
    "bookPublication" : bookPublication,
    "userId" : userId,
    "userName" : userName
})

print(df)
df = df.sort_values(by="libraryId")
print(df)


df.to_excel('libraries-and-books.xlsx')