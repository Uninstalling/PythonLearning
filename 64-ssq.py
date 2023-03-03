from random import randint


def rand():
    rand_list = []
    # [rand_list.insert(i, randint(0, 1)) for i in range(6)]
    [rand_list.append(randint(0, 1)) for _ in range(6)]
    return rand_list


while True:
    red_property = rand()
    yes_no = randint(0, 1)
    if yes_no:
        print(red_property)
        break
    else:
        continue
