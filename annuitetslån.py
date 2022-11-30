laan = float(input("Hvor mye vil du låne? "))
rente = float(input("Hva er renten i prosent? ")) / 100
aar = int(input("Hvor mange år skal lånet løpe? "))
annuitet = float(input("Hva er annuiteten? "))

print("\nLån\t\tRenter\t\tAvdrag")

for i in range (aar):
    renter = laan * rente
    avdrag = annuitet - renter
    laan = laan - avdrag 
    print("%8.2f\t%8.2f\t%8.2f" % (laan, renter, avdrag))
