import sys

for num in sys.stdin:
    a=[]
    for i in range(int(num)):
        a += [input()]
    result = []
    result = sorted(tuple(a))
    for text in result:
    	print(text)
