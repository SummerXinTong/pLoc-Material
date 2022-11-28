#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import os


# In[6]:


'''
    对 csv文件 得到的  真实数据 预测数据 进行处理 得到每个蛋白质两个数据集合
    返回两个集合

'''
# m是类别
def caculator(file_name,m):
    
    df = pd.read_csv(file_name,header=None)
    # 读取数据个数
    n = len(df)
    # 和
    aiming_sum = 0
    coverage_sum = 0
    ab_false_sum = 0
    ab_true_sum = 0
    accuracy_sum = 0
    
    # 读取每行的 真实数据 和 预测数据 得到相对应的集合 并按公式计算
    for i in range(n):
        #true与predict换了位置
        true = set(df.iloc[i,0].strip('[]').split(','))# 真实值的集合
        predict = set(df.iloc[i,1].strip('[]').split(',')) # 预测值的集合 
        predict = {j for j in predict if str.isdigit(j)} # 因为预测集合可能存在空值，因此需要筛选出空值的集合
        # 集合元素从字符串变成整型
        true_sets = {int(a) for a in true } 
        predict_sets = {int(b) for b in predict}
        # 交集
        tp_inter = true_sets & predict_sets
        # 并集
        tp_union = true_sets | predict_sets
        if(true_sets == predict_sets):
            ab_true_sum += 1
        # 并集 与 交集  的 差
        tp_Differ = tp_union - tp_inter

        if len(predict_sets) == 0:
            aiming_sum = aiming_sum + 0
        else:
            aiming_sum = aiming_sum + len(tp_inter) / len(predict_sets)

        coverage_sum = coverage_sum + len(tp_inter) / len(true_sets)
        ab_false_sum = ab_false_sum + (len(tp_Differ) / m)
        accuracy_sum = accuracy_sum + len(tp_inter)/len(tp_union)
    
    # 计算Aiming
    aiming = aiming_sum / n
    
    # 计算coverage
    coverage = coverage_sum / n
    
    # 计算Absolute true
    ab_true = ab_true_sum / n
    
    # 计算Absolute false
    ab_false = ab_false_sum / n
    
    # 计Accuracy
    accuracy = accuracy_sum / n

    return [aiming,coverage,ab_true,ab_false,accuracy]


# In[7]:


def runing(ran_path):
    # 目录下的所有文件
    ran_list = os.listdir(ran_path)
    # 目录下的所有csv文件
    csv_list = [i for i in ran_list if i.endswith('.csv')]
    for filecsv in csv_list:
        # 获取k,x
        name = filecsv.strip('.csv').split('_')
        k = int(name[-3])
        x = int(name[-1])
        data_line_1 = [k,x]
        # 计算 三个值
        csv_path = ran_path + "//" + filecsv
        data_line_2 = caculator(csv_path,m)
        data_line = [k,x,data_line_2[0],data_line_2[1],data_line_2[2],data_line_2[3],data_line_2[4]]
        # 获取要写入csv的行
        # 需要写入的csv文件地址
        csv_output = 'C://Users//87173//Desktop//conabc.csv'
        with open(csv_output,'a+',newline='') as file:
            csv_write = csv.writer(file)
            csv_write.writerow(data_line)


# In[ ]:


# pLoc-mHum-RAKEL
m = 14
mHum_path_3106 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Data//data//pLoc-mHum//x_3106'
runing(mHum_path_3106)


# In[9]:


# pLoc-mGneg-RAKEL
m = 8
mGneg_path_1392 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Data//data//pLoc-mGneg//x_1392'
runing(mGneg_path_1392)


# In[ ]:


# pLoc-mEuk-RAKEL
m = 22
mEuk_path_7766 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Data//data//pLoc-mEuk//x_7766'
runing(mEuk_path_7766)


# In[ ]:


# pLoc-mAnimal-RAKEL
m = 20
mAnimal_path_3919 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Data//data//pLoc-mAnimal//x_3919'
runing(mAnimal_path_3919)

