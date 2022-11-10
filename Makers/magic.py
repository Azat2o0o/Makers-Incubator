asd = [1,2,3,4,5,6]
index_ = asd.index(asd[0])
inp = int(input('Введите индекс числа которое хотите поменять: '))
if inp in asd.index():
    inp2 = int(input('Введите новое значение: '))
    asd[index_] = asd[inp2]
print(asd)