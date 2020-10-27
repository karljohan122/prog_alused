ring = int(input("sisesta ringide arv: "))
N = 0
V = 0
while N <= ring:
    if N%2 == 0:
        V += N
    N += 1
print("Porgandite koguarv on " + str(V))