student=int(input("학생 수 입력 : "))
total = 0
for i in range(student):
    score=int(input("점수 입력"))
    total+=score
print(total)

num= total % student

print(num)