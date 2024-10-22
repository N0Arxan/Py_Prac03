num = int(input("enter a number"))
negative = False
while num != 0 :
    num = int(input("enter a number"))
    if num < 0 :
        negative = True
if negative:
    print("there is negative valor")
else:
    print("no hiha negativo")