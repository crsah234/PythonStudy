# 01 다양한 자료 : 문자열 과 수
# 작은 따옴표나 큰따옴표에 둘러져 있는 것
print('p')
print('python')

# 문자열 * 수 = 문자열 반복수
print("asd"*3) # asdasdasd

# print("asd"+3) # 오류남. 같은 형식의 더하기가 아니기때문

# 삼중 따옴표 : 문자열에입력된것처럼 두줄로 나옴
print('''asdfasdf
asdasd''')


## 정수, 실수, 실수 표현, type
print(type(15/2)) # <class 'float'>
print(type("asd")) # <class 'str'>
 # 실수 표현 e
print(3.4e-4) # 0.00034
print(3.4e4) # 34000.0

 # 복소수
a= 3+4j
print(a.conjugate()) # 3-4j
print(a.real) # 3.0
print(a.imag) # 4.0

## 연산 부분

 # 수의 몫 // : 나누기 결과를 넘지않는 가장 적은 정수 부분
print(8/5) # 1.6
print(8//5) # 1
print(-1.5//0.2) # -8 : -7.5를 넘지않는 가장 작은 정수이기때문.

 # 지수승 연산자 ** :
# 여러개 있을 경우 오른쪽에서부터 계산함 2**2**2 == 2의 (2의 2승)
print(3**4)# 81
print(2**2**3)# 64 가아니라 256

# 부호보다 먼저 계산됨.
print(-2**2) # -4, -(2의 2승)
print((-2)**2) # 4

 # _ 최근 결과의 특별한 저장 장소, 언더스코어(_) - 대화형에서 쓰임.

 # 여러 형식 print문에 출력
print("asdf", 1234,"asd")

 # *** 표현식 eval() : eval('expression') 자바문장이나 표현식의 결과를 반환해 주는 함수이다.
 # - 실행가능한 파이썬 문장의 문자열 실행
print(eval("1+2")) # 3
print(eval("'java'*3")) # javajavajava

