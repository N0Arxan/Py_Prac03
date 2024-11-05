num = int(input("enter number : "))
num_ant=num
num_max=num
num_min=num
conta_canvi=-1
while num!=0:
    while num < 0 and num!=0:
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num
        num = int(input("enter number : "))

    conta_canvi+=1

    while num > 0 and num!=0:
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num
        num = int(input("enter number : "))
    
print(num_max,num_min,conta_canvi)
