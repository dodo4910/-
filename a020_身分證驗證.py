import sys

dict1={'A':10,'J':18,'S':26,'B':11,'K':19,'T':27,'C':12,'L':20,'U':28,
       'D':13,'M':21,'V':29,'E':14,'N':22,'W':32,'F':15,'O':35,'X':30,
       'Y':31,'G':16,'H':17,'Q':24,'Z':33,'I':34,'R':25,'P':23 }
 
for test_input in sys.stdin: 
    test_input = test_input.replace("\r\n","")
    en = ""
    total=0
    h = 8
    
    for i in range(1,9):
        total = total + int(test_input[i])*h
        h-=1
        
    en = str(dict1[test_input[0].upper()]) 
 
    if (int(en[1])*9 + int(en[0]) + total +int(test_input[9]) ) % 10 == 0 :
        print('real')
    else:
        print('fake')
