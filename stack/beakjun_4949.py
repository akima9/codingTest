while True:
    N = input()
    
    if N == '.':
        flag = False
        break
    
    stack = []
    flag = True

    for i in N:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break

    if flag and not stack:
        print('yes')
    else:
        print("no")