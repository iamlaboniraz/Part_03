N=5

for i in range(0,N+1):
    for j in range(1,i+1):
        print(j,end='')
        if i!=j:
            print(end=',')
    print()
