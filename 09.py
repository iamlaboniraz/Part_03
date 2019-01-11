N = 5

middle_point  = int(N/2)+1

low=0
high=N-1
n=1
number=[[0 for x in range(N)] for y in range(N)]

for i in range(middle_point):
    for j in range(low,high+1):
        number[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        number[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        number[high][j]=n
        n=n+1
    for j in range(high-1,low,-1):
        number[j][low]=n
        n=n+1
    low=low+1
    high=high-1


for i in range(N):
    for j in range(N):
        print(number[i][j],end='\t')
    print()
