dict_1 = {'name': '이예준' , 'birth' : 2003, 'addr' : 'KR'}
print(dict_1)
print(dict_1['birth'])

dict_1['weight'] = 60.5
dict_1['family'] = ['부', '모', '누']
print(dict_1)

dict_1.update({'weight':89.1, 'hobby':['게임', '청소']})#딕셔너리 안에는 또다른 딕셔너리가 들어갈 수 있음
print(dict_1)#업데이트는 딕셔너리 형태를 취허고 있음 추가시키는게 아닌 요소를 합쳐준다.

dict_1['hobby']= ['헬스', '프리웨이트'] # 딕셔너리에서 대입 연산자는 추가의 의미도 있지만 수정하는 의미도 갖고있다.
print(dict_1)

del dict_1['weight'] # 요소가 삭제됨
del dict_1['birth']
del dict_1['addr']
print(dict_1)