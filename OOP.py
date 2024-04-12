# class Car:
#     color='Gray'
#     def turn_on(self):
#         pass
#
#     def ride(sel):
#         pass
#
# car_obgect=Car()
#
# print(dir(Car))



# class Car:
#
#     #stasticheskie pola (peremennye klassa
#     default_colur='Gray'
#     default_weight =5000
#
#     def __init__(self , color , model):
#         #dinamicheskoe pole(peremenye objekta)
#         self.color= color
#         self.model = model
#
#     def turn_on(self):
#         pass
#     def info(self):
#         print(self.color, self.model)
# car_obj_1 = Car('blue','BMW')
# car_obj_2 = Car('red','BMW2')
# car_obj_1.turn_on()
# print(car_obj_1.color)
# print(car_obj_2.model)
# car_obj_1.info()
# car_obj_2.info()


# class Car:
#     def __init__(self, color,type,year):
#         self.color=color
#         self.type=type
#         self.year=year
#
#     def func_z(self):print("Автомобиль заведен")
#
#     def func_vk(self): print("Автомобиль заглушён")
#
#     def func_year(self): print("Год машины", self.year)
#
#     def func_type(self): print(self.type_car)
#
#     def func_color(self): print(self.color)
#
# year1= int(input("Ведите год машины"))
# type_car1= input("Ведите тип автомобиля")
# color1= input("Ведите цвет автомобиля")
# car= Car(year1, type_car1,color1)
#
#
# Car.func_year()

# class Human:
#     default_name=0
#     default_age=0
#     def __init__(self,name , age):
#         self.name=name
#         self.age=age
#         self.__money=0
#         self.__house=None
#
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money{self.__money}')
#         print(f'House:{self.__house}')
#
#     @staticmethod
#     def default_info():
#         print(f'Default Name:{Human.default_name}')
#         print(f'Default Age:{Human.default_age}')
#
