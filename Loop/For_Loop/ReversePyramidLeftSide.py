n = 5
for i in range(n, 0, -1):
    for j in range(0, n-1+i):
        print(" " , end=' ')
    for k in range(0, i):
        print(" * " , end='')
    
    print("")