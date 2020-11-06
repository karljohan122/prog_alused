from random import *

sammud = []  #sammude arvude järjend

def km(sammud, sammud_meetrites):                 #funktsioon, mis ei tee hetkel mitte midagi, kuid vastus tuleb siiski õige
    km_arv = (sammud * sammud_meetrites) / 1000
    return(km_arv)

sammud_meetrites = int(input("Sisestage sammude pikkus meetrites: ")) #küsib samme meetrites

for i in range(7):                 #tsükliga lisab 7 suvalist sammude arvu
    rndm = randint(5000, 15000)
    sammud.append(rndm)

print("Sammude arvud järjekorras päevade järgi: ")    #tsükliga väljastab igal päeval läbitud sammude arvud
i = 0
while i < 7:
    print(str(sammud[i]), "sammu")
    i += 1

print("Sammud arvutatud kilomeetriteks: ")    #tsükliga muudab sammude arvud meetriteks ning väljastab nad kilomeetritena
i = 0
while i < 7:
    print(str(round((sammud[i] * sammud_meetrites) / 1000)), "km")
    i += 1

Km_summa = (sum(sammud * sammud_meetrites) / 1000)       #läbitud tee pikkus kokku kilomeetrites (7 päeva)
print("Kilomeetreid iga päev kokku: " + str(round(Km_summa)) + " km")

def keskmine(num):              #leiab 7 päeva keskmise sammude arvu
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg

print("Keskmine sammude arv päevas: ", round(keskmine(sammud)), "sammu") #kui sammud on üle 1000 siis on kõik korras, kui on alla 10000 siis peab rohkem pingutama

if keskmine(sammud) > 10000:
    print("Keskmine sammude arv nädalas on 10000, olete tubli :)")
else:
    print("Keskmine sammude arv nädalas on alla 10000, peate suurema entusiasmiga kõndima")

km(1, 2)
