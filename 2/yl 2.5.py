suurus = float(input("sisesta kirja suurus: "))
pealkiri = input("Sisesta kirja pealkiri: ")
fail = input("Kas kirjaga on kaasas fail(jah,ei): ")
if pealkiri == "" or suurus > 1 and fail == "jah":
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")