## 02 변수와 키워드, 대입 연산자.
type(3) # int
print(type(4/2)) # float
print(4/2) # float

## 키워드 확인 :  import keyword / keyword.kwlist
import keyword
print(keyword.kwlist) # 35

## 변수 선언 시 주의점
# 1. 앞에 숫자 못옴.
# 2. 키워드 사용 불가
# 3. 대소문자 구별된다 친구야...

## 한번에 여러 자료 대입
 # 다른 값 다른변수에 대입
a,b =5, 9
print(a,b)
 # 같은 값 다른변수에 한번에 대입
a=b=c=5

## 한번에 간단한 두변수의 교환 - 파이썬만 가능함 ㅋㅋ
a,b=5,6
b,a=a,b
print(a,b)

## 함수 divmod(a,b) : 몫 연산 // 와 나머지 연산 % 를 튜플 형태로 같이 출력
print(divmod(28,3)) # (9 ,1)

# 두개의 변수에 한줄에 집어넣어서 출력하기
a,b = divmod(28,3)
print(a,b) # 9 1


