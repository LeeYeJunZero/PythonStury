import pandas as pd

data = {'이름' : ['kim', 'park', 'Lee', 'ho'],
        '국어' :[90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88]}

df = pd.DataFrame(data)

print(df, end='\n\n')

sr_name = df['이름']
print(sr_name, end='\n\n')

score = df['이름']
print(df.loc[1:1], end='\n\n')

df.loc[df['이름']=='ho', '수학']=90
print(df, end='\n\n')

df.loc[3]=['oh', 100, 70, 80]
print(df, end='\n\n')

df=df.drop([2], axis=0)
print(df, end='\n\n')