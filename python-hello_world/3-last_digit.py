
import random
number = random.randint(-10000, 10000)

last_digit = number % 10
if last_digit > 5:
    answer = f"The string Last digit of {number} is {last_digit} and is greater than 5"
elif last_digit == 0:
     answer = f"The string Last digit of {number} is {last_digit} and is greater than 0"
elif last_digit < 6 and last_digit != 0:
      answer = f"The string Last digit of {number} is {last_digit} and is less than not 0"

print(answer)