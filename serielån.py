laan = float(input("Hvor mye vil du låne? "))
rente = float(input("Hva er renten i prosent? ")) / 100
aar = int(input("Hvor mange år skal lånet løpe? "))
avdrag = laan / aar

print("\nLån\t\tRenter\t\tAvdrag\t\tRestlån")

for i in range (aar):
    renter = laan * rente
    restlaan = laan - avdrag
    print("%8.2f\t%8.2f\t%8.2f\t%8.2f" % (laan, renter, avdrag, restlaan))
    laan = restlaan