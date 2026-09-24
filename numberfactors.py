z=int(input("I will factor your integer (if it's positive)"))
for i in range(1, z+1):
    if z % i == 0:
        print(i)