### 2.1 부분참조- 슬라이싱

# 리스트[start:end:step]
a=list('123456')
print(a[1::2]) #['2', '4', '6']

# 역순 첨자
print(a[-1:-4:-2]) # ['6', '4']
print(a[-1:]) # 6이 나옴. **** step이 없을 경우에는 왼쪽에서부터 진행하는것같음. step이 있어야 오른쪽에서 왼쪽으로 진행함.


# 음수와 정수 둘다 이용한 첨자
print(a[2:-1]) # ['3', '4', '5']

### 2.2 리스트의 부분 수정

sports=['풋살','족구','비치사커','농구','야구']
# sports[0:2]='축구' # ['축', '구', '비치사커', '농구', '야구']
sports[0:2]=['농구장']
print(sports) # ['농구장', '비치사커', '농구', '야구']

# 리스트 슬라이스에 슬라이스 대입
sports[1:3]=sports[2:3] # ['농구장', '비치사커', '농구', '야구']   - > ['농구장', '농구', '야구']
print(sports)

### 2.3 리스트의 항목 삽입과 삭제

## 리스트의 항목 삽입 insert(첨자,항목)
kpop=[]
kpop.insert(0,'a')
kpop.insert(0,'b')
print(kpop) # ['b', 'a']

## 항목 삭제 remove()
kpop.remove('a')
print(kpop) # ['b']

## 항목 띄우고 삭제 pop(첨자)
# 첨자가 없을 시 맨 마지막 첨자 해당함.
print(kpop.pop()) # b
print(kpop) # []

## 문장 del에 의한 항목, 변수 삭제

# 항목 삭제
kpop=[1,2,3,4]
del kpop[1]
print(kpop) # [1, 3, 4]

# 슬라이스로 일부분 삭제
del kpop[1:]
print(kpop) # [1]

# del 변수 : 메모리에서 변수 자체를 제거한다.
del kpop
# print(kpop) 메모리에서 삭제가되어 오류가 남.

## 리스트의 모든 항목만을 제거해 빈리스트로 만들기 clear()
kpop=[1,2,3,4]
kpop.clear()
print(kpop) # []



### 2.4 리스트의 추가, 연결과 반복

## 리스트에 리스트를 추가하는 메소드 extend()
day=['월','화','수']
# day.extend(['목','금'])
day2=['목','금']
day.extend(day2)
print(day) # ['월', '화', '수', '목', '금']

## 리스트끼리 서로 연결하는 +연산자
korean=['불고기','설렁탕']
chinese=["짜장면",'기스면']
food=korean+chinese
print(food)

### 2.5 리스트 항목의 순서와 정렬

##리스트의 항목순서를 뒤집는 reverse() - 원래 리스트 변화함
#바꿔서 보여주는게 아닌 전체를 뒤집음.
l='abcde'
wlist=list(l)
wlist.reverse()
print(wlist) # ['e', 'd', 'c', 'b', 'a']

## 리스트의 항목 순서를 정렬하는 메소드 sort() - 원래 리스트 변화함
# sort()는 오름차순으로
# sort(reverse=True) 는 내림차순으로 정렬함

wklist=[1,3,2,4,5,6]
wklist.sort()
print(wklist) # [1, 2, 3, 4, 5, 6]

wklist.sort(reverse=True)
print(wklist) # [6, 5, 4, 3, 2, 1]

## 리스트 항목의 순서를 정렬한 리스트 반환하는 내장 함수 sorted() - 원래리스트 변화 없음

w=[1,3,2,4]
w2=sorted(w)
print(w2) # [1, 2, 3, 4]
print(w) # [1, 3, 2, 4]


### 2.6 리스트 컴프리헨션
##조건을 만족하는 항목으로 리스트를 간결히 생성함.
# 변수=[항목연산식 /  for 항목 in 시퀀스 / if 조건식]
# 컴프리헨션 안하고 초기화 할시
even =[]
for i in range(2,11,2):
    even.append(i)

print(even) # [2, 4, 6, 8, 10]

# 컴프리헨션
even= [i for i in range(2,11,2)]
print(even) # [2, 4, 6, 8, 10]

## 조건이 있는 컴프리헨션
# 일반적으로 할때
odd=[]
for i in range(10):
    if i%2==1:
        odd.append(i)
print(odd) # [1, 3, 5, 7, 9]

# 컴프리헨션
even=[i for i in range(10) if i%2==1]
print(odd) # [1, 3, 5, 7, 9]

### 2.7 리스트 대입과 복사
## 리스트 대입에 의한 동일 리스트의 공유
f1=[1,2,3,4]
f2=f1
## 같은 것을 가리키게됨
# 같은 메모리 공간을 사용하는 리스트를 공유하게됨
# 즉 f2와 f1은 하나의 같은 리스트!!!!
f2.pop() # f1 f2둘다 영향줌
print(f1) # [1, 2, 3]
print(f2) # [1, 2, 3]

## 리스트의 깊은 복사에 의한 대입으로 새로운 리스트 생성
# 그저 대입연산자로하면 같은 메모리를 가리키게됨
# 원소값만 같고 다른 메모리를 사용하려면
# 슬라이싱, copy, 또는 list()함수를 사용해야함
f1=[1,2,3,4]
f2=f1[:]
f3=f1.copy()
f4=list(f1)
f2.pop()
f3.pop(2)
f4.append('감')
print(f1,f2,f3,f4) # [1, 2, 3, 4] [1, 2, 3] [1, 2, 4] [1, 2, 3, 4, '감']

## 변수가 같은 메모리를 가리키는지 검사하는 is
print(f1 is f2) # False





