num = int(input("enter number : "))
num_ant = num - 1
creixent = True
while num != 0 and creixent:
    if num < num_ant:
        creixent = False 
    num_ant = num
    num = int(input("enter number 1 : "))

if not creixent:
    print("no es creixent")
else :
    print("es creixent")
