#本題主要考精確度，故需熟練Decimal用法
import sys
from decimal import * 

for content in sys.stdin:
    num_list = content.replace("\n"," ").split()
    loop_use = int(len(num_list)/3)
    
    for i in range(loop_use):
        a,b,N = map(float,num_list[3*i:3+3*i])
        getcontext().prec = len(str(a))+int(N) ＃設定精確度
        getcontext().rounding = ROUND_DOWN ＃避免下行的format發生四捨五入
        print(format(Decimal(a)/Decimal(b),"."+str(int(N))+"f"))
