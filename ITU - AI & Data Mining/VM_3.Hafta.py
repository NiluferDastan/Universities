"""
Created on Mon Oct 14 10:38:49 2024

@author: haticeoral
"""
# Veri Madenciliği
# Hafta 3

import pandas as pd
import seaborn as sbn

# seaborn modülü içerisindeki diamonds verisini kullanacağız
diamonds_df = sbn.load_dataset("diamonds") 

print(diamonds_df.info()) # veri seti hakkında bilgi verir.
# integer, float ve kategorik değişkenler mevcut.
# 53940 tane gözlem mevcut.

diamonds_df_nm = diamonds_df.select_dtypes(include = ['float64', 'int64'])
diamonds_df_nm = diamonds_df_nm.dropna() # Kayıp gözlemleri sildi.

diamonds_df_nm.head() # ilk 5 gözlemi verdi.
diamonds_df_nm.describe() # betimsel istatistikleri veirir.

sbn.boxplot(data = diamonds_df_nm[['x', 'y', 'z']], orient = 'h')
# Bu grafiği kaba yorumlarsak üç değişkende de aykırı değerler mevcut. Hem küçük değerlerde hem de 
# büyük değerlerde aykırı gözlemler mevcut. 

sbn.boxplot(x = diamonds_df_nm['carat'])
# Burada da aykırı değrler var. Fakat bu aykırı değerler tek taraflı. 2'den yüksek çok sayıda gözlem 
# mevcut.

sbn.boxplot(data = diamonds_df_nm[['depth', 'table']], orient = 'h')

# Bağımlı değişkenimiz olan price değişkeni için de boxplot çizdirelim:
sbn.boxplot(x = diamonds_df_nm['price'])

diamonds_df_xyz = diamonds_df_nm[['x', 'y', 'z']]
diamonds_df_xyz.head()

q1_x = diamonds_df_xyz['x'].quantile(0.25)
q3_x = diamonds_df_xyz['x'].quantile(0.75)
iqr_x = q3_x - q1_x
# x değişkeni için aykırı değerleri belirleyecek sınırları bulabiliriz.

lb_x = q1_x - 1.5 * iqr_x # Alt sınır
ub_x = q3_x + 1.5 * iqr_x # Üst sınır

# Şimdi y değişkeni için bakalım:
q1_y = diamonds_df_xyz['y'].quantile(0.25)
q3_y = diamonds_df_xyz['y'].quantile(0.75)
iqr_y = q3_y - q1_y

lb_y = q1_y - 1.5 * iqr_y # Alt sınır
ub_y = q3_y + 1.5 * iqr_y # Üst sınır

# Aykırı Gözlem Tespiti
# x değişkenine ilişkin gözlemleri ele aldığımızda hangi gözlemler aykırı sorgulatalım:
(diamonds_df_xyz['x'] < lb_x) | (diamonds_df_xyz['x'] > ub_x)
# True olanlar aykırı değer, False olanlar aykırı değil. En az biri gerçekleşiyorsa True verir.
# Bu sorgu sadece gözlemlerin aykırı olup olmadığını sorgulatıyor. Alt sınırdan düşük ya da üst 
# sınırdan büyük olduğunu söylemiyor.

# Bunun için öncelikle alt sınırdan küçük olan outlierları bulalım:
outlier_low_x = (diamonds_df_xyz['x'] < lb_x)
outlier_low_x.head(10)
# Kaç tane olduğunu bulalım:
diamonds_df_xyz['x'][outlier_low_x].count() # outlier_low_x sorgusunda True olanların sayısını verir.
# Peki bu 8 gözlem hangileri:
diamonds_df_xyz['x'][outlier_low_x].index

# Şimdi de üst sınırdan büyük olan outlierları bulalım:
outlier_up_x = (diamonds_df_xyz['x'] > ub_x)
outlier_up_x.head(10)
diamonds_df_xyz['x'][outlier_up_x]
diamonds_df_xyz["x"][outlier_up_x].count() 
diamonds_df_xyz["x"][outlier_up_x].index

"""
ÖDEV: Bugün yapılanların aynısını bağımlı değişkeni Table olarak alarak yap.
"""

diamonds_df_tbl = diamonds_df_nm["table"]
diamonds_df_tbl.head()

Q1_tbl = diamonds_df_tbl.quantile(0.25)
Q3_tbl = diamonds_df_tbl.quantile(0.75)

lb_tbl = Q1_tbl - 1.5*Q3_tbl # 51.5
ub_tbl = Q1_tbl + 1.5*Q3_tbl #63.5
IQR_tbl = Q3_tbl-Q1_tbl

# AYKIRI GÖZLEM TESPİTİ
(diamonds_df_tbl < lb_tbl) | (diamonds_df_tbl > ub_tbl)
# true'lar aykırı değerleri false'lar aykırı gözlem olmadığını gösterir

outlier_low_tbl = (diamonds_df_tbl < lb_tbl)
outlier_low_tbl.head(10)

outlier_up_tbl = (diamonds_df_tbl > ub_tbl)
outlier_up_tbl.head(10)
outlier_up_tbl.tail(10)

diamonds_df_tbl[outlier_low_tbl]
diamonds_df_tbl[outlier_low_tbl].count() 
# xtable için küçük değerli aykırı gözlemlerin sayısını bulmuş oluruz 

# bunları yüksek değerli aykırı gözlemlerin sayısını ve indexini bulurken de kullanabiliriz.

diamonds_df_tbl[outlier_up_tbl]
diamonds_df_tbl[outlier_up_tbl].count()  

# hafta 3 2.ders
# SİLME

type(diamonds_df_tbl)
diamonds_df_tbl = pd.DataFrame(diamonds_df_tbl)
diamonds_df_tbl.shape

diamonds_df_tbl_withoutOutlier = diamonds_df_tbl[-((diamonds_df_tbl <(lb_tbl)) | 
                                                   (diamonds_df_tbl > (ub_tbl))).any(axis=1)]
diamonds_df_tbl_withoutOutlier.head()
diamonds_df_tbl_withoutOutlier.shape


# BASKILAMA

# aykırı değerleri max ya da min değerlere bskılayarak değerleri değiştiriyor
diamonds_df_tbl[outlier_low_tbl] = pd.DataFrame(diamonds_df_tbl[outlier_low_tbl])
type(diamonds_df_tbl[outlier_low_tbl])
diamonds_df_tbl[outlier_low_tbl] 

diamonds_df_tbl[outlier_up_tbl] = pd.DataFrame(diamonds_df_tbl[outlier_up_tbl])
type(diamonds_df_tbl[outlier_up_tbl])
diamonds_df_tbl[outlier_up_tbl] 

# EKSİK VERİ PROBLEMİ
# eksik veri giderme yöntemleri
# silme yöntemi , değer atama yöntemi

import numpy as np
arr00 = np.array([0,2,4,np.nan,6,8,np.nan,10,12])
arr01 = np.array([1,np.nan,3,5,7,np.nan,np.nan,9,11])
arr02 = np.array([np.nan,11,13,15,17,19,np.nan,21,29])
df00 = pd.DataFrame({"C1": arr00,
                     "C2": arr01,
                     "C3": arr02})
df00

# ilk aklımıza gelecek soru kayıp gözlem var mı? Ve buna bakacağız
df00.isnull() # true false olarak çıktı verir ( kayıp gözlem true, kayıp olmayanlar false olarak 
# döner)

df00.isnull().sum() # toplam kayıp gözlemleri verir.

df00.notnull() # kayıp olmayan gözlemleri buluruz (true false cinsinden)(kayıp olmayanlar true,
# kayıp gözlemler false olarak döner)

df00.notnull().sum() # toplam kayıp olmayan gözlemleri verir

df00[df00.isnull().any(axis=1)] 
# df00 da kayıp olan gözlemlerle ilgileniyoruz sütun bazında en az bir tane nan olan satırları 
# döndürdü.

df00[df00.notnull().all(axis=1)]  # hiç bir kayıp gözlemi olmayan satırları getirir.

df00[df00["C1"].notnull() & df00["C2"].notnull() & df00["C3"].notnull()]
df00.dropna() # Yukarıdaki işlemleri dropna ile kısa sürede elde edip kayp gözlemlerden
# kurtulabiliriz.

df01 = df00.copy() # orjinal veriyi bozmamak için copy yaptık.
df01

df01.dropna(inplace= True) 
df01
#inplace argümanı dropna fonksiyonunda varsayılan olarak çalışır false ile çalıştırılınca 
# orjinali bozulmaz true ile bozulur.
