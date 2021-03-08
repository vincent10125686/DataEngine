import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_url(url):
    # 得到页面的内容
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(url, headers=headers, timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    #soup = BeautifulSoup(content, 'html.parser',from_encoding='utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    #无需增加from_encoding='utf-8'，会报错
    return soup

def get_df(soup):
    # 找到完整的投诉信息框
    temp = soup.find('div', class_="tslb_b")
    #创建DataFrame
    columns_id= ['投诉编号', '投诉品牌', '投诉车系', '投诉车型', '问题简述', '典型问题', '投诉时间', '投诉状态']
    df=pd.DataFrame(columns=columns_id)
    tr_list=temp.find_all('tr')
    for i in tr_list:
        #获取表格内‘td’开头数据，去除表头，并转换成文本
        td_list=i.find_all('td')
        dic={}
        if len(td_list)>0:
            id, brand, car_model, type, details, problem, datetime, status = [td_list[x].text for x in range(8)]
            dic['投诉编号'] = id
            dic['投诉品牌'] = brand
            dic['投诉车系'] = car_model
            dic['投诉车型'] = type
            dic['问题简述'] = details
            dic['典型问题'] = problem
            dic['投诉时间'] = datetime
            dic['投诉状态'] = status
            df=df.append(dic,ignore_index=True)
    return df
result=pd.DataFrame(columns = ['投诉编号','投诉品牌','投诉车系','投诉车型','问题简述','典型问题','投诉时间','投诉状态'])
url_base='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0'
#确定爬取所需的页数
page_num=5
for i in range(1,page_num+1):
    url=url_base+str(i)+ '.shtml'
    soup=get_url(url)
    df=get_df(soup)
    result=result.append(df,ignore_index=True)
result.to_excel('car_complain.xlsx',index=False)
print('文件存储完成')






