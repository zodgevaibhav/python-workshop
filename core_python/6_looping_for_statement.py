def simulate_for_loop_posibilities():
    for a in range(1, 11):  # Over range
        print(a*2)

    fruits = ["apple", "banana", "cherry"]  # Over List
    for fruit in fruits:
        print(fruit)

    word = "Python"  # Over String
    for letter in word:
        print(letter)

    person = {"name": "Alice", "age": 30}  # Over Dictionary
    for key, value in person.items():
        print(f"{key}: {value}")

    coordinates = (3, 4)
    for coordinate in coordinates:  # Over Tuple
        print(coordinate)

    for i in range(3):  # Nested loops
        for j in range(2):
            print(f"({i}, {j})")


if __name__ == '__main__':
    simulate_for_loop_posibilities()
