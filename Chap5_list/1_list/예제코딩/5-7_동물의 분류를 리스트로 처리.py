animal=[['사자','코끼리'],'조류','어류']
bird=['새','참새']
fish=['갈치','붕어']
animal[1:]=[bird,fish]
print(animal)
#[['사자', '코끼리'], ['새', '참새'], ['갈치', '붕어']]

for lst in animal:
    for item in lst:
        print(item,end=' ')
    print()
print()
# 사자 코끼리
# 새 참새
# 갈치 붕어
# 위는 원소 개별로 출력

# 밑은 리스트출력
for a in animal:
    print(a)
    # ['사자', '코끼리']
    # ['새', '참새']
    # ['갈치', '붕어']