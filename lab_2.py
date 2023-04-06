#1 Написать функцию для вычисления n-ого элемента последовательности Фибоначчи (используя рекурсию).
def Fibonacchi(n, n1, n2):
    if n>0:
        n2=n1+n2
        n1=n2-n1
        if n2==0: n2=1
        return Fibonacchi(n-1, n1, n2)
    return n2
    
print (Fibonacchi(6,0,0))

#2 Из двух списков удалить все элементы, которые есть в обоих списках.
def Spiski(a1,a2):
    d = {}
    for e in a1:
        if not (e in d):
            d[e]=1
    i=0
    while i<len(a2):
        if a2[i] in d:
            d[a2[i]]=0
            a2.remove(a2[i])
            i=i-1
        i=i+1
    i=0
    while i<len(a1):
        if d[a1[i]]==0:
            a1.remove(a1[i])
            i=i-1
        i=i+1
    return a1,a2

print(Spiski([1,2,3,4,5,6], [4,5,6,7,8,9]))

#3 Извлечь из списка все элементы, которые встречаются не реже заданного числа раз.
def PrintFromArray(a,n):
    d = {}
    for e in a:
        if e in d:
            d[e]=d[e]+1
        else:
            d[e]=1
    i=0
    while i<len(a):
        if a[i] in d and d[a[i]]>=n:
            print (a[i], end=' ')
            d[a[i]]=-1
            i=i-1
        i=i+1
    return

PrintFromArray([1,2,3,3,3,3,3], 4)
print()

#4 Заменить в списке все вложенные списки суммой их элементов.
def SumOfArrays(a, l):
    newArray=[]
    s=0
    for e in a:
        if type(e) is list:
            e=SumOfArrays(e, l+1)
        if l==0:
            newArray.append(e)
        else:
            s=s+e
    if l==0:
        return newArray
    else:
        return s 

print(SumOfArrays([1,[2,3],[4,[5,6]]],0))

#5 Найти наибольшую возрастающую подпоследовательность в списке.
def Dottore(a):
    index1,index2,maxIndex1,maxIndex2 =0,1,0,0
    for i in range(len(a)):
        if len(a)==1:
            maxIndex2=1
            maxIndex1=0 
            break
        if i==0:
            i=i+1
        if a[i-1]<a[i]:
            index2=index2+1
        else:
            if maxIndex2-maxIndex1<index2-index1:
                maxIndex2=index2
                maxIndex1=index1
            index1, index2=i,i+1
    if maxIndex2-maxIndex1<index2-index1:
        maxIndex2=index2
        maxIndex1=index1
    return a[maxIndex1:maxIndex2]

print(Dottore([1,2,3,2,4,5,6,7]))

#6 Привести заданную строку к стилю “заборчиком”.
def Fence(s):
    newS=''
    for i in range(len(s)):
        if i%2==0:
            newS=newS+s[i].upper()
        else:
            newS=newS+s[i]
    return newS

print(Fence("я люблю дотторе"))

#7 На вход подается ширина и высота. По этим параметрам нарисовать ромб, используя на выбор один из символов: #, *, +
# я не буду переделывать пусть будет только для равнодиагональных
def Rhombus3000(height, width):
    A = [[' ']*width for i in range(height)]
    x=int(width/2)
    y=int(height/2)
    A[0][x], A[y][0], A[height-1][x], A[y][width-1]='+','+','+','+'
    if width>height: dots=round(((width-3)/2)/((height-3)/2))
    else: dots=round(((height-3)/2)/((width-3)/2))
    i,j,k=x+1,1,0
    while j<height-1:
        if j==y:
            if width>=height: i=i+2-width
            else: i=i+3-width
            j=j+1
            k=0
        if k<dots:
            A[j][i]='+'
            k=k+1 
            if width>=height: i=i+1
            else: j=j+1
        else:
            if width>=height: j=j+1
            else: i=i+1
            k=0
    i,j,k=x-1,1,0
    while j<height-1:
        if j==y:
            if width>=height: i=i-2+width
            else: i=i-3+width
            j=j+1
            k=0
        if k<dots:
            A[j][i]='+'
            k=k+1 
            if width>=height: i=i-1
            else: j=j+1
        else:
            if width>=height: j=j+1
            else: i=i-1
            k=0
    for row in A:
        for elem in row:
            print(elem, end = ' ')
        print()
    return
            

Rhombus3000(5,5)

#8 Заполнить квадратную матрицу так, чтобы все числа первого столбца и первой строки были равны 1,
#а каждое из оставшихся чисел равно сумме верхнего и левого соседей. Вывести на экран матрицу данного размера.
def Matrix(n):
    A = [[1]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==0 or j==0: continue
            A[i][j]=A[i-1][j]+A[i][j-1]
    for row in A:
        for elem in row:
            print(elem, end = ' ')
        print()
print()
Matrix(4)
print()

#9 Найти сумму всех чисел в строке. 
def Summa(s):
    number=''
    sum=0
    for i in range(len(s)):
        if s[i].isdigit():
            number+=s[i]
        else:
            if len(number)>0:
                sum+=int(number)
                number=''
    if len(number)>0:
        sum+=int(number)
    return sum
    
print(Summa('В этой 1 строке 4 всего 5 четыре числа 9'))

#10 То же самое, но без явной конвертации (не используя int())
def SummaWow(s):
    number=''
    sum=0
    for i in range(len(s)):
        if s[i].isdigit():
            number+=s[i]
        else:
            if len(number)>0:
                k=0
                while k<len(number):
                    sum=sum+(10**k)*(ord(number[len(number)-k-1])-48)
                    k=k+1
                number=''
    if len(number)>0:
        k=0
        while k<len(number):
            sum=sum+(10**k)*(ord(number[len(number)-k-1])-48)
            k=k+1
    return sum
    
print(SummaWow('В этой 1 строке 4 всего 5 четыре числа 9 100'))
