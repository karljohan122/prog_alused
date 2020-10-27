vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ")
tüüp = int(input(" Sisestage treeningu tüüp: "))
## ""
sugu = sugu.upper()
#minpulss
#maxpulss
s = 0
if sugu == ("N"):
    vanusnaine = vanus * 0.88
    s = 206 - vanusnaine
else:
   s = 220 - vanus
if tüüp == 1:
    minpulss = s * 0.50
    maxpulss = s * 0.70
elif tüüp == 2:
    minpulss = s * 0.70
    maxpulss = s * 0.80
else:
    minpulss = s * 0.80
    maxpulss = s * 0.87
minpulss = round(minpulss)
maxpulss = round(maxpulss)
print("Pulsisagedus peaks olema vahemikus " + str(minpulss) + " kuni " + str(maxpulss))