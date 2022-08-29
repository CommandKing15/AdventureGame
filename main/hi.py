import random
import time

def radn(input):
    i = input + random.randint(0, input)
    i * input + random.randint(0, i)
    i / input
    if i < input:
        i += i
    if i > input * 5:
        i -= i + input

    return i

def miss():
    a = random.randint(-20, 50)
    
    if a > 1:
        a = 1
    elif a < 1:
        a = 0
    return a

print(radn(10))
print(radn(10))
print(radn(10))
print(radn(10))
print(radn(10))
print(radn(10))
print(radn(10))
print(radn(10))
print(miss())
print(miss())
print(miss())
print(miss())
print(miss())
print(miss())
print(""" It's fightin' time!

                                        [1] Run
                                        [2] Fight!
                                    """)

time.sleep(10)