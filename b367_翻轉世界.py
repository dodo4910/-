import sys

a = int(input())
for i in range(a):
    temp1 = list(map(int,input().split()))
    h = int(temp1[0])
    w = int(temp1[1])
    list_a = [[0]*w for i in range(h)]
    list_b = [[0]*w for i in range(h)]
    for j in range(h):
        temp2 = list(map(int,input().split()))
        for k in range(w):
            list_a[j][k] = temp2[k]
            list_b[h-j-1][w-k-1] = temp2[k]
    if list_a == list_b:
        print('go forward')
    else:
        print('keep defending')
