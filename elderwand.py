def wizards(n,start,duels):
    owner=start
    change_hands=1
    print(duels[0][1])
    for duels in range(0):
        if duels[0][1] == owner:
            owner = duels[0][0]
            change_hands+=1
    print(owner)
    print(change_hands)
    
wizards(3, "A", ["BA", "CB", "DA"])








#todo
    #find how many wizards held wand
    #find which wizard holds wand at end
