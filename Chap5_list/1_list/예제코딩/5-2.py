## 일반적인 리스트 저장 및 출력하기
coffee=['에스프레소','아메리카노','카페라떼']
for i in coffee:
    print(i)
    # 에스프레소
    # 아메리카노
    # 카페라떼

## 중앙정렬로 리스트 출력
# coffee 위에것 사용
for ca in coffee:
    print("{:^15s}".format(ca))  # 15칸중 중앙에 정렬
    print("{:<15s}".format(ca))  # 15칸중 오른쪽 정렬
    print("{:*<15s}".format(ca))  # 15칸중 왼쪽정렬,빈칸 *로 채움