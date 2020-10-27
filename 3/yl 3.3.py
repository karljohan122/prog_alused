from random import *
Täring = int(input("Tärnigute arv: "))
N = 0
L = 0
while N < Täring:
    L = randint(1,6)
    N += 1
    print(L)