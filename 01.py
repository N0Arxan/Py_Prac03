char:str = ""
sum:int = 0
while char != "." :
    char = input("enter a letra ")
    if char == "a" :
        sum += 1
    
print(sum)