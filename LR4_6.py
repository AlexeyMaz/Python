#Задание 6. Сумма кубов. По данному натуральному n вычислите сумму 1^3 + 2^3 + 3^3+ ... + n^3.

n = int(input("Введите n: "))
summa = 0

for i in range(1, n + 1):
    summa += i ** 3
print(summa)