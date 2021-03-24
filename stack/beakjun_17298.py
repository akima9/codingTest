N = int(input())
A = list(map(int,input().split()))
stack = []

for i in range(N):

    while stack and A[stack[-1]] < A[i]:
        A[stack[-1]] = A[i]
        stack.pop()

    stack.append(i)

while stack:
    A[stack[-1]] = -1
    stack.pop()

for i in A:
    print(i,end=' ')