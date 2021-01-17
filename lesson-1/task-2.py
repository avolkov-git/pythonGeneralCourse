time = input('Введите количество секунд')
intTime = int(time)

hh = intTime // (60*60)
hhM = hh * (60*60)
mm = (intTime - hhM) // 60
mmS = mm * 60
ss = intTime - (hhM + mmS)
nullValue = '00'

if hh == 0:
    hh = nullValue
elif hh < 10:
    hh = '0' + str(hh)

if mm == 0:
    mm = nullValue
elif mm < 10:
    mm = '0' + str(mm)

if ss == 0:
    ss = nullValue
elif ss < 10:
    ss = '0' + str(ss)

print('{}:{}:{}'.format(hh, mm, ss))
