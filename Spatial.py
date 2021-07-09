A=[[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
#[[1,2,3],[4,5,6],[7,8,9]]

top=0
left=0
bottom=len(A)-1
right=len(A[0])-1
d=0 #0: 1:left,2:
while(top<=bottom and left<=right):
    #print("in while")
    if(d==0):
        for i in range(left,right+1):
            print(A[top][i],end=" ")
        top+=1
    if(d==1):
        for i in range(top,bottom+1):
            print(A[i][right],end=" ")
        right=right-1
    if(d==2):
        for i in range(right,left-1,-1):
            print(A[bottom][i],end=" ")
        bottom=bottom-1
    if(d==3):
        for i in range(bottom,top-1,-1):
            print(A[i][left],end=" ")
        left=left+1
    d=(d+1)%4
    
