import pandas as pd

col_names = ['과목번호', '과목명', '강의실', '시간수']  # 열 이름 리스트 정의
list1 = [['C1', '인공지능개론', 'R1', 3],
          ['C2', '웃음치료', 'R2', 2],
          ['C3', '경영학', 'R3', 3],
          ['C4', '3D디자인', 'R4', 4],
          ['C5', '스포츠경영', 'R2', 2],
          ['C6', '예술의세계', 'R3', 1]
          ]

df = pd.DataFrame(list1, columns=col_names)  # 데이터프레임 생성
print(df)
print(df.head(3))
sr_name = df['과목명']
print(sr_name)
sr_two = df.loc[2]
print(sr_two)
cell_name=df.loc[2]['강의실']
print(cell_name)

df.to_csv("lecture.csv", header=True, index=False)

#행은 가로 열은 세로