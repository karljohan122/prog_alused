from random import *
õun = int(input("Mitu pöialpoissi tahab õuna(0-7)? "))
N = 0
L = 0
n = 14
while N < õun:
    L = randint(1,2)
    n -= L
    N += 1
    print(L)
print("Lumivalgekesel jäi " + str(n))