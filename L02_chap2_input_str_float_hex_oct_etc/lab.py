# 가장 먼저 변환할 수가 2, 8, 16 중 무엇인 지 입력받기
# 그럼 다음, 표준 입력한 수의 2진수,8 진수 16진수 출력

a=input("입력할수의 진법 기수 입력 : ") # 2,8,16
b=int(input("표준입력(2,8,16진수형태)"),int(a))
print("2진수 출력:",bin(b))
print("8진수 출력:",oct(b))
print("10진수 출력:",int(b))
print("16진수 출력:",hex(b))



# float.fromhex(str) : 16진수 형태의 str을 실수로 변환하는 함수.
print(float.fromhex('e.1')) # 14.0625