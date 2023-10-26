# Specify the file path
file_path = 'Users.csv'

# Open the file in read mode
file = open(file_path, 'r')  # r - read, w - write, a - append

# Read the entire file content
file_contents = file.read()

# Close the file
file.close()

# Now, you can work with the file content
print(file_contents)
