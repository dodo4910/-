import sys

for num_str in sys.stdin:
    num = int(num_str)
    if num <= 10:
        print(num*6)
    elif num >= 11 and num <= 20:
        print((num-10)*2+10*6)
    elif num >= 21 and num < 40:
        print((num-20)*1+10*6+10*2)
    elif num >= 40:
        print(100)
