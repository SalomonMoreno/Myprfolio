import random
names = input("Write down the names who can be choose to buy separated by \", \".\n")
names_splited = names.split(", ")
number_contestants = len(names_splited)
choosen_name = random.randint(0, number_contestants - 1)
wholl_pay = names_splited[choosen_name]
print(f"{wholl_pay} is going to buy the meal today!.")