char = ""
cont = 0
while char!= ".":
    char = input("enter letter")
    if char == "l":
        char = input("enter letter")
        if char == "a":
            cont += 1

print(cont)