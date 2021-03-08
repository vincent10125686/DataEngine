import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

def import_data(file):
    data=pd.read_csv('car_data.csv',encoding='gbk')
    print(data.shape)
    print(data.head())
    return data

#数据清洗
def data_clean(data):
    le=LabelEncoder
    train_x=data.iloc[:,1:]
    #规范化到[0,1]空间
    mxs=preprocessing.MinMaxScaler()
    train_x=mxs.fit_transform(train_x)
    return train_x

#KMeans聚类
def K_means(train_data,k):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(train_data)
    #predict_y=kms.predict(train_data)
    return kmeans

#手肘法分析
def sse(train_data):
    sse=[]
    for k in range(2,10):
        #KMeans算法
        kmeans=KMeans(n_clusters=k)
        kmeans.fit(train_data)
        predict_y=kmeans.predict(train_data)
        sse.append(kmeans.inertia_)
    x = range(2, 10)
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.plot(x, sse, 'o-')
    plt.show()

if __name__== '__main__':
    data=import_data("car_data.csv")
    train_x=data_clean(data)
    print(train_x)
    #通过手肘法确定k值
    sse(train_x)
    kmeans=K_means(train_x,5)
    #合并聚类结果，插入到原数据中
    result=pd.concat((data,pd.DataFrame(kmeans.labels_)),axis=1)
    result.rename({0:'聚类结果'},axis=1,inplace=True)
    print(result)
    # 打印分组情况
    for item in sorted(result["聚类结果"].unique()):
        print('第{}组: '.format(item + 1))
        # 筛选同组纪录
        record = result[result["聚类结果"] == item]
        print(record['地区'].values)
