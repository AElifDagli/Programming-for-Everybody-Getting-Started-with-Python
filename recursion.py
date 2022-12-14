def factorial(n):                # recursive function (parameters)
    if n < 2:                    # base case condition (parameters)
        return 1                 # base case value
    return n * factorial(n - 1)  # recursive function (modified parameters)

# OR

def factorial(x):
    if x == 1:
        return 1
    else :
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

# toplama

def sum_positive_numbers(n):
  if n<1:
    return 0
  return (n + sum_positive_numbers(n-1))

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# ************************************************************************************************************
# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base.
# Note: base is assumed to be a positive number.
# Tip: for functions that return a boolean value, you can return the result of a comparison.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False