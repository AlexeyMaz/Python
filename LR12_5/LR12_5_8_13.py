def task_5():
    # Задание 5. Самое длинное слово в файле. В данном задании вы должны
    # написать программу, которая будет находить самое длинное слово в файле. В
    # качестве результата программа должна выводить на экран длину самого
    # длинного слова и все слова такой длины. Для простоты принимайте за
    # значимые буквы любые непробельные символы, включая цифры и знаки
    # препинания.

    fname = input("Введите название файла для чтения: ") + ".txt"

    is_file_opened = False
    while is_file_opened == False:
        try:
            inp = open(fname, "r")
            is_file_opened = True
        except FileNotFoundError:
            fname = input("Файл не найден. Введите название файла заново: ") + ".txt"

    words = ''
    strings = inp.readlines()
    for str in strings:
        if str != "\n":
            words += str.rstrip() + " "
    inp.close()

    words = words.split()
    max = len(words[0])
    for word in words:
        if len(word) > max:
            max = len(word)

    out = open("output.txt", "w")
    out.write(f"Длина самого длинного слова - {max}\n")
    for word in words:
        if len(word) == max:
            out.write(word + '\n')
    out.close()


def task_8():
    sum = 0
    str = input("Введите число: ")
    while str != "":
        try:
            sum += int(str)
            print(f"Текущая сумма = {sum}")
            str = input("Введите число: ")
        except ValueError:
            print("Вы ввели не число")
            str = input("Введите число: ")
    print("Ввод окончен")


def get_key(dict, value):
    for key, values in dict.items():
        if value in values:
            return key

def task_13():
    inp = open("elements.txt", "r")
    strings = inp.readlines()
    elems = {}

    for elem in strings:
        elem = elem.rstrip().split(',')
        elems[elem[0]] = {elem[1], elem[2]}

    string = input("Введите число протонов, обозначение или название хим. элемента: ")
    while string != "":
        try:
            if string.isdecimal():
                print(elems[string])
            elif not string.isdigit():
                if get_key(elems, string) != None:
                    print(get_key(elems, string))
                else:
                    raise KeyError
            string = input("Введите число протонов, обозначение или название хим. элемента: ")
        except KeyError:
            print("Такого элемента не существует")
            string = input("Введите число протонов, обозначение или название хим. элемента заново: ")
    print("Ввод окончен")


task_13()
