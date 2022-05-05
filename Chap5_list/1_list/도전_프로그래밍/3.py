# 문자열 helloPython! 으로 리스트를 만들어
# 부분 리스트 참조인 슬라이스를 위한 3개의 정수를 표준입력으로 받은 후
# 슬라이스 결과를 출력하는 프로그램

l1=list("helloPython!")
more = True
while more:
    print("+012345678901")
    print(" hellopython!")
    print("-210987654321")
    a =int(input("start 입력 : "))
    b=int(input("end 입력 : "))
    c=int(input("step 입력 : "))
    if a==0 and b==0 and c==0:
        more= False
    else :
        print(l1[a:b:c])

else:
    print("종료".center(20,"*"))

