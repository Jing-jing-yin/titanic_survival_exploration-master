# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 20:53:07 2018

@author: Jing
"""
import numpy as np
import pandas as pd

df=pd.read_csv('titanic_data.csv') #读取整个表格数据
df=df.iloc[0:20] #按索引提取前20行数值
#print(df)
#print(df.shape)#获取维度
#print(df.info())#获取数据表的基本信息
#print(df.dtypes)#获取每列的类型
#print(df['Parch'].dtype)#获取某列数据的格式
#print(df.isnull())#判断是否为空值
#print(df['Age'].unique())#获取某一列的唯一值
#print(df.values)#查看数据表的值
#print(df.columns)#查看列名称
#print(df.head())#默认前十行数据
print(df)#默认前十行数据
#print(df.tail())#默认后十行数据
print(df.dropna())
#print(df.fillna(0)) #用0 填充缺失的值
#print(df)#默认前十行数据
#print(df['Age'].values)#查看数据某列的值
#print(df['Age'].fillna(df['Age'].mean()))
#print(df.fillna({'Age':df['Age'].mean(),'Cabin':20}))
#print(df['Age'].values)#查看数据某列的值



