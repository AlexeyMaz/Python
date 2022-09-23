def task_1():
    # Задание 1. Количество различных чисел. Дан список чисел. Определите, сколько в нем встречается различных чисел.
    print(len(set([input() for i in range(int(input("Введите кол-во элементов: ")))])))


def print_set_info(set_tmp):
    print(len(set_tmp))
    print(sorted(set_tmp))


def task_5():
    # Задание 5. Кубики. Аня и Боря любят играть в разноцветные кубики,
    # причем у каждого из них свой набор и в каждом наборе все кубики различны
    # по цвету. Однажды дети заинтересовались, сколько существуют цветов таких,
    # что кубики каждого цвета присутствуют в обоих наборах. Для этого они
    # занумеровали все цвета случайными числами от 0 до 10^8 На этом их
    # энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.

    # В первой строке входных данных записаны числа N и M – число кубиков
    # у Ани и Бори. В следующих N строках заданы номера цветов кубиков Ани. В
    # последних M строках номера цветов Бори.
    # Найдите три множества: номера цветов кубиков, которые есть в обоих
    # наборах; номера цветов кубиков, которые есть только у Ани и номера цветов
    # кубиков, которые есть только у Бори. Для каждого из множеств выведите
    # сначала количество элементов в нем, а затем сами элементы, отсортированные
    # по возрастанию.
    print("Введите N и M:")
    n, m = [int(i) for i in input().split()]

    print("Введите номера цветов кубиков Ани:")
    a_set = set([int(input()) for i in range(n)])
    print("Введите номера цветов кубиков Бори:")
    b_set = set([int(input()) for i in range(m)])

    print("")
    print_set_info(a_set.intersection(b_set))
    print_set_info(a_set.difference(b_set))
    print_set_info(b_set.difference(a_set))


def task_6():
    # Задание 6. Количество слов в тексте.Дан текст: в первой строке записано
    # число строк, далее идут сами строки.Определите, сколько различных слов
    # содержится в этом тексте.
    n = int(input("Введите кол-во строк: "))
    s = ""
    for i in range(n):
        s += input() + " "
    print(f"\n{len(set(s.split()))}")


task_6()