num = int(input("enter number : "))
num_ant = num 
monotona = True
while num != 0 and (monotona==True):
    if num_ant < num :
        while num != 0 and (monotona==True):
            num_ant = num
            num = int(input("enter number 1 : "))
            if num_ant > num : 
                monotona = False

    elif num_ant > num :
        while num != 0 and (monotona==True):
            num_ant = num
            num = int(input("enter number 2 : "))
            if num_ant < num : 
                monotona = False

    else:
        num_ant = num
        num = int(input("enter number 3 : "))       

if not monotona:
    print("no es monotoma")
else :
    print("es monotoma")
