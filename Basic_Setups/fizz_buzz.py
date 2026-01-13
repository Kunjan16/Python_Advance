def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    return input

print(fizz_buzz(3))    # Output: Fizz
print(fizz_buzz(5))    # Output: Buzz
print(fizz_buzz(15))   # Output: FizzBuzz
print(fizz_buzz(7))    # Output: 7