
Speach_A = "Every thing is Ture"

Speach_B = "Every thing is False"
print(Speach_A)
print(Speach_B)
User_ent = input("type A if option A is correct and B if option B is correct:\n").lower()
if User_ent == "true":
    SP_A = True 
    SP_B = False
elif User_ent == "false":
    SP_A = False 
    SP_B = True


if SP_A == False and SP_B == True:
    print(Speach_A)
    


    


