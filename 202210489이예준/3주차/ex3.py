#파이썬에서 for문은 데이터 묶음에서
#데이터를 하나씩 끄집어내는 동안만 반복된다.

#while문은 조건, for문은 데이터 묶음 속에서 데이터가 있는 만큼만 나온다.

a = 5
i = 1
while i <= 9:
    print(f"{a} X {i} = {a*i}")
    i +=1

for i in range(1, 10):
    print(f"{a} X {i} = {a*i}")

#range는 배열 리스트를 만들어준다. range(3, 7)이라면 3~ -7까지 만들어준다.