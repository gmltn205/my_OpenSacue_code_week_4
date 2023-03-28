#체인법을 구현하는 해시 클래스 ChainedHash의 사용

from enum import Enum
from chained_hash import ChainedHash

Menu=Enum('Menu',['추가','삭제','검색','덤프','종료'])#메뉴를 선언

def select_menu()->Menu:
    s=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep='  ',end='')
        n=int(input(' :  '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash=ChainedHash(13) #크기가 13인 해시 테이블 생성

while True:
    menu=select_menu()

    if menu==Menu.추가:
        key=int(input('추가 할 키를 입력 : '))
        val=input('추가 할 값을 입력 : ')
        if not hash.add(key,val):
            print('추가 실패했습니다')

    elif menu==Menu.삭제:
        key=int(input('삭제 할 키를 입력 : '))
        if not hash.remove(key):
            print('삭제를 실패했습니다.')

    elif menu==Menu.검색:
        key=int(input('검색 할 키를 입력 : '))
        t=hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색 할 데이터가 없습니다.')

    elif menu==Menu.덤프:
        hash.dump()

    else:
        break
    
