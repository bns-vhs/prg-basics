def f(palindrome:str)->str:
        if palindrome == palindrome[::-1]:
            return True
        else:
            return False

        
print(f('12-11-21'))



def funkcja(palidrom:str)->bool:
     return palidrom == palidrom[::-1]


print(funkcja('book'))