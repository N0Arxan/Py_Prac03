char=input("enter parblas and seperate them with space: ")
cont_parablas=1
while char!=".":
    if " " in char:
        cont_parablas+=1
    char=input("enter parablas and seperate them with space: ")
print(cont_parablas)