print("수 입력 : ")
num=int(input())


i=1

if num<=9:
    while i<=9:
        a=f"{num}X{i}={num*i}"
        print(a)
        i+=1
else :
        print("1~9 사이까지만 입력.")