char:str = ""
sum:int = 0
while char != "." :
    char = input("enter a letra ")
    if char == "a" or char == "o" or char == "i" or char == "e" or char == "u" :
        sum += 1
    
print(sum)