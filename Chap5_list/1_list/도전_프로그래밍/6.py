# 다음 중첩된 리스트를 for문으로 행과 열을 맞춰 항목을 출력한 후
# 다시 행과 열이 바뀐 형태를 for문으로 출력하는 프로그램ㅇ르 작성하시오
m=[[1,2],[3,4],[5,6],[7,8]]


for i in range(len(m)):
    for a in range(len(m[0])):
        print("%2d"%(m[i][a]), end="")
    print()
    # 1 2
    # 3 4
    # 5 6
    # 7 8
for i in range(len(m[0])):
    for a in range(len(m)):
        print("%2d"%(m[a][i]), end="")
    print()

    # 1 3 5 7
    # 2 4 6 8