num = int(input("enter number: "))
num_ant = num
longitud_max = 0

while num != 0 :
    
    longitud = 0
   
    while (num == num_ant) and (num != 0):
        longitud += 1 
        num_ant = num
        num = int(input("enter number 2: "))
    
    if longitud_max < longitud:
        longitud_max = longitud
    
    num_ant = num
        
    
print(longitud_max)