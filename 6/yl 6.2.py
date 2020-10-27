def eelarve(kutsun):
    return kutsun * 10 + 55


kutsutud = int(input("mitu on kutsutud: "))
tuleb = int(input("mitu inimest tuleb: "))
a = eelarve(kutsutud)
A = eelarve(tuleb)
print("Maksimaalne eelarve on " + str(a))
print("Minimaalne eelarve on " + str(A))
from datetime import *


def kuu_nimi(invest):
    return (päevalist[int(invest) - 1])