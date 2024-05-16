import md # 함수 하나만 임포트 할거라면 from md import isprime
print("10~20사이 소수 :")
for j in range(10, 20):
    if md.isPrime(j): # 사용할때 모듈이 앞에 와야함, 만약 함수 임포트라면 isprime(j)로 변경
        print(j)

#모듈 임포트는 임포트 +모듈 이름 작성하면 됨 import module
#모듈 내 특정 함수는 from 모듈이름 + 임포트 from module import() , ()

#모듈을 단축명으로 import
#import module as mde하면 mde로 사용 가능함S

#데이터프레임은 엑셀형태 행과 열을 가짐 