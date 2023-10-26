def simulate_while():
    count = 1

    while count <= 5:
        print(count)
        count += 1

    user_flag = True
    while user_flag:
        user_value = input("Do you want to stop the loop ? (Yes/No)")
        if user_value.lower() == "yes":
            user_flag = False


if __name__ == '__main__':
    simulate_while()

