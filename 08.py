N=7

x=int(N/2)+1

a=2
b=N-1

for i in range(1,N+1):

    for j in range(1,N+1):
        if i==1:
            print("1",end='')
        elif j==1:
            print("1",end='')


    for k in range(2,N):
        if i==k:
            for l in range(k,N):
                if i==x and l!=x:
                    y=x+3
                    print(y,end='')
                else:
                    print(l,end='')

    print()
