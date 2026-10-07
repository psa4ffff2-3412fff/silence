def wizards(n,start,duels):
    wand_winners=list()
    owner=start
    change_hands=1
    wand_winners.append(start)
    for i in range(0,n):
        if duels[i][1] == owner:                #i=0 , owner=A, duels[i][1]=A
            owner = duels[i][0]
                                                # if owner is not in wand winners then add 1 and add to wand winners
            if is_owner_winning_for_first_time(owner, wand_winners):
                change_hands+=1
                wand_winners.append(owner)
    print(owner)
    print(change_hands)

def is_owner_winning_for_first_time(owner, wand_winners): #winning first time  
                                                        #return false if owner in wand winners
                                                        #return true if not in wand winners
    for j in wand_winners:
        if j == owner:
            return False
    return True

#wizards(5, "N", ["DA", "NB", "BA", "CD", "FA"])
wizards(4, "X", ["AX", "BX", "XA", "DA"])
#wizards(3, "A", ["BA", "CB", "DA"])







#todo
    #find how many wizards held wand
    #find which wizard holds wand at end
