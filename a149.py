import sys

num_sum = []
for num in sys.stdin:
    num_sum += num.split()

for j in range(1,int(num_sum[0])+1):
	total = 1
	for i in range(len(num_sum[j])):
		total = int(num_sum[j][i])*total
	print(total)
