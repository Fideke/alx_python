def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
print(add(1, 2), end="\n")
print(add(98, 0), end="\n")
print(add(100, -2), end="\n")


