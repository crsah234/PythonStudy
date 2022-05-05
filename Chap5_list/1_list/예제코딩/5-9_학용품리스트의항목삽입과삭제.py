item=['연필','볼펜']
print(item)

# 연필 1개와 볼펜 세자루 삽입
item.insert(1,2)
item.insert(3,3)

# 맨뒤에 지우개, 1개 삽입
item.insert(4,'지우개')
item.insert(5,1)
print(item) # ['연필', 2, '볼펜', 3, '지우개', 1]

# 연필 2자루 삭제
print(item.pop(1)) #첨자 1항목 삭제
item.remove('연필') # '연필' 항목 삭제
del item[2:] # 지우개와 수 품목 삭제

print(item) # ['볼펜', 3]



