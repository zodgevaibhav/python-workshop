# Python main function
In python there is no main function as other languages. 
But it has ability to determine the current script/file being directly run as main (python3 hello.py), if so `__name__` special variable value get set to `__main__`

#### The `if __name__ == '__main__':` Statement

In Python, the `if __name__ == '__main__':` statement is often used in scripts to control the execution of code. It allows you to determine whether a Python script is being run as the main program or if it's being imported as a module into another script.

Here's how it works:

- When a Python script is executed, the Python interpreter assigns a special variable called `__name__` to the script.
- If the script is the main program being executed directly, `__name__` is set to `'__main__'`.
- If the script is imported as a module into another script, `__name__` is set to the name of the module.

#### Using `if __name__ == '__main__':`

The `if __name__ == '__main__':` statement is used to define a block of code that should only run when the script is the main program, not when it's imported as a module. This is commonly used for script entry points.

Here's an example:

```python
def main():
    # Your main code goes here

if __name__ == '__main__':
    main()
```

# Python Data Types

| Data Type                                                                                                                                                      | Description                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Numeric Types:                                                                                                                                                 |                                                                                     |
| `int`                                                                                                                                                          | Integer type, e.g., 42, -10, 0.                                                     |
| `float`                                                                                                                                                        | Floating-point type, e.g., 3.14, 2.0, -0.5.                                         |
| `complex`                                                                                                                                                      | Complex number type, e.g., 3+4j, 1-2j.                                              |
| Sequence Types:                                                                                                                                                |                                                                                     |
| `str`                                                                                                                                                          | String type, e.g., "Hello, World!", 'Python'.                                       |
| `list`                                                                                                                                                         | List type, e.g., [1, 2, 3], ['apple', 'banana', 'cherry'].                          |
| `tuple`                                                                                                                                                        | Tuple type, e.g., (1, 2, 3), ('a', 'b', 'c').                                       |
| Mapping Type:                                                                                                                                                  |                                                                                     |
| `dict`                                                                                                                                                         | Dictionary type, e.g., {'name': 'Alice', 'age': 30}, {'key1': 42, 'key2': 'value'}. |
| Set Types:                                                                                                                                                     |                                                                                     |
| `set`                                                                                                                                                          | Set type, e.g., {1, 2, 3}, {'apple', 'banana', 'cherry'}.                           |
| `frozenset`                                                                                                                                                    | Immutable set type, e.g., `frozenset([1, 2, 3])`.                                   |
| Boolean Type:                                                                                                                                                  |                                                                                     |
| `bool`                                                                                                                                                         | Boolean type, either `True` or `False`.                                             |
| Binary Types:                                                                                                                                                  |                                                                                     |
| `bytes`                                                                                                                                                        | Immutable sequence of bytes, e.g., `b'Hello'`, `b'\x41\x42\x43'`.                   |
| `bytearray`                                                                                                                                                    | Mutable sequence of bytes, e.g., `bytearray(b'Python')`.                            |
| None Type:                                                                                                                                                     |                                                                                     |
| `None`                                                                                                                                                         | A special type representing the absence of a value or a null value.                 |
| Custom User-Defined Types:                                                                                                                                     | You can define your own custom classes to create custom data types.                 |
| Special Types:                                                                                                                                                 |                                                                                     |
| `Ellipsis (...)`                                                                                                                                               | Represents an extended slice in certain data structures.                            |
| `NotImplemented`                                                                                                                                               | Represents a method or operation that is not implemented.                           |
| Other Types:                                                                                                                                                   |                                                                                     |

## Console Input and Output in Python

Python provides ways to interact with the console (command line) for both input and output operations. These operations are essential for user interaction, data input, and displaying results.

### Console Input

- **`input()` Function**: Python's `input()` function is used to read input from the user via the console. It displays a prompt and waits for the user to enter text. The entered text is returned as a string.

  ```python
  user_input = input("Enter something: ")
  
### Console Output

- **`print()` Function**: Python's `print()` function is used to print data on console. 

  ```python
    print("Enter something: ")
  ```
  ``` python
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
  ```
  ``` python
  import sys

  user_input = sys.stdin.readline()
  sys.stdout.write("This is standard output.")
  sys.stderr.write("This is an error message.")
  ```
  #### Data type conversion while taking input
  ```python
  user_input = input("Enter an integer: ")
  try:  # Observer try and catch
      integer_value = int(user_input)
      print(f"You entered an integer: {integer_value}")
  except ValueError: # Observer how catch is written
      print("Invalid input. Please enter an integer.")
  ```
  ```python
  float_value = float(input("Enter a  number: "))
  string_value = str(input("Enter a  number: "))
  ```

## If-Else Statements

In Python, `if` and `else` are control flow statements used for decision-making. They allow you to execute different blocks of code based on specified conditions. Here's a brief summary:

- **`if` Statement**: The `if` statement is used to execute a block of code if a specified condition is `True`. It has the following syntax:

  ```python
  if condition:
      # Code to execute if the condition is True

  --
  if condition:
    # Code to execute if the condition is True
  else:
    # Code to execute if the condition is False
  
  --
  if condition1:
    # Code to execute if condition1 is True
  elif condition2:
    # Code to execute if condition2 is True
  else:
    # Code to execute if no conditions are True
  
### If condition constructs
    if condition
    if not condition
    if condition1 and condition2
    if condition1 or condition2
    if not condition1
    if condition1 and not condition2
    Comparison Operators: `<`, `>`, `<=`, `>=`, `==`, `!=`
    Membership Operators: `in`, `not in`
    Identity Operators: `is`, `is not`
    Ternary Conditional Operator

## While Statements constructs
  ```python
  while condition:
    # Code to execute if the condition is True
  ```
    while condition
    while not condition
    while condition1 and condition2
    while condition1 or condition2
    Comparison Operators: `<`, `>`, `<=`, `>=`, `==`, `!=`
    Membership Operators: `in`, `not in`
    Identity Operators: `is`, `is not`
    Break and Continue Statements

# Python Constructors

In Python, a constructor is a special method that is called when an object is created from a class. 
Constructors are used to initialize the attributes (variables) of an object and perform any setup that is needed for the object to function correctly.

### Default Constructor

A default constructor is provided by Python if you don't define one in your class. It initializes the object with default values.

Example:

```python
class MyClass:
    def __init__(self):
        self.value = 0
# Creating an object
obj = MyClass()
print(obj.value)  # Output: 0
```
### Parameterized Constructor

You can define your own constructor with parameters to initialize object attributes based on the provided values.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Creating an object with parameter values
alice = Person("Alice", 30)
```

# Python Naming Conventions

Python follows a set of naming conventions and style guidelines to ensure code readability and maintainability. Here are some of the key Python naming conventions:

1. **Variable Names**:
   - Use lowercase letters.
   - Separate words with underscores for readability (snake_case).
   - Choose descriptive and meaningful names.
   - Avoid using single-character variable names, except for loop counters (e.g., `i`, `j`) and mathematical variables (e.g., `x`, `y`).
   ```python
   age = 30
   user_name = "Alice"
   ```
2. **Function and Method Names**:
   - Use lowercase letters.
   - Separate words with underscores (snake_case).
   - Choose descriptive and concise names that indicate the function's purpose.
   - Use verbs for function names (e.g., `calculate_total`, `print_report`).
   ```python
   def calculate_total(price, quantity):
   def print_report(report_data):
   ```
3. **Class Names**:
   - Use CamelCase (capitalizing the first letter of each word).
   - Choose nouns or noun phrases for class names.
   - Avoid underscores in class names.
   ```python
    class Car:
    class ShoppingCart:
   ```
4. **Constants**:
   - Use uppercase letters.
   - Separate words with underscores (UPPER_CASE_SNAKE_CASE).
   - Declare constants at the module level and make them meaningful.
   ```python
    MAX_VALUE = 100
    PI = 3.14159
   ```
5. **Module Names**:
   - Use lowercase letters.
   - Avoid using special characters or spaces.
   - Module names should be short but meaningful.
   ```python
    import math_utils
   ```
   
6. **Package Names**:
   - Use lowercase letters.
   - Use single, short, and meaningful words.
   - Avoid underscores in package names.
   ```python
    import utilities 
   ```

7. **Private Names (Convention)**:
   - To indicate a name as "private" (not intended for external use), prefix it with an underscore (e.g., `_private_variable`).
   - This is a convention, and the name is not truly private or protected.
   ```python
    _internal_variable = 42  # Private variable (convention)
   ```
