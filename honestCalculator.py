msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msgs = {0: msg_0, 1: msg_1, 2: msg_2, 3: msg_3, 4: msg_4, 5: msg_5, 6: msg_6,
        7: msg_7, 8: msg_8, 9: msg_9, 10: msg_10, 11: msg_11, 12: msg_12}


def check(v1,v2,v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if ((v1 == 1 or v2 == 2) and v3 == "*"):
        msg += msg_7
    if ((v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-")):
        msg += msg_8
    if (msg != ""):
        msg = msg_9 + msg
        print(msg)

def is_one_digit(v):
    if  -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


result = 0
memory = 0
running = True

operation = {"-", "+", "*", "/"}

while running:
    print(msg_0)
    calc = input()
    x,oper, y = calc.split()
    

    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
        
    except:
        print(msg_1)
        continue


    if oper in ["-", "+", "*", "/"]:
        check(x,y,oper)
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

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            #memory = result
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msgs[msg_index])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer != 'n':
                        continue
                    else:
                        break
            else:
                memory = result
                


    answer = ""
    while answer != "y" and answer != "n":
        print(msg_5)
        answer = input()
        if answer == "n":
            running = False
