import sys

K = int(sys.stdin.readline())
stack = []

for i in range(K):
    temp = int(sys.stdin.readline())
    if temp != 0:
        stack.append(temp)
    else:
        stack.pop(len(stack)-1)

print(sum(stack))