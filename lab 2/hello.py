# Task 1
print('--------TASK 1--------')
print (37 / 10)
print (37 // 10)
print (37 % 10)
# Task 2
print('--------TASK 2--------')
print ('hello world')

#Task 3
print('--------TASK 3--------')
a = 3
print(type(a))
a = 3.5
print(type(a))
a = 'qwerty'
print(type(a))
a = True
print(type(a))
a = '123'
print(type(a))
#если попробовать сложить строку с числом -
#будет ошибка типа

#Task 4
print('--------TASK 4--------')
asd = int(5.7)
print(asd)
asdf = int(-5.7)
print(asdf)
asdfg = 3**39 - int(float(3 ** 39))
print(asdfg)
#получилось очень большое число (????)

#Task 5
print('--------TASK 5--------')
a = str(input('enter your name:'))
print('howdy,',a)

#task 6
print('--------TASK 6--------')
print('how many hours did the doctor drive to work?')
x = int(input())
print('how many minutes did the doctor walk from lunch to work?')
y = int(input())
asfsa = ((x * 60) + y)
print('minutes spent on the road:', (asfsa * 2))

#task 7
print('--------TASK 7--------')
a = False
b = True
c = False

z = (not (a or b) and c)
print(z)

#task 8
print('--------TASK 8--------')
print('enter the year')
year = int(input())
if ((year < 1900) or (year > 3000)):
    print('out of range')
elif (year % 400 == 0):
    print('happy birthday')        
else:
    print('nah, not that')


#task 9
print('--------TASK 9--------')
counter = 0
while True:
    if counter != 20:
        counter += 2
        print(counter)
    else:
        print('finish')
        break
    

#task 10
print('--------TASK 10--------')
x = int(input())
result = 0
while x:
    result += x
    x = int(input())
print('summ of entered values:',result)


#task 11
print('--------TASK 11--------')
p = int(input('colleagues at the FREE clinic: '))
c = int(input('colleagues at the clinic: '))
a = 2
while a % p != 0 or a % c != 0:
    a += 1
print('need a', a, 'slices of pizza')


#task 12
print('--------TASK 12--------')
a = 0
for a in range (1, 20 + 1):
    if (a % 2 == 0):
        print(a, end = '')
a += 1

#task 13
print('--------TASK 13--------')
a = int(input('enter the value: '))
b = int(input('enter the value: '))
c = int(input('enter the value: '))
d = int(input('enter the value: '))
print('', end='\t')
#first indent, empty
for j in range(c, d + 1):
#the first row of numbers
    print(j, end='\t')
print()
#the first row of numbers
for i in range(a, b + 1):
#for this series of numbers
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
#multiply two numbers
print()

#task 14
print('--------TASK 14--------')
n = int(input('enter matrix: '))
a = [[0] * n for i in range(n)]
count = 0
for i in range(n):  
    #filling first row
    count += 1
    a[0][i] = count
j = 0
i = n-1  
n -= 1 
#setting the size
while len(a)**2 != count: 
#exit condition
    for k in range(n): 
        #moving down
        j += 1
        count += 1
        a[j][i] = count
    for k in range(n): 
        #moving left
        i -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1): 
        #moving up
        j -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):
        #moving right
        i += 1
        count += 1
        a[j][i] = count
        n -= 2
        #transition
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

#task 15
print('--------TASK 15--------')
import time
from tkinter import messagebox

while True:
#a cycle for infinity
    time.sleep(10)
    #every ten seconds
    if __name__ == '__main__':
        messagebox.showinfo('Useful Python', 'turn around')
    else: print('uga')