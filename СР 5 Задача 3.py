x=int(input("Минимальная сумма инвестиций - "))
maikl=int(input("Cколько долларов у Майкла - "))
ivan=int(input("Сколько долларов у Ивана - "))
if (maikl>=x) and (ivan>=x):
    print(2)
elif (maikl>=x) and (ivan<=x):
    print("Mike")
elif (maikl<=x) and (ivan>=x):
    print("Ivan")
elif (maikl<=x) and (ivan<=x) and ((maikl+ivan)>=x):
    print(1)
elif (maikl<=x) and (ivan<=x) and ((maikl+ivan)<=x):
    print(0)
