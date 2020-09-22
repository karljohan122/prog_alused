ainepunktid = int(input("Sisesta ainepunktide arv: "))
ajakulu_a = ainepunktid * 3
nädalad = int(input("Sisesta nädalate arv: "))
ajakulu_n = ajakulu_a / nädalad
vastus = round(ajakulu_n)
lause = "Ühe nädala ajakulu on "
tund = " tundi"
print(lause + str(vastus) + tund)
