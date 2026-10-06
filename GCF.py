x= int(input("I can find GCF (if it's positive). Insert 1 integer."))
y=int(input("insert second integer"))

factor_x=list()
for i in range(1, x+1):
    if x % i == 0:
        factor_x.append(i)

factor_y=list()
for i in range(1, y+1):
    if y % i == 0:
        factor_y.append(i)
        
#print (factor_x) 
#print (factor_y)

gcf=int()
for i in (factor_x):
    for j in (factor_y):
        if i == j: 
            gcf = i

print (gcf)