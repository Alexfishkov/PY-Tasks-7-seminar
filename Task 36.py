# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Ввод: print_operation_table(lambda x, y: x * y)

import os

os.system('CLS')
print ("Распечатаем таблицу умножения в пределах указанных вами значений [M x N]")
num_rows = int(input("Введите кол-во строк M=> "))
num_columns = int(input("Введите кол-во столбцов N=> "))

# table =[]
# table = list(map(lambda num_rows, num_columns: num_rows*num_columns, table))
# print(table)

for i in range (1, num_rows+1):
    print()
    for j in range (1,num_columns+1):
        print(i*j, end="\t")


















