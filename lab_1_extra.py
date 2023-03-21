#5 развернуть строку
stroka = str(input())
for i in range(len(stroka)):
    print(stroka[len(stroka)-i-1],end="")
print()

#8 распаковка массивов
def DoIt(arr):
    for x in arr:
        if type(x) is list:
            DoIt(x)
        else:
            print(x,end=' ')
    return

a=[1,[2,3],[4,[5,6]]]
DoIt(a)