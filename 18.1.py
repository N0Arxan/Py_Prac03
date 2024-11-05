num = int(input("enter number : "))
num_ant = num -1
cont = 0
while num != 0 :
    while (num > num_ant) and (num != 0):
        cont += 1    
        num_ant = num
        num = int(input("enter number 1 : "))
    while (num == num_ant) and (num != 0):
        num_ant = num
        num = int(input("enter number 2 : "))

print(cont)