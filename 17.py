num = int(input("enter number: "))
cont = 1
num_ant = num
while num != 0 :
    if num < num_ant:
        cont +=1 
        print("..")
    num_ant = num
    num = int(input("enter number: "))
    
    
print(cont)