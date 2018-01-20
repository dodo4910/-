import sys
import math

for num in sys.stdin:
    a,b,c = map(int,num.split())

    if b**2-4*a*c == 0 :
        print("Two same roots x="+str(int(-b/(2*a))))
    elif b**2-4*a*c > 0 :
        x1 = round((-b + math.sqrt(b**2-4*a*c))/(2*a))
        x2 = round((-b - math.sqrt(b**2-4*a*c))/(2*a))
        print("Two different roots x1="+str(x1)+" , x2="+str(x2))

    else:
        print("No real root")
