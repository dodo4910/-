import sys
for text in sys.stdin:
    print(eval(text.replace("/","//"))) #因除法有小數會影響，不然可以直接用eval直接處理
