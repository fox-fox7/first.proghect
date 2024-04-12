# a=input("ВВедите текст :")
# b=a.lower()
# na=0
# ns=0
# for i in b :
#     if i in "aeiouy":
#         na+=1
#     elif i in "bcdfghjklmnpqrstvzwxz":
#         ns+=1
# print("количество глассных :",na,"количество согласных:",ns )

# print("Введите 3 числа :")
# n1=int(input("Введите число :"))
# n2=int(input("Введите число :"))
# n3=int(input("Введите число :"))
# if n1<n2<n3 or n3<n2<n1:
#      print("srednee :", n2)
# elif n2<n1<n3 or n3<n1<n2:
#      print("srednee :", n1)
# elif n2==n1==n3:
#      print('odinakovye')
# else:
#      print('srednee ',n3)

# with open ('task_1.txt') as f:
#     s= f.read()
#     print(s)
# s =s.replace('_','')
# a =s.split()
# print(a)
# s=0
# for i in a:
#     if i.isdigit():
#         i=int(i)
#         s+=1
# print(s)

# with open ('task_1.txt') as f:
#     s= f.readlines()
# print(s)
# a=[]
# b=[]
#
# for i in  s:
#     i=i.replace('\n','')
#     if i.isalpha():
#         a.append(i)
#     elif  i.isdigit():
#         b.append(int(i))
# print(b,a)
# b.sort()
# a.sort(key=len)
# mas =a+b
# print(mas)]
# list1=[1,2,3,4,5,6,7,8,9]
# def sum():
#     summa=0
#     for i in list1:
#         summa+=i
#     print(summa)
#
# sum()
# def is_year_leap(year):
#     return year %4==0 and year %100!=0 or year %400==0
#
# print(is_year_leap(int(input("Веедите год:"))))
#
# def season(num):
#     if num ==12 or 1 <=num<=2:
#         print("winter")
#     elif 3<=num<=5:
#         print("spring")
#     elif 6<=num<=8:
#         print("summer")
#     elif 9<=num<=11:
#         print("autmn")
#     else:
#         print("веден неправильный номер месяца")
# n=int(input("Ведите номер месяца(1-12):"))
# season(n)
