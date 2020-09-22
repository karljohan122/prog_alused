nimi = str(input("Sisestage oma nimi: "))
lubatud_kiirus = int(input("Sisestage lubatud kiirus: "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus: "))
lause_osa = " Teie trahv on: "
euro = "€"
ületatud_kiirus = tegelik_kiirus - lubatud_kiirus
trahv = min(190, ületatud_kiirus * 3)
print(nimi + lause_osa + str(trahv) + euro)
