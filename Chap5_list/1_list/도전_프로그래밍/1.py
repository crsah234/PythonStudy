# 1~99까지의 난수 10개로 리스트를 만든후
# 리스트와 정렬된 리스트
# 그리고 내림차순으로 정렬된 역순 리스트를 출력하세요

from random import randint
a=[randint(0,100) for a in range(10) ]
b=sorted(a)
c= sorted(a,reverse=True)
print(a)
print(b)
print(c)

# [47, 70, 86, 60, 78, 22, 35, 39, 74, 79]
# [22, 35, 39, 47, 60, 70, 74, 78, 79, 86]
# [86, 79, 78, 74, 70, 60, 47, 39, 35, 22]