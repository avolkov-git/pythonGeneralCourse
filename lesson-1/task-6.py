countA = int(input('Введите сколько километров спортсмен пробежал в первый день: '))
countB = int(input('Укажите минимальное значение километража: '))
days = 1;

while True:
    countA+=countA*0.1
    days+=1
    if countA > countB:
        break

print('На {} день результат будет больше {} км.'.format(days, countB))
