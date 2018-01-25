import sys
for num in sys.stdin:
    num = num.strip()
    if num == num[::-1]:
        print('yes')
    else:
        print('no')
