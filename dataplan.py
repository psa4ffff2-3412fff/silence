def diseases(n, r, p, d, s):
    for i in range(1, d+1):
        s=r*i+1         
        if s>p:
            break 



diseases(1, 5, 750)
print(p)










#n=number of people who start with disease
#r=number of people infected on the next day. all infected infect r amount of people next day
#p=we need the code to stop once s>p
#d=days it takes for infected population to pass p
#s=infected population