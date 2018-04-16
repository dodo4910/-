import sys
import datetime
import time

date1 = 0

for num in sys.stdin:
    a,b,c = map(int,num.split())
    
    if date1 == 0:
        date1 = datetime.date(a,b,c)
    else:
        print(abs((date1 - datetime.date(a,b,c)).days))
        date1 = 0
