def welcome():
    name = input("Enter your name : ")
    age = int(input("Enter your age: "))
    print(type(age))
    print("Happy "+str(age)+"th birthday Mr.", name)


if __name__ == '__main__':
    welcome()
