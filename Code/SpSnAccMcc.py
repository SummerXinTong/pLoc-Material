#!/usr/bin/env python
# coding: utf-8

# In[2]:

'''
    Caculate Sp,Sn,Acc,MCC
    
'''

# In[3]:


import pandas as pd
import csv
import os
import math
def CaculateSpSnAccMCC(file_name,m):   
    # 读文件
    df = pd.read_csv(file_name,header=None)
    # 读取数据个数
    n = len(df)
    
    TP = [0] * m
    FN = [0] * m
    TN = [0] * m
    FP = [0] * m
    sample_num = 0 # 样本总数
    
    # 类别
    # 读取每行的 真实数据 和 预测数据 得到相对应的集合 并按公式计算
    for i in range(n):
        true = set(df.iloc[i,0].strip('[]').split(','))# 真实值的集合
        predict = set(df.iloc[i,1].strip('[]').split(',')) # 预测值的集合 
        predict = {j for j in predict if str.isdigit(j)} # 因为预测集合可能存在空值，因此需要筛选出空值的集合
        # 集合元素从字符串变成整型
        true_sets = {int(a) for a in true } 
        predict_sets = {int(b) for b in predict}
        for ii in true_sets:
            if ii in predict_sets:
                TP[ii] = TP[ii] + 1
            else:
                FN[ii] = FN[ii] + 1
        for jj in range(m):
            if jj not in true_sets:
                if jj not in predict_sets:
                    TN[jj] = TN[jj] + 1
                else:
                    FP[jj] = FP[jj] + 1
    # 根据公式，分别计算
    for i in range(m):
        SN = TP[i]/(TP[i]+FN[i])
        SP = TN[i]/(TN[i]+FP[i])
        ACC = (TP[i]+TN[i])/(TP[i]+TN[i]+FP[i]+FN[i])
        a = (TN[i]+FN[i])*(TN[i]+FP[i])*(TP[i]+FN[i])*(TP[i]+FP[i])
        if a == 0:
            MCC = -1
        else:
            MCC = (TP[i]*TN[i] - FP[i]*FN[i])/math.sqrt((TN[i]+FN[i])*(TN[i]+FP[i])*(TP[i]+FN[i])*(TP[i]+FP[i]))
    
        data_line = [i,SN,SP,ACC,MCC]
        # 获取要写入csv的行
        # 需要写入的csv文件地址
        csv_output = 'C://Users//87173//Desktop/snspaccmcc.csv'
        with open(csv_output,'a+',newline='') as file:
            csv_write = csv.writer(file)
            csv_write.writerow(data_line)


# In[ ]:


# pLoc-mHum-RAKEL
m = 14
mHum_path_3106 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Lab//Data//pLoc-mHum//x_3106//pLoc-mHum_rakel_k_9_x_3106.csv'
CaculateSpSnAccMCC(mHum_path_3106,m)


# In[ ]:


# pLoc-mGneg-RAKEL
m = 8
mGneg_path_1392 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Lab//Data//pLoc-mGneg//x_1392//pLoc-mGneg_rakel_k_6_x_1392.csv'
CaculateSpSnAccMCC(mGneg_path_1392,m)


# In[ ]:


# pLoc-mEuk-RAKEL
mEuk_path_7766 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Lab//Data//pLoc-mEuk//x_7766//pLoc-mEuk_rakel_k_8_x_7766.csv'
CaculateSpSnAccMCC(mEuk_path_7766,m)


# In[ ]:


# pLoc-mAnimal-RAKEL
m = 20
mAnimal_path_3919 = 'C://Users//87173//Documents//ZnCu_Document//BaiduNetdiskWorkspace//Lab//Data//pLoc-mAnimal//x_3919//pLoc-mAnimal_rakel_k_8_x_3919.csv'
CaculateSpSnAccMCC(mAnimal_path_3919,m)

