while True:
    print('음료목록 1. 오렌지주스(100원), 2.커피(200원), 3.콜라(300원)')
    
    money = int(input("동전을 넣으세요 : "))
    coffe = int(input("음료를 고르세요 : "))
    if coffe == 1:
        if money>=100: 
            cell=money-100 
            print('오렌지주스가 곧 제공됩니다.')
            print('거스름돈은 {}원 입니다.'.format())
        else:
            print('잔액이 부족합니다.')
    elif coffe == 2:
        if money>=200: 
            cell=money-200 
            print('zjvl가 곧 제공됩니다.')
            print('거스름돈은 {}원 입니다.'.format(cell))
        else:
            print('잔액이 부족합니다.')
    elif coffe == 3:
        if money>=300: 
            cellmain=money-300 
            print('콜라 곧 제공됩니다.')
            print('거스름돈은 {}원 입니다.'.format(cell))
        else:
            print('잔액이 부족합니다.')
    else:
        print("없는 메뉴.")