# 다음 중첩된 리스트 data에서 각 행과 열의 합을 리스트 rsum csum에 저장해 출력하시오
data=[[1,2,3],
      [4,5,6],
      [7,8,9]]
rsum=list()
csum=list()

for i in data:
      sum=0
      for a in i:
            sum+=a
      rsum.append(sum)
print(rsum)
# 00 10 20
# 01 11 21
# 02 12 22
for i in range(len(data)):
      sum=0
      for a in range(3):
            sum += data[a][i]
      csum.append(sum)
print(csum)