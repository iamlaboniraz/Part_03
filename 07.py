N=5

x=1

a=2
b=N
for i in range(1,N+1):
    for j in range(1,N+1):
        if i<=j:
            print(j,end='')
        if i==a and j==N:
            for k in range(1,i):
                if j==N:
                    print(k,end='')
            a=a+1
            b=b-1

    print()
