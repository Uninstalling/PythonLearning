#
from random import randint


def rand():
    rand_list = []
    [rand_list.append(randint(0, 1)) for _ in range(3)]
    return rand_list


print('{:-^49}'.format(''))

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

# 和大小(约各50%)
sum_big_or_small_property = randint(0, 1)
if sum_big_or_small_property:
    sum_big_or_small = list(range(13, 28))
else:
    sum_big_or_small = list(range(14))
# 和奇偶(约各50%)
sum_odd_or_even_property = rand()
if sum(odd_or_even_property) % 2:
    sum_odd_or_even = [i * 2 + 1 for i in range(14)]
else:
    sum_odd_or_even = [i * 2 for i in range(14)]
# 和正态分布(和值在[8,19]区间约占75%）
sum_distribution_property = randint(0, 3)
if sum_distribution_property:
    sum_distribution = list(range(8, 20))
else:
    sum_distribution = list(range(0, 8)) + list(range(20, 28))

# 显示结果
[print(set(big_or_small[i]) & set(odd_or_even[i]), end=' ') for i in range(3)]
print(set(sum_big_or_small) & set(sum_odd_or_even) & set(sum_distribution))

print('{:-^49}'.format(''))
