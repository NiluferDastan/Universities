"""
Created on Mon Oct 21 10:20:38 2024

@author: haticeoral
"""
# Veri Madenciliği
# Hafta 4

import numpy as np
import pandas as pd

arr00 = np.array([0, 2, 4, np.nan, 6, 8, np.nan, 10, 12])
arr01 = np.array([1, np.nan, 3, 5, 7, np.nan, np.nan, 9, 11])
arr02 = np.array([np.nan, 11, 13, 15, 17, 19, np.nan, 21, 23])
df00 = pd.DataFrame({"C1": arr00,
                     "C2": arr01,
                     "C3": arr02})

# df00 verisini bozmamak içn kopyalayalım:
df01 = df00.copy()

df01.dropna() # Eksik gözlemlerin bulunduğu sütunları sildi.
df01.dropna(inplace = True)

# df00 verisini tekrar kopyalayalım
df02 = df00.copy()

df02["C1"] # Elde edilen çıktı bir data frame değil bir seridir.

df02["C1"].mean() # C1 sütununun ortalamasını verir.

df02["C1"].fillna(df02["C1"].mean()) # C1 sütunundaki kayıp gözlemleri C1 sütununun ortalaması
# ile doldurduk.

# Eğer 0 ile dodlurmak isteseydik:
df02["C1"].fillna(0)

# Biz tek bir sütun üzerinde ilgili sütundaki kayıp gözlemleri ortalaması ile doldurduk. Bu işlemi
# bütün sütunlar için bir fonksiyon ile yaptırabiliriz.

df02.apply(lambda x: x.fillna(x.mean())) # Varsayılan axis=0'dır. Bu sütun bazında demek.

# Eksik gözlemleri görmek için görsel yöntemlerle de inceleyebiliriz.
# !pip install missingno

#import missingno as msno
#msno.bar(df02)python -m pip install certifi

#msno.matrix(df02) # Bu grafikte beyaz kısımlar missing gözlemleri; siyah kısımlar ise kayıp olmayan
# gözlemleri temsil eder. Yandaki çizgi de 3 ve 0 değerleri arsında zik zak çiziyor. 3'en başlıyor
# çünkü başlangıçta üç sütunun da son değeri kayıp olmayan gözlemdir.

# Şimdi seaborn paketindeki planet veri setini çağıralım:
import seaborn as sbn
planetsDf = sbn.load_dataset("planets")

planetsDf.head(10) # ilk 10 satırını verir.

# Bu veriye de aynı işemleri uygulayalım
df = planetsDf.copy()
df.isnull().sum() # Her bir sürun için kayıp gözlem sayısını verir.

# Kayıp gözlemleri grafik ile inceleyelim:
msno.matrix(df) # Birinde beyaz varken diğerinde de sürekli beyaz çıkıyor olması bu iki dğeişkenin
# ilişikili olduğunu belirtebilir.
# Bazı değişkenlerde kayıp gözlem olması diğer değişkende de kayıp gözlem olmasına sebep olabilir.

msno.heatmap(df) # Kayıp gözlemlerin değişkenler arasında ilşkisini gösterir. Yani değişkenlerin
# kayıp gözleme sahip olmaları konusunda birbirini etkilemelerini (ilişkili olmalarını) gösterir.

# Şimdi kendi ürettiğimiz veriye dönelim:
df02.dropna() # Her bir satırda en az bir sütunda kayıp gözlem varsa o satırı siler.
df02.dropna(how = "all") # Her bir satırda bütün sütunlarda NaN olan satırları bulup onları siler.

# Sütunlar üzerinden NaN kontrolü yaptırmak istersek yani 1.sütuna bak en az 1 NaN görüyorsan 
# dışla; 2.sütuna bak en az 1 NaN görüyorsan dışla şeklinde:
df02.dropna(axis = 1)

# Herhangi bir değişkenin sütunlarının bütün değerleri NaN ise o sütunları dışla:
df02.dropna(axis = 1, how = "all")

# Mesela df02'ye bütün değerleri NaN olan bir sütun ekleyelim:
df02["silgitsin"] = np.nan
df02
df02.dropna(axis = 1, how = "all")
df02.dropna(axis = 1, how = "all", inplace = True)

# Bazı kayıp gözlemleri kategorilerine uygun olacak şekilde kategorilerine uygun olacak
# doldurmalıyız.

# Yapay veri seti oluşturalım:
arr03 = np.array([10, 14, 48, np.nan, 36, 68, np.nan, 10, 12])
arr04 = np.array([10, np.nan, 30, 51, 72, np.nan, np.nan, 9, 11])
arr05 = np.array([np.nan, 11, 130, 150, 170, 190, np.nan, 21, 23])
arr06 = np.array(["KD1", "KD1", "KD2", "KD2", "KD2",
                  "KD2", "KD2", "KD1", "KD1"])
df03 = pd.DataFrame({"C1": arr03,
                     "C2": arr04,
                     "C3": arr05,
                     "CKD": arr06})

# C1 değişkeni için ortalama bulalım:
df03["C1"].mean()

# Ortalama 28 çıktı. 28'in bu değişken için uygun olup olmadığını bulmak için:
df03.groupby("CKD")["C1"].mean()
# İlgili kategorik değişkenin kategorileri bakımından bu dataframe'i ayrıştırmış olduk. Kategorik 
# değişkenin KD1 ve KD2 değerleri için ortalamaları ayrı ayrı hesaplattı.
# 28 değerini ikisine de uymadığını gördük.

# Şimdi diğer sütunlardaki NaN değerlerini kategorik değişkenin kategorileri bakımından ayrılmış
# ortalama değerleri ile dolduralım.
df03["C1"].fillna(df03.groupby("CKD")["C1"].transform("mean"))

# Ya kayıp gözlemimiz kategorik bir değişkende ise:
arr07 = np.array([10, 14, 48, np.NaN, 36, 68, np.NaN, 10, 12])
arr08 = np.array(["KD1", np.NaN, "KD2", "KD2",
                  "KD2", "KD2", "KD2", "KD1", "KD1"], dtype = object)
df04 = pd.DataFrame({"C1": arr07, "CKD": arr08})

# Kayıp kategorik değişkenler için kayıp gözlemleri değişkenin modu ile doldurabiliriz.
df04["CKD"].mode()

df04["CKD"].fillna(df04["CKD"].mode()) 
# Bu kodu çalıştırınca doldurma işlemi yapmadı. Çünkü kategorik olduğundan index belirtmemiz 
# gereliyor.
df04["CKD"].mode()[0]
df04["CKD"].fillna(df04["CKD"].mode()[0])

df04["CKD"].fillna(method = "bfill")
# method parametresi kayıp gözlmeleri ne ile dolduracağımız hakkında bilgi verir.
# bfill KD2 ile doldurdu.
df04["CKD"].fillna(method = "ffill")
# ffill KD1 ile doldurdu.

# DÖNÜŞÜMLER
# Yeni bir data frame oluşturalım:
arr09 = np.array([10, 2, 5, 6, 1, 4, 12])
arr10 = np.array([11, 3, 6, 7, 19, 11, 13])
arr11 = np.array([12, 24, 10, 12, 28, 20, 16])
df05 = pd.DataFrame({"C1": arr09,
                     "C2": arr10,
                     "C3": arr11})
df05

# Standart normal dağılıma dönüşüm
from sklearn import preprocessing

preprocessing.scale(df05) 
# Verideki her değişkeni kendi ortalama ve standart sapmalarını kullanarak standartize eder.

# df05'in standartize edilmiş halini bir data frame formatına dönüştürelim:
df05std = pd.DataFrame(preprocessing.scale(df05))
# Satır ve sütun isimlerini değiştirebiliriz. Biz bir şey belirmtediğimiz için kendisi otomatik
# indexler verdi.

# Bu normal dağılıma dönüşümü nasıl yatığını nasıl anlarız. Bildiğimiz yöntemi mi uyguladı?

df05std.mean()
# Baktığımızda her sütunun ortlaması 0'a çok yakın. 0 kabul edilebilir.

df05std.std()
# Sütunların varyansları 1 çok yakın değerler çıktı.

# Yani scale() methodu ortalama 0 ve standart sapma 1 olacak şekilde standartalaştırma işlemi 
# yaptı. Bu değişkenlerin alacağı değerler -3sigma ve +3sigma aralığındadır.

# Min-Max dönüşümü 
# Verinin en küçük değerleri 0 en büyük değerleri 1'e eşit yapan dönüşüm.
scaler00 = preprocessing.MinMaxScaler(feature_range=(0,1))
# Yukarıdaki kod satırı bir ölçeklendirici hazırlar. Bu ölçeklendiriciyi bir nesnede tutup o nesne
# üzerinden tanmladığımız bu ölçeklendirmeyi istediğimiz yerde daha rahat kullanabiliriz.

scaler00.fit_transform(df05) 
# x_yeni = (x_gözlem - min(x)) / (max(x) - min(x))  şeklinde hesaplıyor.

# Değerleri 0 ve 1 arasındaki değerlerden oluşan bu yeni veriyi data frame yapısına dönüştürelim:
df05scaler00 = pd.DataFrame(scaler00.fit_transform(df05))

# Şimdi bir veri seti import edelim:
housing = pd.read_csv("Housing.csv")
dt = housing.copy()

dt.head() # İlk beş gözlem
len(dt.index) # verini 545 gözlemden oluştuğu bilgisini verir. 545 değerini kullanmak için
# bu şekilde çekeriz.
dt.isnull().sum() # Her bir değişken için kayıp gözlem sayısını verir.
dt.info() # Her bir değişkeni kayıp gözlemi olup olmadığını ve türünü verir.
# Bu veride hem sayısal hem de kategorik değşkenler var.

# Biz fiyat tahmini oluşturacağız. Price ve area değişkenlerini kullanacağız.
focused_Vs = housing.loc[:, ["area", "price"]]
# loc fonksiyonu sütunların indexleri ile çalışır. İki değişkenden oluşan bir data frame
# oluşturmuş olduk.
focused_Vs

# Şimdi bu dataframe üzerinden bir doğrusal regresyon modeli oluşturup oluşturamayacağımıza 
# bakacağız. Bunun için saçılım grafiğine bakarız.

import seaborn as sbn
sbn.regplot(x = "area",
            y = "price",
            data = focused_Vs,
            fit_reg=True)

# fit_reg parametresinin varsayılan değeri True'dur. fit_reg= True değeri regresyon doğrusunu
# çizdirirken False dendiğinde regresyon doğrusu çizdirilmez.

# Regresyon doğrusunun etrafindaki gölgelik güven aralığını gösterir.

# Hem saçılım grafiğini hem de ilgili değişkenlerin grafiğini birlikte görmek için:
sbn.jointplot(x = "area",
              y = "price",
              data = focused_Vs,
              kind="reg")