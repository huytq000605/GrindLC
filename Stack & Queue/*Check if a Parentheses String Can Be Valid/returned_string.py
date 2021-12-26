def canValid(s: str, locked: str):
    s = list(s)
    locked = list(locked)
    n = len(locked)
    if n % 2 == 1:
        return False
    stack = []
    current_open = 0
    for i in range(n):
        if locked[i] == "1":
            if s[i] == "(":
                current_open += 1
            else:
                current_open -= 1
        else:
            stack.append(i)
        if current_open < 0:
            if len(stack) == 0:
                return False
            current_open += 1
            idx = stack.pop()
            s[idx] = "("
            locked[idx] = "1"

    stack = []
    current_open = 0
    for i in range(n - 1, -1, -1):
        if locked[i] == "1":
            if s[i] == ")":
                current_open += 1
            else:
                current_open -= 1
        else:
            stack.append(i)
        if current_open < 0:
            if len(stack) == 0:
                return False
            current_open += 1
            idx = stack.pop()
            s[idx] = ")"
            locked[idx] = "1"
    m = len(stack)
    for i in range(m):
        if i % 2 == 0:
            s[stack[i]] = ")"
        else:
            s[stack[i]] = "("

    stack = 0
    for l in s:
        if l == "(":
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            print("WRONG")
            return

    if(stack != 0):
        print("WRONG")
        return
        

    print(''.join(s))
    return s

# s = "())()))()(()(((())(()()))))((((()())(())"
# locked = "1011101100010001001011000000110010100101"              
s = "))()))"
locked = "010100"
canValid(s, locked)
