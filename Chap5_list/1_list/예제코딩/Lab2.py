# 햄버거 콤보 번호를 받아 주문 가격 표시
menu=('주문종료','올인원팩','투게더팩','트리오팩','패밀리팩')
price=0,6000,7000,8000,10000

msg= "주문할 콤보 번호와 수량을 계속 입력하세요!"
for i in range(len(menu)):
    msg+='\n\t %d %s'%(i,menu[i])
    if i!=0:
        msg+=' %5d 원 '%price[i]
msg+="\n >>"
more=True
total=0
while more:
    a = input(msg) # 안내 텍스트 나옴.
    if(a.count(" ")>0): # 번호와 수량 입력
        order,cnt=a.split()
        cnt=int(cnt)
    else:               # 번호만 입력
        order=a
    order= int(order)
    if order==0:
        print()
        print("주문 종료".center(20,'*'))
        more= False
    elif 1<=order<=4:
        print("%s, %d개 주문"%(menu[order],cnt))
        sub=price[order]+cnt
        total+=sub
        print("%s 주문 가격 %d, 총 가격 %d"%(menu[order],sub,total))
    else:
        print("모르겠어요 다시 주문하세요")
else:
    print("총 주문 가격 %d 원"%total)





