import sys
for text in sys.stdin:
    text1=""	
    num = len(text)
    # 讀入文章
    for i in range(num):
        text1 += chr(ord(text[i])-7)
        #在 python 裡面，字串是不允許變更，故需要重新創一空白string ，然後用加法的慢慢建立一個新的字串

    print(text1)
