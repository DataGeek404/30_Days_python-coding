"""a=3
b=a+3
print(b)
"""
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List - Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.
print(type({'name':'Asabeneh'})) # Dictionary- A Python dictionary object is an unordered collection of data in a key value pair format.
print(type({9.8, 3.14, 2.7}))    # Set- A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.
print(type((9.8, 3.14, 2.7)))    # Tuple - A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.


"""
Exercise: Level 3

    Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    Find an Euclidian distance between (2, 3) and (10, 8)

"""
#part 1

# Number Data Types
integer_example = 42  # An integer
float_example = 3.14  # A floating-point number
complex_example = 2 + 3j  # A complex number

# String Data Type
string_example = "Hello, world!"

# Boolean Data Type
boolean_example = True  # Boolean value can be either True or False

# List Data Type
list_example = [1, 2, 3, "a", "b", "c", True, 3.14]  # A list can contain elements of different types

# Tuple Data Type
tuple_example = (1, 2, 3, "a", "b", "c", True, 3.14)  # A tuple is similar to a list but is immutable

# Set Data Type
set_example = {1, 2, 3, 4, 5}  # A set contains unique elements only

# Dictionary Data Type
dictionary_example = {"name": "Alice", "age": 25, "city": "New York"}  # A dictionary has key-value pairs

#part 2
import math

# Define the points
point1 = (2, 3)
point2 = (10, 8)

# Calculate the difference in coordinates
dx = point2[0] - point1[0]
dy = point2[1] - point1[1]

# Calculate the Euclidean distance
distance = math.sqrt(dx**2 + dy**2)
print("Euclidean distance:", distance)
