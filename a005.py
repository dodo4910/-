import sys
row_num = int(input())
while(row_num>0):
		for num in sys.stdin:
				a,b,c,d = map(int,num.split())

				if (b - a)==(d - c):
				print(a,b,c,d,2*d-c)
				else:
				print(a,b,c,d,d*(d/c))
				
		row_num = row_num -1
