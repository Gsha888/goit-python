result = 0
s = input("Знак (+,-,*,/,): ")

while s not in ('+', '-', '*', '/', '='):
    s = input("wrong sign plz try again: ")

if s in ('+', '-', '*', '/',):
    x = float(input("x="))
    y = float(input("y="))
    
    if s == '+':
        result += x + y
    elif s == '-':
        result += x - y
       
    elif s == '*':
        result += x * y
        
    elif s == '/':
        if y != 0:
            result += x / y
            
        else:
            print("cant dev by 0")
            result = result    
while True:
    s = input("Знак (+,-,*,/,=): ")
    
    if s == '=':
        print(result)
        break
    
    while s not in ('+', '-', '*', '/',):
        s = input("Wrong sign plz try again: ")
    
    if s in ('+', '-', '*', '/',):
        z = float(input("Next number: "))
        
        if s == '+':
            result = result + z
        
        elif s == '-':
            result -= z
        
        
        elif s == '*':
            result *= z
       
        
        if s == '=':
            print(result)
            break
        elif s == '/':
            if z != 0:
                result /= z
            
            else:
                print("Деление на ноль!")

    if s not in ('+', '-', '*', '/', '='):
        print("Wrong sign!")
    
