n = int(input("enter no of items"))
W = int(input("enter max weight"))
m=[[0 for i in range(W+1)] for j in range(n+1)]
p = [] * n
w = [] * n
for i in range(n):
    w.append(int(input("enter weight values")))
for i in range(n):
    p.append(int(input("enter profit values")))
for i in range(n+1):
    for j in range(W+1):
        if (i == 0 or j == 0):
            m[i][j] = 0
        elif (w[i-1] <= j):
            m[i][j] = max(p[i-1]+m[i - 1][j - w[i-1]] ,m[i - 1][j])
        else:
            m[i][j] = m[i - 1][j]
print("max profit is", m[n][W])
