x = int(input("Enter the value of a_1: "))
y = int(input("Enter the value of a_2: "))
z = int(input("Hvor i rekken vil du finne: "))
i = 0
a = []

a.append(x)
a.append(y)

d = a[1] / a[0]
n = z - 1
a_n = a[0] * d ** n

for i in range(10):
    o = a[i+1] * d
    a.append(o)
    i += 1

print(a_n)
print(a)


