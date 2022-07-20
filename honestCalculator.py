# write your code here
from turtle import circle


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

operation = {"-", "+", "*", "/"}


while True:
    print(msg_0)
    calc = input()
    x,oper, y = input().split()
    

    try:
        x = float(x)
        y = float(y)
        
    except:
        print(msg_1)
        continue
    
    if oper in ["-", "+", "*", "/"]:
        break
    else:
        print(msg_2)


  


   
   
