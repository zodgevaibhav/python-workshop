my_list = [1, 2, 3, "apple", "banana"]

print(my_list[0])  # Index starting from 0

my_list.append(4)            # Append an
my_list.extend([5, 6, 7])    # Extend with multiple elements
my_list.remove("apple")      # Remove an element by value
print("Length of list is "+str(len(my_list)))

for li in my_list:
    print("For loop: "+str(li))

index = 0
while index < len(my_list):
    print("While loop : "+str(my_list[index]))
    index = index+1

