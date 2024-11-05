char=input("enter char: ")
primer_char=char
trobat=False
while char!="." and (not trobat):
    char_ant=char
    char=input("enter char: ")
    if char_ant == " ":
        if char != primer_char:
            trobat=True
    