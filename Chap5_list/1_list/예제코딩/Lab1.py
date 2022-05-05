# 스포츠 종목과 팀원 수를 리스트로 적절히 출력
# 실행결과 :
# 축구 : 11명 야구 :9명 농구 : 5명 배구 : 6명
sports=['축구','야구','농구','배구']
num=[11,9,5,6]

## 두 리스트로 출력
for i in range(len(sports)):
    print("%s : %d명"%(sports[i],num[i]),end=" ")
# 축구 : 11명 야구 : 9명 농구 : 5명 배구 : 6명
print()
## 2차원 리스트로 출력
snum=[sports,num]
for i in range(len(snum[0])):
    print("%s : %d명"%(snum[0][i],snum[1][i]),end=" ")
print()
## 다른 구조의 2차원 리스트 생성을 컴프리헨션으로 처리
snum2=[[sports[i],num[i]] for i in range(len(sports))]
# print(snum2) # [['축구', 11], ['야구', 9], ['농구', 5], ['배구', 6]]
for i in range(len(snum2)):
    print("%s : %d명"%(snum2[i][0],snum2[i][1]), end=" ")
