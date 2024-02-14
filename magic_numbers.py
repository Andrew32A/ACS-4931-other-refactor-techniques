# by Kami Bigdely 
# Replace magic numbers with named constanst

# constants for clarity
COULOMBS_CONSTANT = 8.9875517923e9
EVEN_DIVISOR = 2

def calculate_electric_force(q1, q2, distance):
    """
    Calculate the electric force exerted between two charges.
    """
    return COULOMBS_CONSTANT * q1 * q2 / (distance ** 2)

def is_even(number):
    """
    Check if a number is even.
    """
    return number % EVEN_DIVISOR == 0

# electric force calculation
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))
force = calculate_electric_force(q1, q2, distance)
print("Electric Force between q1 and q2 is: ", force, "Newton")

# check if number is even or odd
num = int(input('Enter an integer number: '))
if is_even(num):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
