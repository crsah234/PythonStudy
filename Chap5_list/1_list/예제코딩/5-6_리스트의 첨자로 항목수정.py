top=['bts','볼빨간사춘기','BTS','blackPink','태연']
top[1]='소울워커'
print(top) # ['bts', '소울워커', 'BTS', 'blackPink', '태연']

top.append('울면') # ['bts', '소울워커', 'BTS', 'blackPink', '태연', '울면']
a=input("입력하시오") # asd
# 입력한것으로 변경하기
top[top.index('bts')]=a
print(top) # ['asd', '소울워커', 'BTS', 'blackPink', '태연']


