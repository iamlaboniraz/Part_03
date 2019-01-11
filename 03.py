N=20
for i in range(0,N):
    for j in range(i,N-1):
        print(" ",end='')

    for k in range(0,i+1):
        if i==0 or i==1:
            print("*",end='')
        elif i==N-1:
            print("*",end='')

    if i!=0 and i!=1 and i!=N-1:
        for l in range(0,i+1):
            if l==0:
                print("*",end='')
            elif i>l:
                print(" ",end='')
            else:
                print("*",end='')
    print()
