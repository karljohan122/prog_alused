from random import *

for i in range (10):
    rndm = random.randint(1, 1000)
    konekestus.append(rndm)

minutihind = float(input("Sisestage kõneminuti hind: "))

konedearv = int(input("Sisestage kõnede arv: "))

konehind1 = minutihind * 1

konehind2 = minutihind * 10

konehind3 = minutihind / 60


if any(x<60 for x in konekestused):
    print("Kõne maksumus on " + str(konehind1))
if any(x>600 for x in konekestused):
    print("Kõne maksumus on " + str(konehind2))
else: print("Kõne maksumus on" + str (konehind3))
