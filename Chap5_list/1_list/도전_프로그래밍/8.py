# 1~99까지 난수 10개로 리스트를 만든 후
# 다시 이 리스트를 튜플로 변환
# 다음과같이 정렬된 리스트와 합, 항목 수, 최대. 최소 평균을 출력하는 프로그램

from random import randint
a=list()
for i in range(10):
    a.append(randint(0,100))
print("리스트 : ",a)
t_a=tuple(a)
print("튜플 : ",t_a)
t_a_s=sorted(t_a)
print("튜플 정렬된 리스트:",t_a_s)
total=0
count=0
for i in a:
    count+=1
    total+=i
print("합 : %d, 항목 수 : %d"%(total,count))
print("최대 : %d, 최소 : %d, 평균 : %d"%(max(t_a),min(t_a),sum(t_a)/count))

# 리스트 :  [68, 24, 53, 54, 47, 63, 68, 65, 91, 64]
# 튜플 :  (68, 24, 53, 54, 47, 63, 68, 65, 91, 64)
# 튜플 정렬된 리스트: [24, 47, 53, 54, 63, 64, 65, 68, 68, 91]
# 합 : 597, 항목 수 : 10
# 최대 : 91, 최소 : 24, 평균 : 59