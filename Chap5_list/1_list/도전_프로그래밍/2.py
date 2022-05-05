# 영한 사전과 같이 한글과 영어에 대응되는 튜플 korean과 english 를 만든 후,
# 표준 입력으로 한글을 입력받아 영어를 출력하는 프로그램을 작성하시오
k=1,2,3,4,5
e='a','b','c','d','e'

more=True
while more:
    a=int(input("1,2,3,4,5중 하나 입력"))
    if a in k:
        print("%s"%(e[k.index(a)]))
    else:
        more =False
