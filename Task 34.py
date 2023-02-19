# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

import os

os.system('CLS')
print ("Проверяем наличие ритма в стихах Винни-Пуха :)))")
poem = input("Введите его стихотворение (допускается вводить русские буквы, \nсимволы - в качестве разделителя слов во фразе и пробелы в качестве разделителя фраз=>")
dictionary = 'АЕЁИЙОУЫЭЮЯ'
poem = poem.split()
answer = True

def vowel(word):
    sum = 0
    for i in range(len(word)):
        if word[i].upper() in dictionary:
            sum +=1
    return sum

testsum = vowel(poem[0])

for i in range(1,len(poem)):
    if vowel(poem[i]) != testsum:
        answer = False
        break
if answer == True:
    print("ПАРАМ ПАМ-ПАМ")
else:
    print("ПАМ ПАРАМ")

    
    



















