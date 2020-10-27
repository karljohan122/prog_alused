from datetime import*
def kuu_nimi(invest):
    return (päevalist[int(invest)-1])

päevalist = ["jaanuar", "veebruar", "märts", "april", "mai", "juuni", "juuli",  "august" , "september" , "oktoober" , "november",  "detsember"]
mis = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
def kuupäev_sõnena(b):
    b = b.split(".")
    return (b[0] + ". " + kuu_nimi(int(b[1])) + " "+ b[2] +  ". a")
print(kuupäev_sõnena(mis))