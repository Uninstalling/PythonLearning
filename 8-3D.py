#
from random import randint


def rand():
    rand_list = []
    [rand_list.insert(idx, randint(0, 1)) for idx in range(3)]
    return rand_list


def rand_pro():
    if randint(0, 3):
        return 1
    else:
        return 0


print('{:-^49}'.format(''))
while True:
    # 各位数大小
    big_or_small_property = rand()
    big_or_small = []
    for i in range(3):
        if big_or_small_property[i]:
            big_or_small.append([5, 6, 7, 8, 9])
        else:
            big_or_small.append([0, 1, 2, 3, 4])
    # 各位数奇偶
    odd_or_even_property = rand()
    odd_or_even = []
    for i in range(3):
        if odd_or_even_property[i]:
            odd_or_even.append([1, 3, 5, 7, 9])
        else:
            odd_or_even.append([0, 2, 4, 6, 8])

    # 和大小、奇偶、分布
    sum_big_or_small_property = rand()
    # 和大小
    if sum_big_or_small_property:
        sum_big_or_small = list(range(13, 28))
    else:
        sum_big_or_small = list(range(14))
    # 和奇偶
    sum_odd_or_even_property = rand()
    if sum(odd_or_even_property) % 2:
        sum_odd_or_even = [i * 2 + 1 for i in range(14)]
    else:
        sum_odd_or_even = [i * 2 for i in range(14)]
    # 和分布
    sum_distribution_property = rand_pro()
    if sum_distribution_property:
        sum_distribution = list(range(8, 20))
    else:
        sum_distribution = list(range(0, 8)) + list(range(20, 28))

    # 阳卦选取，阴卦继续
    if sum([randint(0, 1) for i in range(3)]) % 2:
        [print(set(big_or_small[i]) & set(odd_or_even[i]), end=' ') for i in range(3)]
        print(set(sum_big_or_small) & set(sum_odd_or_even) & set(sum_distribution))
        print('{:-^49}'.format(''))
        break
    else:
        continue
