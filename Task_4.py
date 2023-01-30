length = int(input('Длина шоколадки:'))
width = int(input('Ширина шоколадки:'))
slice = int(input('Кол-во долек:'))
if slice % length == 0 or slice % width == 0 and slice <= length * width:
    print('Yes')
else:
    print('No')