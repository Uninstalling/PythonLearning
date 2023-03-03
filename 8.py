from random import randint

print('=' * 49)
while True:
    gua = [randint(0, 1) for i in range(3)]
    if sum(gua) != 3 and sum(gua) != 0:
        if sum(gua) % 2:
            print('阳卦:', gua)
        else:
            print('阴卦:', gua)
    else:
        if sum(gua) == 3:
            print('阴卦:', gua)
        elif sum(gua) == 0:
            print('阳卦:', gua)
    print('-' * 49)

    ch = input('>>> Continue? 0.No 1.Yes: ')
    if ch == '0':
        print('=' * 49)
        break
    elif ch == '1':
        print('-' * 49)
        continue
    else:
        print('>>>Chosen Error...')
        print('=' * 49)
        break
