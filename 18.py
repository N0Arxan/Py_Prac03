num = int(input("enter number : "))
num_ant = num -1
cont = 0
while num != 0 :
    if num > num_ant:
        cont += 1    
    num_ant = num
    num = int(input("enter number 1 : "))

print(cont)