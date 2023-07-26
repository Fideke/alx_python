import main
from main import add
print(add(1, 2))

# a and be must be defined in 2 different lines a=1, b=2
def add_0(a, b):
    return a + b

a = 1
b = 2

sum = add_0(a, b)

print(f"{a} + {b} = {sum}", end="\n")