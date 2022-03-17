import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = random.randint(0, len(names)-1)
choosen_person = names[random_name]
print(choosen_person + " is going to buy the meal today!")

