char:str = ""
sum:int = 0
vocal:str = ""
founded:bool = False
while char != "." :
    char = input("enter a letra ")
    if (char == "a" or char == "o" or char == "i" or char == "e" or char == "u") and (founded == False) :
        founded = True
        vocal = char 
    
print(vocal)