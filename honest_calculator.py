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
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

active = True
memory = float(0)


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def in_memory(value):
    if value == 'M':
        return True


def is_one_digit(value):
    if -10 < value < 10:
        if value.is_integer():
            return True
        else:
            return False
    else:
        return False


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


while active:
    print("Enter an equation")
    equitation = input().split()
    x = equitation[0]
    y = equitation[2]
    oper = equitation[1]

    if in_memory(x):
        x = memory
    if in_memory(y):
        y = memory
    if not in_memory(x) and not in_memory(y) and isfloat(x) and isfloat(y):
        x = float(x)
        y = float(y)
    else:
        print(msg_1)
        continue
    if oper in '+-*/':
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/' and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
        print(result)
        if_save = ''
    else:
        print(msg_2)
        continue
    while if_save == '':
        print(msg_4)
        if_save = input()
        if if_save == 'y':
            if is_one_digit(result):
                msg_index = 10
                while msg_index < 13:
                    print(globals()['msg_' + str(msg_index)])
                    answer = input()
                    if answer == 'y':
                        msg_index += 1
                        continue
                    if answer == 'n':
                        break
                    else:
                        continue
                if msg_index >= 13:
                    memory = result
            else:
                memory = result
        elif if_save == 'n':
            pass
        else:
            if_save = ''
            continue
        if_continue = ''
        while if_continue == '':
            print(msg_5)
            if_continue = input()
            if if_continue == 'y':
                break
            elif if_continue == 'n':
                active = False
                break
            else:
                if_continue = ''
                continue
        break
    continue
