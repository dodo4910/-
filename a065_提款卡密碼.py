import sys

for num in sys.stdin:
    list_a = num.split()
    list_b = '' 
    for i in range(len(list_a[0])-1):
        list_b = list_b + str(abs(ord(list_a[0][i])-ord(list_a[0][i+1])))
    print(list_b)
