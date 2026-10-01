
n=str
f=str
e=str
french=0
english=0
for i in range(n):
        if f[i]== "s" or "S":
            french +=1
        if e[i]=="T" or "t":
            english +=1
        if english > french:
            print ("English")

        else:
            print ("French")
n("ttttttttttt")