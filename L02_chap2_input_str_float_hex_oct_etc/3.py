## 자료의 표준 입력(input)과 자료 변환 함수(int(), float(), str())
# 입력받기 - input()
# a= input("입력하시오")
# print(a) # 입력한 값 출력됨
# input()으로 받은 값은 모두 str형태임. 따라서 활용시 형변환 필요

# 자료 변환 함수 str(), int(), float()
 # 출력값 : 각각의 형태
 # 인자값 :
    # str() :다드감
    # int() : 정수 형태의 문자열, 실수값
    # float() : 실수(정수도 가능), 실수 형태의 문자열(정수도 가능)

 # str() - 정수와 실수를 문자열로 변환하느데 주로 사용됨
print(str(345)) # int가 아닌 문자열 형태의 345

 # int() - 1. 정수형태의 문자열값을 정수로 / 실수값을 정수로 변환함
print(int("1234")) # 1234
print(int(3.45)) # int값 3으로 나옴

 # float() - 1. 실수 형태의 문자열값을 실수로 / 정수값을 실수로 변환함
print("1.234") # 1.234 type= float
print(1) # 1.0 type = float
print(float("1")) # 1.0됨. 정수도 실수에 포함되기 때문

# 변환 함수 str(), int(), float()의 오류 종류, 그리고 헷갈릴 만한 것 알아보기
# int('python') # 문자열내용이 정수가 아님
# int("6400i") # 문자열 내용에 정수로만 이루어져있는게 아님
# int("3.13123") # 문자열 내용이 정수가아님
# float("3.14123f") # 문자열 내용이 실수로만 이루어져있는게 아님
# int("0b11") # 10진수 형태가 아님
print(int(float("1.123"))) # 안에서 한번 걸러지기에 가능.


# 입력받은 값은 str. 따라서 다른 형태로 변환하여 활용하기
# a = input("실수 입력") # type(a)= str 따라서 형태를 변환해줘야함
# a= float(input("실수 입력")) # type(a) = float

## 16진수, 10진수, 8진수, 2진수와 활용
print(0b11) # 2진수로 인식하여 10진수 형태로 출력 ****
print(0x11) # 8진수로 인식하여 10진수 형태로 출력
print(0xaa) # 16진수로 인식하여 10진수 형태로 출력

# 10진수에서 각각의 진수로 변환 함수
 # - bin(), oct(), hex() - str형태로 출력
    # 인자값 : 10진수 형태 **
    # 출력값 : 문자열 형태 **
print(bin(7)) # 0b111
print(type(bin(7))) # type = str

# data = int(input("정수 입력 : "))
# print(hex(data)) # str형태값 16진수 값 출력
# print(bin(data))
# print(oct(data))

## int('정수'==strnum, 진법기수) 를 활용한 여러진수상수형태 문자열의 10진수 변환
 # strnum을 진법기수의 형태의 값으로 인식, 10진수로 출력.

 # int('strnum') & int('strnum',10) -  10진수 형태의 문자열을 10진수 로 변환
print(int('1234',10)) # 1234 출력

 # int('strnum',n) n= 2,8,16 : 진법기수의 맞는 형태로 문자열인식. 10진수로 출력
  # strnum은 0b11이든 11이든 n의 값에따라 인식함.
print("2진수형태의 값 인식 10진수로 출력 int('11',2) : ", int('11',2)) # 3
print('int("22",8)',int("22",8))
print("int('0b11',2): ",int('0b11',2))

 # int('strnum', 0) : strnum의 맨앞이 0b,0x,0o를 분류하여 자동으로 인식
print(int('0b1',0)) # 2진수로 인식
print(int('0x12',0)) # 16진수로 인식

# 16진수 입력으로 2진수, 8진수, 10진수, 16진수 출력
value=input("16진수 입력: ") #0x10 16진수 입력
data= int(value,16) # value를 16진수로 인식하고 10진수 형태로 data에 저장.
print('2진수 : ',bin(data))
print('8진수 : ',oct(data))
print('16진수 : ',hex(data))
