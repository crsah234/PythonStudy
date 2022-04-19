## 문자열의 표현
# 작은 따옴표, 큰 따옴표, 삼중 따옴표(여러줄 표현)

# 문자열 길이 반환 : len()
print(len('python')) # 6
## 문자열의 문자 참조
# 1. 변수 대입 후 참조
a ='python'
print(a[0])
print('python'[0])

# 2. 문자열에서 바로 참조
print('python'[-1])

# 3. len()을 이용한 참조. - len()-1 은 그 문자열의 마지막 원소값.
print('python'[len('python')-1]) # n

## 문자열 슬라이싱 str[start:end] == start~ end-1까지 반환함.
# start, end에는 양수, 음수, 0 , 빈칸도 가능함.
print('python'[-5:-1])

# [:] = 전체 출력하기
print('python'[:])


## str[start:end:step] : 문자사이의 간격을 step으로 조정 가능.
# step은 얼마나 몇문자씩 건너뛸건지임.
 # str[:] == str[::]= str[::1]
a='python'
print(a)
print(a[0:5:2])# pto

 # step이 음수인경우
# step에는 음수도 가능 -> 이때 start가 end보다 오른쪽에 위치한 첨자여야함. *****
# 간단하게 start와 end는 방향이 오른쪽에서 왼쪽으로 가야 스텝에서 음수부분이 가능하다.
print(a[::-2])
print(a[-1:-7:-1]) #


## ord('문자') chr(코드번호)
# ord('문자') : '문자'의 코드번호 반환
# chr(코드번호) : 코드번호의 문자 반환
print(ord('가')) # 44032
print(chr(44032)) #  가


## 이스케이프 문자
print('\\') # 역슬래쉬
print('\'') # '
print('\"') # "
print('\a') # 벨소리
print('\b') # 백스페이스(이전문자 지우기)
print('\n') # 새줄
print('\t') # tnvudoq
print('\N{DAGGER}') # † \N{name} : 유니코드의 이름
print('\uac00') # \uxxxx : 16비트 16진수 코드
print('\U0000AC00') # \Uxxxxxxxx : 32비트 16진수 코드
print('\0043') # \0xxx : 8진수의 코드 문자
print('\xff') # \xhh : 16진수의 코드 문자

## 내장 함수 min(), max()
 # 인자가 1개인 경우
# 문자열내에서 최소, 최댓값을 구하여 출력함
print(max('1234'), min('asd')) # 4

 # 인자가 2개 이상인 경우
#두 문자열 중 최대와 최소인 문자열을 반환한다.
print(max('asdf','asdff'))


