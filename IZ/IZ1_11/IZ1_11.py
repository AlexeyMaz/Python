def process(lines, inc_list, maxS, ind, j):
    sum_before = total(lines, ind, inc_list[j])
    sum_after = total(lines, inc_list[j], inc_list[j + 1] - 1)
    sum_both = total(lines, ind, inc_list[j + 1] - 1)
    _maxSum = max(sum_before, sum_after, sum_both, maxS)
    ind = inc_list[j] + 1

    if j == len(inc_list) - 2:
        sum_before = total(lines, ind, inc_list[len(inc_list) - 1])
        sum_after = total(lines, inc_list[len(inc_list) - 1], len(lines) - 1)
        sum_both = total(lines, ind, len(lines) - 1)
        _maxSum = max(sum_before, sum_after, sum_both, _maxSum)

    return _maxSum, ind


def total(_list, start, end):
    _total = 0

    for j in range(start, end + 1):
        if _list[start] < 0:
            start += 1
        elif _list[start] > 0:
            break

    for j in range(end, start, -1):
        if _list[end] < 0:
            end -= 1
        elif _list[end] > 0:
            break

    for j in range(start, end + 1):
        _total += _list[j]
    return _total


inp = open("11a.txt", "r")
strLines = inp.readlines()
inp.close()

readyLines = list(map(str.rstrip, strLines))
readyLines = list(map(int, readyLines))
n = readyLines[0]
readyLines.remove(readyLines[0])

incredible_nums = {}
for i in range(len(readyLines)):
    if readyLines[i] > 0 and readyLines[i] % 2 == 0:
        incredible_nums[i] = readyLines[i]
incredible_list = list(incredible_nums)

max_sum = 0
ind_first = 0
for i in range(len(incredible_list) - 1):
    max_sum, ind_first = process(readyLines, incredible_list, max_sum, ind_first, i)

print(f"\nМаксимальная сумма подпоследовательности для первого файла = {max_sum}")

inp = open("11b.txt", "r")
strLines = inp.readlines()
inp.close()

readyLines = list(map(str.rstrip, strLines))
readyLines = list(map(int, readyLines))
n = readyLines[0]
readyLines.remove(readyLines[0])

incredible_nums = {}
for i in range(len(readyLines)):
    if readyLines[i] > 0 and readyLines[i] % 2 == 0:
        incredible_nums[i] = readyLines[i]
incredible_list = list(incredible_nums)

max_sum = 0
ind_first = 0
for i in range(len(incredible_list) - 1):
    max_sum, ind_first = process(readyLines, incredible_list, max_sum, ind_first, i)

print(f"Максимальная сумма подпоследовательности для второго файла = {max_sum}")
