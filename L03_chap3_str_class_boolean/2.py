# replace() - 문자열을 바꿔 반환하는 메소드
 # 값자체를 바꾸기보다는 바꿔서 보여줌
str="자바는 인기 있는 언어 중 하나이다."
print(str) # 자바는 인기 있는 언어 중 하나이다
print(str.replace('자바는','c언어는')) # c언어는 인기 있는 언어 중 하나이다

 # replace(a,b,count) : count가 있으면 그 수만큼 변환함.
print('a a a'.replace('a','b',2)) # b b a

## 활용 예제
# 소수형태의 수의 모든 자릿수의 합을 구하여라
# ex : 123.123 = 12
# a=input(" 실수 입력")# 1.123
# num=a.replace('.','') #
# print(num) # 1123
# 이걸이용, 참조를 하여 모두더하면끝

# count() - 문자나 부분문자열의 출현횟수를 알려줌
print(str.count('중')) # 1

# join() - 문자와 문자 사이에 문자열을 삽입하는 메소드
# a.join(b) -> a를 b문자열 중간중간에 삽입함.
print('.'.join(str)) #  자.바.는. .인.기. .있.는. .언.어. .중. .하.나.이.다..

# find(), index() - 찾는 부분 문자열 첨자 반환, 정확히는 시작하는 첨자 반환
# 둘의 차이점 : index()는 찾는 게없을시 오류가 나고, find()는 -1 반환시켜줌.
str='자바 c 파이썬 코틀린'
print(str.find('코틀린')) # 9 반환

# rfind() , rindex() 는 오른쪽으로부터 찾아 첨자를 반환한다
print(str.rfind('코')) # 9 반환

## 공백을 기준으로 분류된 단어 2개를 역순으로 출력하기 사과 배라 -> 배라 사과 -> 라배 과사
a=input("공백을 기준으로 단어 2개 입력하기(예 : 사과 배라")
num=a.find(' ')
a1=a[:num]
a2=a[num+1:]
print(a1,a2) # 배라 사과
print(a1[::-1], a2[::-1]) # 라배 과사

# split() -문자열을 여러 문자열로 나누는 메소드
print(str.split()) # 공백으로 str문자열 나누기 # ['자바', 'c', '파이썬', '코틀린']
print('a,b,c,d,e'.split(',')) # ,으로 문자열 나누기 # ['a', 'b', 'c', 'd', 'e']

# split을 이용한 input 활용하기.
# 4개의 수를 입력하는것을 한번에 받기
a,b,c,d=input('빈칸을 기준으로 숫자 4개 입력').split(' ') # 1 2 3 4

##  영문자 알파벳 변환 관련 메소드
# upper() - 대문자로 변경
print('asdf'.upper())

#  lower() - 소문자로 변경
print('ASD'.lower())

# capitalize() - 첫 문자만 대문자로 변환
print('asd df sdf'.capitalize())

# title() - 단어마다 첫 문자를 대문자로 변환해 반환
print('asd sdf sdf'.title())

# swapcase() - 소문자와 대문자를 서로 변환해 반환
print('asdf AASD'.swapcase())

# ljust() , rjust() - 폭을 지정하고, 왼, 오른쪽으로 정렬하는 메소드
print('python'.ljust(10,'/'))
print('python'.ljust(10))
print('python'.rjust(10,'/'))
print('python'.rjust(10))

# zfill() - 폭을 지정하고, 문자열을 제외한 남는 자리에 제로 0을 채워놓는 메소드
print('234'.zfill(5))

##### 강의에 나온 두가지 : center() / strip()

# center() - 폭을 지정하고 중앙에 배치하는 메소
 # 두번째 인자없이
print('asd'.center(30)) #              asd              /
 # 두번째 인자 있이
print('asd'.center(30,'*')) # *************asd**************

# strip() - 문자열 앞뒤의 특정 문자들을 제거하는 메소드
 # 오른쪽 제거 - rstrip()
print('asd    '.rstrip())

 # 왼쪽 제거 - lstrip()
print('   asd'.lstrip())




