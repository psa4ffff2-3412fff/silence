def spaces (n,y,t):
    output = 0
    for i in range(n):
        if y[i] == "c" and t[i] == "c":
            output +=1
    print(output)
spaces(5,"c.c.c","ccccc")
