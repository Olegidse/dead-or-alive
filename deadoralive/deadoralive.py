import random
import time
import sys

def printM(matr):
    for i in range(len(matr)):
      for j in range(len(matr[i])):
         print(matr[i][j], end = '    ')
         if j == len(matr[i])-1:
             print('\n')
#Случайное заполнение поля размером a*b
def initDesk(a,b): 
    Desk = [] 
    random.seed()
    for i in range(a):
        Desk.append([0] * b)
    for i in range(a):
        for j in range(b):
            Desk[i][j] = random.randint(0,1)
    return Desk

#a = 1 - ввод целого числа, a = 0 - ввод строки
def input1(errortext, prompt, a ):  
  try:
    if a == 1:
      return int(input(prompt))
    if a == 0:
      return input(prompt)
  except:
    print(errortext)
    time.sleep(5)
    sys.exit()
   
#Считает количество единиц вокруг одного элемента, проверяет каждый случай его возможного расположения на поле 
def count(matr, i, j):
    N = len(matr) - 1
    M = len(matr[0]) -1 
    sum = 0
    if i == 0 and not (j == M or j == 0):
        sum = matr[0][j-1] + matr[0][j+1] + matr[1][j-1] + matr[1][j] + matr[1][j+1] 
    elif i == N and not (j == 0 or j == M):
        sum = matr[N][j-1] + matr[N][j+1] + matr[N-1][j-1] + matr[N-1][j] + matr[N-1][j+1]
    elif j == 0 and not (i == 0 or i == N):
        sum = matr[i-1][0] + matr[i+1][0] + matr[i-1][1] + matr[i][1] + matr[i+1][1]
    elif j == M and not (i == 0 or i == N):
        sum = matr[i-1][M] + matr[i+1][M] + matr[i-1][M-1] + matr[i][M-1] + matr[i+1][M-1]
    elif i == 0 and j == 0:
        sum = matr[0][1] + matr[1][0] + matr[1][1]
    elif i == 0 and j == M:
        sum = matr[0][M-1] + matr[1][M-1] + matr[1][M]
    elif i == N and j == 0:
        sum = matr[N][1]+ matr[N-1][0]+ matr[N-1][1]
    elif i == N and j == M:
        sum = matr[N][M-1] + matr[N-1][M] + matr[N-1][M-1]
    else:
      sum = matr[i-1][j-1] + matr[i-1][j] + matr[i-1][j+1] + matr[i][j-1]+ matr[i][j+1] + matr[i+1][j-1] + matr[i+1][j] + matr[i+1][j+1] 
    return sum

#создаёт считает кол-во единиц вокруг каждого элемента, создаёт новое изменённое состояние и передаёт его в эту же функцию
def loop(N,M,Desk,counter):
    counter += 1
    print()
    NewDesk = []
    for i in range(N):
            NewDesk.append([0] * M)
    for i in range(N):
        for j in range(M):
            if Desk[i][j] == 1:
                if count(Desk,i,j) < 2 or count(Desk,i,j) > 3:
                    NewDesk[i][j] = 0
                else: NewDesk[i][j] = 1
            if Desk[i][j] == 0:
                 if count(Desk,i,j) == 3:
                    NewDesk[i][j] = 1
                 else: NewDesk[i][j] = 0
    print('Состояние ',counter,': ')
    print()
    printM(NewDesk)
    time.sleep(1)
    loop(N,M,NewDesk,counter)


print('Выберите способ получения стартового состояния:')
print('0 - случайное стартовое состояние')
print('1 - считывание из файла')
A = input1('Неверный ввод!','',1)
if A == 0: #случайное заполненение с вводом размеров поля
    N = input1('Неверный ввод!', 'Введите количество строк: ',1)
    M = input1('Неверный ввод!', 'Введите количество столбцов: ',1)
    Desk = initDesk(N,M)
    print('Состояние 1:')
    print()
    printM(Desk)
    time.sleep(1)
    loop(N,M,Desk,1)
if A == 1: #считывание стартового состояния из файла
   file = input1('Неверный ввод!','Введите имя файла: ',0)
   try:
     f = open(file, 'r')
   except:
     print('Неверное имя файла!')
     time.sleep(5)
     sys.exit
   N = 0
   M = len(f.readline())-1 #количество столбцов
   print(M)
   f.seek(0)
   
   for line in f: #Считаем кол-во строк
       N += 1
   Desk = []    #создаём поле размером N*M, заполненное нулями
   for i in range(N):
        Desk.append([0] * M)
   i = -1
   j = -1
   f.seek(0)
   for line in f: #Заполняем поле числами из файла
       i+=1
       for symb in line:
         j+=1
         if not symb == '\n':
            try:
               Desk[i][j] = int(symb)
            except:
                print('Неверно задано поле')
                time.sleep(5)
                sys.exit()
                 
         else: j = -1
         
   f.close()
   print('Состояние 1:')
   print()
   printM(Desk)
   time.sleep(1)
   loop(N,M,Desk,1)
