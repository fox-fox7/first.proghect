# def recurs(n):
#     if n!=0:
#         print(n)
#         return  n*recurs(n-1)
#     else:
#         return 1
# print(recurs(5))# !5=5*4*3*2*1=120

# def add(a,b):
#     return a+b
#
# sum =(1,2)
# print(sum)

# def func(x): return x
#
# a1=func
# a2=a1
# print(a2(10))
#abc = lambda a,b: a*b
#print(abc(2,4))иклы сдесь не работакют  просто функция как вматематике
# power= lambda x=1,y=2: x**y
# square= power
# print(square(5))


# def one (a):
#     def secund(b):
#         return  a*b
#     return secund
# print(one(2)(3))     #2 пойдет на one, а 3 пойдёт на secound

# def mul (a):
#     def helper(b):
#         return a*b
#     return helper
#
# three_mul =mul(3)
#
# print(three_mul(5))


# #Декоратор
# def first_test():
#     print("Test function")
#
# def second_test():
#     print("Test func 2")
#
# def simple_decor(fn):
#      def wrapper():
#          print("start")
#          fn()
#          print("stop")
#      return wrapper# он относится ко всеему decor не к wrapper
#
# first = simple_decor(first_test)
# second=simple_decor(second_test)
# first()
# second()


# def simple_decor(fn):
#     def wrapper():
#         print("start")
#         fn()
#         print("stop")
#
#     return wrapper
# @simple_decor
# def first_test():
#     print("Test function")
#
# @simple_decor
# def second_test():
#     print("Test func 2")
# first_test()
# second_test()
# def simple_decor(fn):
#     def wrapper (arg):
#         print("sturt function" + str(fn.__name__)+ "(), with param: "+ str(arg))
#         fn(arg)
#     return wrapper
# @simple_decor
# def first_test(num):
#     print(num*2)
#
# first_test(4)
#


# def anc(a):
#     return len(str(a))
# print(anc(1234567))

import random
def diapozon (a,b):
    list1=[random.randint(a,b) for i in range(10)]
    return list1
print(diapozon(10,20))

git
if __name__ == '__main__':
    add
