from itertools import product

n1 = n2 = n3 = range(0, 10)
sum_pool = range(0, 28)

for sp in sum_pool:
    print(sp, ':', end=' ')
    for i in product(n1, n2, n3):
        if sum(i) == sp:
            print(i, end=' ')
    print('')
