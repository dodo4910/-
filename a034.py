import sys
for text in sys.stdin:
    print(bin(int(text)).replace("0b",""))
