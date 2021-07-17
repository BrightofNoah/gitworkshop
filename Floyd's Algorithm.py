INF=999999
def floydWarshal(cost,p,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(cost[i][k]+cost[k][j]<cost[i][j]):
                    cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
                    p[i][j]=k
    print("Cost Matrix:")
    for i in range(n):
        for j in range(n):
            if(cost[i][j]==INF):
                print("INF",end="\t")
            else:
                print(cost[i][j],end="\t")
        print()
def path(p,q,r):
    if p[q][r] != 0:
        path(p,q,p[q][r])
        print("v =",p[q][r])
        path(p,p[q][r],r)
        return
    else:
        return
p=[[0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]]
graph = [[0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]]
floydWarshal(graph,p,4)
print("\nPaths:")
for i in range(0,4):
    for j in range(0,4):
        if i==j:
            continue
        else:
            print(i,j,": ")
            path(p,i,j)