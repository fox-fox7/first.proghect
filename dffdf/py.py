import pandas as pd
import matplotlib.pyplot as plt
import random
# data ={'Name':['Alice','Bob','Charlie'],
#        'Age' : [25,30,35] , 'town': ['Minsk',"zhodino","Borisov"]}
#
# df= pd.DataFrame(data)
#
# print(df)
#
# table={'день':[1,2,3,4,5], "Name":["Пылесос","телевизор", 'ноутбук', 'телевизор',' ноутбuk' ],
#        "kolic":[3,12,25,1,3],"cena":[1200,1300,2500,6000,5400],}

# ps=pd.DataFrame(table)
# print(ps)
# plt.title("График усталости за неделю")
# week= pd.Series({"понедельник":90, "вторник ":76, "среда ":51, "четверг ":39, "пятница":23, "суббота ":66, "воскресенье":100})
# plt.plot(week)
# plt.show()
#
# plt.title("Кто сколько съел")
# name= pd.Series({
#        "igor":50,
#        " anya":100,
#        "vasya":150
# })
# plt.pie(name, labels=name.index)
# plt.show()

#plt.title("оценки")
# marks= pd.Series({
#        "5":= 6,
#        "4":17,
#        "3"=14,
#        "2":=4,
#        "1": 1 })
# plt.bar(marks.index,height=marks)
# plt.show()

a=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),]
b=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),]
a,b
plt.plot(a,color="r",marker="o",label="data1")
plt.plot(b,color="b",marker="$F $", label="data2")
plt.legend()
plt.show()