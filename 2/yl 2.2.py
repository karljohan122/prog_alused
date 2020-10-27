nimi = input("Sisesta nimi: ")
if nimi[-2:] == "ne":
   print("abielus")
elif nimi[-2:] == "te":
   print("vallaline")
elif nimi[-1] == "e":
   print("määramata")
else:
   print("pole ilmselt leedulanna perekonnanimi")