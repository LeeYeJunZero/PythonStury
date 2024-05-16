list_1=[1, 2, 3, 4, 5, 1, 3]
list_2=[ ]
print(list_1)
print(list_2)

print(len(list_1)) #데이터의 크기를 센다
print(list_1)

list_1.append(100) #append = 리스트에 새로운 요소를 추가
print(list_1)
list_1 = [1, 2, 3, 9999, 5, 1, 3, 100]
list_2 = []

print(list_1)

list_1.remove(9999) # remove는 인자를 검색해서 삭제
#clear() - 리스트 전체 지우기
#pop() - pop은 부여된 인덱스를 지움 pop(2)라면 배열 0 1 2 3 4 5 중 2번 인덱스를 지움
print(list_1)

list_1.insert(0,777) #insert는 2개의 인자를 필요로 한다 0번 인덱스에 777의 값을 넣는다
print(list_1)

list_2 = list_1.copy() #list_1이라는 배열을 하나 더 만듦
print(list_2)

list = [1, 2, 3, 4, 5, 1, 3]
#1 2 3 4 5 1 3의 인자값이
for num in list :
    print(num)#모두 빠져나간 후 반복문 탈출
#시험에 나온다