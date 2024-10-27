char = ""
conta = 0
contl = 0
while char!= ".": 
    char = input("enter letter") 
    if char == "l":
        char = input("enter letter")
        if char == "a":
            contl += 1
    
    if char == "a":
        char = input("enter letter")
        if char == "l":
            conta += 1


print(conta+contl)