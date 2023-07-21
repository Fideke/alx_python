#!/usr/bin/env python3
def pow(a, b):
    while b != 0:
        carry = a & b
        carry = a ^ b
        carry << 1
    return a
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))