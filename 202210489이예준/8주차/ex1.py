def scorelist(total, score):
    n=len(score)#배열은 len으로 길이를 측정 할 수 있다
    print(total)
    print(score)#score는 배열
    print(total/n)
    #함수로 선언

score= []
n = int(input("학생 수"))

total = 0
for i in range(0, n):
    jumsu = int(input("[%d]영어성적:" % (i+1)))
    total += jumsu
    score.append(jumsu)

scorelist(total, score)
#호출하는 인자는 실인자라고 부른다. (argument)
#파이썬은 실인자 지정 방법이 두개 있으며 하나는 위치 지정과 키워드 인자가 존재함
#키워드 인자는 함수가 정의된 키워드를 가져와 사용함
