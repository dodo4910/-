import sys
for text in sys.stdin:
    text1=""	
    num = len(text)
    # 讀入文章
    for i in range(num):
        text1 += chr(ord(text[i])-7)

    print(text1)
