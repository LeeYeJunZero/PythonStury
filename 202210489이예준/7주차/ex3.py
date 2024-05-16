a = int(input("숫자입력: "))
b = 0

for i in range(2, a):
    if a%i==0:
        b=1
if b==1 or a==1 or a==0:
    print("소수아님")
else:
    print("소수맞음")
