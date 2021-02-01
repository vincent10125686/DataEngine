import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = {
    'Chinese': [68, 95, 98, 90, 80],
    'Math': [65, 76, 86, 88, 90],
    'English': [30, 98, 88, 77, 90]
}
df = DataFrame(data,
               index=['张飞', '关羽', '刘备', '典韦', '许褚'],
               columns=['Chinese', 'Math', 'English'])
df.rename(columns={'Chinese': '语文', 'Math': '数学', 'English': '英语'}, inplace=True)
# 输出5名同学成绩
print('五位同学的成绩如下：')
print(df)

data2 = {'平均成绩': df.mean(), '最小成绩': df.min(), '最大成绩': df.max(), '标准差': df.std(), '方差': df.var()}
df1 = DataFrame(data2)
# 输出各科平均成绩、最小成绩、最大成绩、方差和标准差
print('\n平均成绩、最小成绩、最大成绩、方差、标准差如下：')
print(df1)

df2=DataFrame(df.sum(axis=1),columns=['总分'])
df2= df2.sort_values('总分', ascending=False)
df2['排名']=np.arange(1, df2.shape[0]+1)
# 总成绩排序进行成绩输出
print("\n总成绩排序：")
print(df2)




