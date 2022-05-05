# 다음 리스트 sports/ num을 활용해 스포트 종목과 팀원수가 번갈아
# 나오는 리스트를 만든 후 다음과 같이 출력하는 프로그램을작성하시오

sports=['축구','야구','농구','배구']
num=[11,9,5,6]

# 리스트 sports에 insert메소드로 직접 팀원수를 삽입
# 리스트 sports의 홀수 참조에 빈문자 ''을 insert메소드,로 삽입
# 위 결과 리스트에서 슬라이스 sports[1::2]에 num 대입

for i in range(4):
   sports.insert((2*i)+1,num[i])
print(sports)
#
# for i in range(4):
#     sports.insert()

sports.insert(2,"")
print(sports)