def get_ticket_details():
    age = int(input("Enter your age: "))
    if age <= 5:
        print("No ticket")
    elif 5 < age <= 10:  # 5 < age <= 10:
        print("Half ticket")
    elif 10 < age <= 55:
        print("Full ticket")
    else:
        print("Half ticket")


if __name__ == '__main__':
    get_ticket_details()

