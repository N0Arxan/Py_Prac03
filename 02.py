char:str = ""
sum:int = 0
char_donat:str = input("dona un char : ")
sum_partir:int = 0 

while char != "." :
    char = input("enter a letra : ")
    sum += 1
    if char == char_donat:
        while char != "." :
            char = input("enter a letra : ")
            sum_partir += 1

    
print(f"total chars = {sum + sum_partir}")
print(f"chars a partir de {char_donat} = {sum_partir}")