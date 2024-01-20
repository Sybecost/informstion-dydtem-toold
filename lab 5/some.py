#task 1
p = input('введите строку: ')
p = p.lower() #нижний регистр
p = p.replace(' ','') #лишние пробелы
if p == p[::-1]:
    print('да')
else:
    print('нет')

#task 2
m = []
s = ['end'] #cnjgth
while True:
    n = input().split()
    if n == s:
        break
    else:
        k = min(n, key=int)
        m.append(k)
for i in m:
    print(i)    

#task 3
m = [] #список
d = {} #словарь
n = str(input())
m.append([str(s.lower()) for s in n.split()])
li, lj = len(m), len(m[0])
for i in range(li):
    for j in range(lj):
        p = m[i][j]
        if p in d:
            d[p]+=1
        else:
            d[p] = 1
for key,value in d.items():
   print(key,value)
    
#task 4
import pymysql

connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='pass',
    database='my_db'
)

cur = connect.cursor()
year= int(input('введите год: '))
s = year
cur.execute('select first_name,last_name,date_of_birth from user where year(date_of_birth) = %s',s)
for rec in cur:
    print(rec[0],rec[1],rec[2])