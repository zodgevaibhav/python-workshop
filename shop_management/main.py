from user_management.UserManagement import UserManagement


def main():  # It's just simple function, in python there is no entry point function. Name of function can be anything

    can_i_keep_running_the_program = True
    # Python is "Dynamically Types Programming Language".
    # Which mean we don't need to provide data type while declaring variables.

    print("**** Welcome to Shop Management *****")  # Observe print functions. Refer readme for Console Input/Output
    print("\n")

    login_name: str = input("Enter login name: ")  # However it's possible to declare variable upfront like here.
    password = input("Enter password: ")  # Refer Readme file for more data types

    if not UserManagement.validate_user_and_password(login_name, password):  # Static method call # Observe if syntax
        print("!!!!!!!! Login failed. Closing the application")
        return

    while can_i_keep_running_the_program:   # Observe while syntax. Refer Readme for more information
        print("**** Welcome to Shop Management *****")
        print("\n")

        print("What would you like to do?")
        print("1. User Management")
        print("2. Product Management")
        print("5. Quit")

        option_selected_by_user = int(input())  # Observe input functions. Refer readme for Console Input/Output

        if option_selected_by_user == 1:
            UserManagement.user_management()
        #    elif option_selected_by_user == 2: # Implement Product Management similar to User Management
        # ProductManagement.product_management()
        elif option_selected_by_user == 5:  # Observe else if statement in python
            break


if __name__ == '__main__':  # In
    main()
