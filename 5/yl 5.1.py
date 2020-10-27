fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
for el in vastuvõetud:
    print(el)
L = input("Palun sisestage, millise aasta andmeid vajate(2011-2019): ")
jeet = int(L) - 2010
jeef = print(str(L) + ". aastal oli vastuvõetud " + str(vastuvõetud[int(L[3])-1]))
fail.close()