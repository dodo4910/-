import sys
import math
for num in sys.stdin:
    a,b = map(int,num.split())
    print(math.gcd(a,b))
