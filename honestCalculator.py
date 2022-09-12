
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"

result = 0
memory = 0

operation = {"-", "+", "*", "/"}


while True:
    print(msg_0)
    calc = input()
    x,oper, y = calc.split()

    try:
        x = float(x)
        y = float(y)
        
    except:
        print(msg_1)
        continue
    
    if oper in ["-", "+", "*", "/"]:
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/" and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
    else:
        print(msg_2)
        continue
    
    print(result)
    print(msg_4)
    answer = input().lower()

    if answer == "y":
        

  


   
   
