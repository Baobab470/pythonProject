name = input("what is your name?")
age = input("what is your age?")
age = int(age)
print("hello {}, your age is {}".format(name, age))
if age >= 21:
    print("you can buy an alcoholic beverage")
else:
    print("you cannot buy an alcoholic beverage")