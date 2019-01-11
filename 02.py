N = 5

for i in range(0,N):
    for j in range(0,N):
        if i==0:
            print("*",end='')
        elif i==N-1:
            print("*",end='')
        else:
                x=int(N/2)
                if x==j:
                       print(" ",end='')
                elif i==x:
                    if j==0:
                        print("*",end='')
                    elif j==N-1:
                        print("*",end='')
                    else:
                        print(" ",end='')
                else:
                    print("*",end='')
    print()
    
