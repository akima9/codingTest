import sys
input=sys.stdin.readline

N = int(input())
stack = []
result = []
for i in range(N):
    a = input().split()
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        if len(stack) > 0:
            #result.append(stack[len(stack)-1])
            print(stack[len(stack)-1])
            stack.pop(len(stack)-1)
        else:
            #result.append(-1)
            print(-1)
    elif a[0] == 'size':
        #result.append(len(stack))
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack) > 0:
            #result.append(0)
            print(0)
        else:
            #result.append(1)
            print(1)
    elif a[0] == 'top':
        if len(stack) > 0:
            #result.append(stack[len(stack)-1])
            print(stack[len(stack)-1])
        else:
            #result.append(-1)
            print(-1)
        
