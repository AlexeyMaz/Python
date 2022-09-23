def task_8():
    latin_to_eng = {}
    for i in range(int(input("Введите кол-во английских слов в словаре: "))):
        eng_word, latin_translations = input().split(' - ')
        latin_translations_list = latin_translations.split(', ')
        for latin_word in latin_translations_list:
            latin_to_eng[latin_word] = set()
            latin_to_eng[latin_word].add(eng_word)

    print(len(latin_to_eng))
    for latin_word, eng_translations in sorted(latin_to_eng.items()):
        print(latin_word + ' - ' + ', '.join(eng_translations))

def task_9():
    # Задание 9. Контрольная по ударениям. Учительница задала Пете
    # домашнее задание — в заданном тексте расставить ударения в словах, после
    # чего поручила Васе проверить это домашнее задание. Вася очень плохо знаком
    # с данной темой, поэтому он нашел словарь, в котором указано, как ставятся
    # ударения в словах. К сожалению, в этом словаре присутствуют не все слова.
    # Вася решил, что в словах, которых нет в словаре, он будет считать, что Петя
    # поставил ударения правильно, если в этом слове Петей поставлено ровно одно
    # ударение.
    # Оказалось, что в некоторых словах ударение может быть поставлено
    # больше, чем одним способом. Вася решил, что в этом случае если то, как Петя
    # поставил ударение, соответствует одному из приведенных в словаре
    # вариантов, он будет засчитывать это как правильную расстановку ударения, а
    # если не соответствует, то как ошибку.
    # Вам дан словарь, которым пользовался Вася и домашнее задание,
    # сданное Петей. Ваша задача – определить количество ошибок, которое в этом
    # задании насчитает Вася.

    print("Введите кол-во слов в словаре:")
    n = int(input())

    print("Введите слова из словаря:")
    accents = {}
    for i in range(n):
        word = input()
        base_form = word.lower()
        if base_form not in accents:
            accents[base_form] = set()
        accents[base_form].add(word)

    print("Введите текст Пети:")
    errors = 0
    text = input().split()
    for word in text:
        base_form = word.lower()
        if (base_form in accents and word not in accents[base_form]
                or len([l for l in word if l.isupper()]) != 1):
            errors += 1
    print("Кол-во ошибок в Петином тексте:", errors, end='\n')


def IsAncestor(man, older_man, tree):
    if man == older_man:
        return True
    while man in tree:
        man = tree[man]
        if man == older_man:
            return True
    return False

def task_12():
    p_tree = dict()
    n = int(input())
    for i in range(n - 1):
        child, parent = input().split()
        p_tree[child] = parent

    for i in range(int(input())):
        first, second = input().split()
        if IsAncestor(second, first, p_tree):
            print(1, end=' ')
        elif IsAncestor(first, second, p_tree):
            print(2, end=' ')
        else:
            print(0, end=' ')


task_12()