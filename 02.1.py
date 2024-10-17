char:str = ""
sum:int = 0
char_donat:str = input("dona un char : ")
sum_partir:int = 0 
conatr:bool = False

while char != "." :
    char = input("enter a letra : ") 
    
    sum += 1
    
    if char == char_donat:
        conatr = True
    
    if conatr:
        sum_partir += 1 
    
    
    

print(f"total chars = {sum - 1}")
print(f"chars a partir de {char_donat} = {sum_partir - 1 }")