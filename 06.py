N = 11
x=int(N/2)

a=0
b=N-1

c=x+1
d=x-1

for i in range(0,N):
    for j in range(0,N):
        if i==j:
            if i==x:
                print("1",end='')
            else:
                print("*",end='')
        elif i==a and j==b:
            print("*",end='')
            a=a+1
            b=b-1
        elif i==c and j==d:
            print("*",end='')
            c=c+1
            d=d-1            
        else:
            print(" ",end='')
    print()
