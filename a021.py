import sys
for num in sys.stdin:
    print(int(eval(num.replace("/","//"))))
