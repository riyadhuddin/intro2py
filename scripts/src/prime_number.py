#prime numbers - Integers that have only two factors, which are the number itself multiplied by 1. The lowest prime number is 2.
def prime_number():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
#prime_number()
# prime factors - Prime numbers that are factors of an integer. For example, the prime numbers 2 and 5 are the prime factors of the number 10 (2x5=10). The prime factors of an integer will not produce a remainder when used to divide that integer. 
def prime_factors():
    num = int(input("Enter a number: "))
    for i in range(2, num):
        while num % i == 0:
            print(i)
            num = num / i
#prime_factors()
# divisor - A number (denominator) that is used to divide another number (numerator). For example, if the number 10 is divided by 5, the number 5 is the divisor.
def divisor():
    num = int(input("Enter a number: "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
#divisor()
#sum of all divisors of a number - The result of adding all of the divisors of a number together.  
def sum_of_all_divisors():
    num = int(input("Enter a number: "))
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
    print(sum)
#sum_of_all_divisors()
#    multiplication table - An integer multiplied by a series of numbers and their results formatted as a table or a list. 
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
#multiplication_table()
#Fix the while loop so there is an exit condition

def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number != 0 and number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False