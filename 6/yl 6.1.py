def banner(a):
  return a.upper()
mitu = int(input("Mitu korda soovite reklaamilauset kuvada? "))
tekst = str(input("Siesestage reklaami lause "))
for number in range(mitu):
    print((banner)(tekst))