usrNum = input('Введите целое положительное число ')
intUsrNum = int(usrNum)
maxNum = intUsrNum % 10

while intUsrNum > 0:
    if intUsrNum % 10 > maxNum:
        maxNum = intUsrNum % 10
    intUsrNum = intUsrNum // 10
print(maxNum)
