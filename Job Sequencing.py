def jobSequencing(id,p,d):
    t=max(d)
    result = [False] * t
    job = ['-1'] * t
    for i in range(len(p)):
        for j in range (min(t-1, d[i]),-1,-1):
            if result[j] is False:
                result[j] = True
                job[j] = id[i]
                break
    print(job)
id=[int(x) for x in input("Enter the JOB ID:").split()]
p=[int (y) for y in input("Enter the Profits of the JOB:").split()]
d=[int (z) for z in input("Enter the deadlines of the JOB:").split()]
jobSequencing(id,p,d)