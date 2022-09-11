# Задание 3 Большие буквы. Напишите функцию capitalize(), которая
# принимает слово из маленьких латинских букв и возвращает его же, меняя
# первую букву на большую.

def capitalize(string):
    tmp = string.split()
    res = ""
    for i in range(len(tmp)):
        res += tmp[i][0].upper() + tmp[i][1:] + ' '
    return res


print(capitalize(input()))