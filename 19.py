num = int(input("enter number: "))
cont = 0
num_ant = num - 1
longtitud = 1
while num != 0 :

    if longtitud < cont:
        longtitud = cont 

    cont = 0
    
    num_ant = num
    num = int(input("enter number 3: "))
    
    while (num == num_ant) and (num != 0):
        cont += 1 
        num_ant = num
        num = int(input("enter number 2: "))
        
    
    
print(longtitud)