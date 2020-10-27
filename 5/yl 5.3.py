fail = open("konto.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(float(rida))
for el in vastuvõetud:
    if el > 0:
        print(el)
fail.close()