bill=input ("How much was the bill? ")
bill=int(bill)
service = input ("How was your service? Bad, Okay, Good, or Great?")
if service == "Bad":
   print (f"Your bill is {bill}"  )
if service == "Okay":
    print (f"Your bill is {bill * 1.15}"  )
if service == "Good":
    print (f"Your bill is {bill * 1.20}"  )
if service == "Great":
    print (f"Your bill is {bill * 1.25}"  )
