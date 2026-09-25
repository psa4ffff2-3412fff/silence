z=int(input("I can find GCF (if it's positive). Insert 1 number."))
for i in range(1, z+1):
    if z % i == 0:
        print(i)
y=int(input("Insert 2nd number."))
for n in range(1, y+1):
    if y % n == 0:
        print(n)