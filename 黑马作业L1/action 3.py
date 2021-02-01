import pandas as pd
import numpy as np

#导入数据
df = pd.read_csv('car_complain.csv')
# 拆分problem类型=>多个字段。
df= df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))


#数据清洗
def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
df['brand']=df['brand'].apply(f)

#总问题数
Problem_sum= df.groupby('brand')['id'].agg(['count']).sort_values('count', ascending=False)
Problem_sum.reset_index(inplace=True)

#车型问题总数
Car_model_problem=df.groupby('car_model')['id'].agg(['count']).sort_values('count', ascending=False)
Car_model_problem.reset_index(inplace=True)

#品牌的平均车型投诉
df2=df.groupby(['brand','car_model'])['id'].agg(['count'])
df2.reset_index(inplace=True)
#print(df2)
Car_problem_average=df2.groupby(['brand']).mean().sort_values('count', ascending = False)
Car_problem_average.reset_index(inplace=True)

print(Problem_sum)
print(Car_model_problem)
print(Car_problem_average)









