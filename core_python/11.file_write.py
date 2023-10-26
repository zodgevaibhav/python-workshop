
user_name = input("Enter User Name : ")
password = input("Enter Password : ")

file_path = 'Users.csv'

# Open the file in write mode ('w')
with open(file_path, mode='a', newline='') as file:
    # r - read, w - write, a - append
    file.write(user_name+","+password+"\n")

print("Data has been written to the text file.")
