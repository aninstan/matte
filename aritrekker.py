x = int(input("Enter the value of a_1: "))
z = int(input("Hvor i rekken vil du finne: "))
a = []

a.append(x)

for i in range (z):
    o = 2 * a[i] + 1
    a.append(o)
    i += 1

print(a)