#1.Напишите функцию, которая транспонирует двумерный массив.
def Trans(arr):
    m = len(arr[0])
    n = len(arr)
    transArr = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            transArr[j][i]=arr[i][j]
    return transArr

arr=[[1,2,3], [4,5,6]]
print(Trans(arr))

#2
def Sobaki(spisok):
    d={}
    for pet in spisok:
        if pet[2:] in d:
            d[pet[2:]].append(pet[0])
            d[pet[2:]].append(pet[1])
        else:
            d[pet[2:]]=list(pet[:2])
    return d

spisok = [('Тоша', 20, 'Дотторе', 'Няшка'), ('Тови', 15, 'Дотторе', 'Няшка'), ('Лили', 14, 'Панталоне', 'Няшка')]
print(Sobaki(spisok))

#3 Напишите функцию, которая принимает на вход строку, и выводит слово, которое встречается во фразе реже всего.
def RareWords(s):
    d={}
    s=sorted(s.lower().split())
    for word in s:
        for letter in word:
            if not letter.isalpha():
                word = word.replace(letter, '')
        if word in d:
            d[word]+=1 
        else:
            d[word]=1
    minimum=10000
    rareWord=''
    for key in d.keys():
        if d[key]<minimum:
            if len(key)==0: continue
            minimum=d[key]
            rareWord=key
    return rareWord
    
s='Дотторе!! няшка!!!!!'
print(RareWords(s))

#4 Напишите функцию, которая принимает на вход строку, содержащую разные буквы латинского алфавита и символы пунктуации
#и возвращает букву, которая встречается чаще всего.
def CommonLetter(s):
    d={}
    s=s.lower().split()
    for word in s:
        for letter in word:
            if not letter.isalpha():
                word = word.replace(letter, '')
        if word in d:
            d[word]+=1 
        else:
            d[word]=1
    max=0
    commonLet=''
    for key in d.keys():
        if d[key]>=max and (key<commonLet or len(commonLet)==0):
            if len(key)==0: continue
            max=d[key]
            commonLet=key
    return commonLet
    
s='а а а а , , , , , д д д д'
print(CommonLetter(s))

#5.Напишите функцию, которая принимает на вход строку и определяет, является ли она палиндромом. Использовать рекурсию. 
def Palindrom(s):
    s=s.replace(' ','')
    if len(s)>2:
        if s[0]==s[-1]:
            return Palindrom(s[1:-1])
        else: return False
    elif len(s)==2:
        return s[0]==s[1]
    else:
        return True
        
pal='п ип'
print(Palindrom(pal))

#6 Напишите функцию, которая принимает на вход массив чисел и сортирует его по частоте элементов.
def Frequency(arr):
    d={}
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    newArr=[]
    for i in range(len(d)):
        for key in d.keys():
            if d[key]==i:
                for j in range(i):
                    newArr.append(key)
    return newArr 
    
arrF=[1,2,1,2,3]
print(Frequency(arrF))

#7.Напишите функцию, которая принимает на вход строку, состоящую из слов и чисел, разделенных одним пробелом.
#Определить, имеется ли в передаваемой строке непрерывная последовательность из трех слов.
def Sequence(s):
    s=s.split()
    k=0
    for e in s:
        if k==3: break
        if e.isalpha():
            k+=1
        else:
            k=0 
    return k==3
    
dottore = 'дотторе дотторе 3 дотторе'
print(Sequence(dottore))

#8.Напишите функцию, которая принимает на вход строку и возвращает максимальную длину непрерывной
#последовательности одинаковых букв.
def MaxSequence(s):
    k=0 
    max=0
    letter=''
    for e in s:
        if e==letter:
            k+=1
            if k>max: max=k
        else:
            letter=e
            k=1
    return max
    
bukvi='dottorenyaaaaaaaadottore'
print(MaxSequence(bukvi))

#9.Напишите функцию, которая в качестве параметра принимает строку и вычисляет введенное там арифметическое выражение. 
#Пример входных данных: “2+2*2”, результат выполнения: 6
def Calculator(s):
    return eval(s)

piece='2+2*2'
print(Calculator(piece))

#10.Напишите функцию, которая в качестве параметра принимает список словарей
#(в качестве ключей – строки, в качестве значений – числа) и выполняет следующую процедуру:
#Если ключ есть в нескольких словарях, то в новый словарь добавить этот ключ, а в качестве значения
#использовать сумму всех значений. 
#Если ключ есть только в одном из словарей, то просто добавить его в новый словарь. Вернуть новый словарь
def FindKey(listik):
    d={}
    for e in listik:
        for  key in e.keys():
            if key in d:
                d[key]+=e[key]
            else:
                d[key]=e[key]
    return d
    
harbingers=[{'дотторе': 10, 'панталоне': 8, 'арлекино': 7,'капитано': 7},{'капитано': 5, 'дотторе': 10},{'панталоне': 10, 'сандроне': 9}]
print(FindKey(harbingers))
