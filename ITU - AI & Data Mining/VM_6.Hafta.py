"""
Created on Mon Nov  4 10:33:22 2024

@author: haticeoral
"""
# Veri Madenciliği
# Hafta 6

import pandas as pd
housing = pd.read_csv("Housing.csv")

dt = housing.copy()23


# Kategorik değişkenlerin isimlerinden oluşan bir liste oluşturalım:
dt.info()
binary_vals = ["mainroad", "guestroom", "basement", 
               "hotwaterheating", "airconditioning", "prefarea"]

# Şimdi bu iki seviyeli kategorik değişkenlerin seviyelerini 0 ve 1 olarak belirleyen fonksiyonu 
# yazalım:
def binary_map(x):
    return x.map({"yes": 1,
                  "no": 0})

# Verideki kategorik değişkenlere bu fonksiyonu uygulayalım:
dt[binary_vals] = dt[binary_vals].apply(binary_map)
# Artık yes'ler yerine 1, no'lar yerine 0 yazıyor.

# Şimdi 3 kategoriye sahip kategorik değişken için dummy değişken tanımlayalım. 3 kategoriye sahip
# bir değişken için 2 tane dummy değişken oluşturulmalıdır. Sebebi ise 3 kategoriden ikisini
# biliyorsanız üçünüyü bilmenize gerek yok mantığıdır.
dt["furnishingstatus"].unique() # unique(), bütün değerleri tekrarsız bir şekilde döndürür.
status = pd.get_dummies(dt["furnishingstatus"], drop_first=True)
# drop_first = True, ilk kategoriyi dışarıda bırakır.

# Şimdi dt housing verisi ile iki değişkenli status verisini sütun bazlı birleştirelim:
dt = pd.concat([dt, status], axis = 1)

# Artık furnishingstatus değişkenine ihtiyacımız yok.
dt.drop(["furnishingstatus"], axis = 1, inplace = True)
# Sütun bazlı silme işlemi yapması için axis = 1 yazıldı.
# Bu işlemin dt versinde tanımlaması için inplace = True yazıldı.

# Şimdi train ve test verilerini ayıralım:
from sklearn.model_selection import train_test_split
h_DF_Train, h_DF_Test = train_test_split(dt, train_size=0.7, test_size=0.3, random_state = 1907)

# Bağımsız değişkenlerimizin ölçekleri farklı olduğu için analize başlayamayız. Öncelikle veriyi
# analize hazır hale getirmemiz gerek.

# min-max scaler ile değişkenlerdeki gözlemleri 0 ve 1 aralığında ölçeklendiririz. 
# min_max_scaler işlemi uyglayacak bir araç hazırlayalım ki her defasında bu işlemi çağırmak kolay
# olsun:
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

# Farklı olduğunu düşündüğümüz değişkenlere yani sayısal değişkenlere bu scaler işlemi yaptıralım:
dt.info()
numeric_vals = ["area", "bedrooms", "bathrooms", "stories", "parking", "price"]

# Ölçeklendirme yaparken fit etme işlemi train set üzerinden yapılır.
h_DF_Train[numeric_vals] = scaler.fit_transform(h_DF_Train[numeric_vals])
h_DF_Test[numeric_vals] = scaler.fit_transform(h_DF_Test[numeric_vals])

# Bağımlı ve bağımsız değişkenleri ayıralım:
h_y_Train = h_DF_Train.pop("price")
# Bu işlemden sonra train sete baktığımızda artık price değişkeni yok.
h_x_Train = h_DF_Train

h_y_Test = h_DF_Test.pop("price")
# Bu işlemden sonra test sete baktığımızda artık price değişkeni yok.
h_x_Test = h_DF_Test

# Bu şekilde veri analize uygun hale geldi.
# Fakat çok fazla bağımsız değişkeni olan verilerde başka bir sorun daha çıkabilir. Bu sorun da 
# bağımsız değişkenlerin tamamını kullanmak zorunda olup olmadığımızdır.

# Bu verideki 13 değişkenin tamamını kullanmak zorunda mıyım değil miyim?
# Ya da daha az bağımsız değişken ile analizimi yapabilir miyim?
# Elemem gereken değişkenler var mı?

# Öz yinelemeli eleminasyon yöntemi ile değişken sayısına karar verilir. Maximum kaç değişken
# alacağımıza bizim karar vermemiz gerekir.

# RFE, özellik seçimi için kullanılan bir tekniktir. Özellik seçimi modelin performansını
# iyileştirmek, aşırı uyumu (overfitting) önlemek ve eğitim süresini kısaltmak amacıyla gereksiz
# veya anlamlı olmayan özellikleri (değişkenleri) veriden çıkarmak için yapılan bir işlemdir.

from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

# Bir lineer regresyon modeli oluşturalım:
lm_RFE = LinearRegression()
# Modeli x'lere karşılık y'lerle fit edelim:
lm_RFE.fit(h_x_Train, h_y_Train)

# Şimdi bu fit edilmiş model üzerinden RFE işlemi yapalım yani 10 bağımsız değişken seçelim:
rfe = RFE(lm_RFE, n_features_to_select=10)

rfe = rfe.fit(h_x_Train, h_y_Train)
list(zip(h_x_Train.columns, rfe.support_, rfe.ranking_)) # Hangi değişkenlerin modelde olduğuna
# dair bir liste verir.
# Toplamda 13 değişken var. 10 tanesinde 1 var. Çünkü tahminleri 10 değişken ile yaptı.
# Bu modelde işe yaramadığını düşündüğü modele dahil etmediği 3 değişken var.

# Tahminlerimizi bu 10 değişken ile elde edebiliriz.

y_pred_Train = rfe.predict(h_x_Train)
y_pred_Train
# Toplamda eğitim kümesindeki gözlem sayısı kadar tahmin yaptık yani 381 tane.

y_pred_Test = rfe.predict(h_x_Test)
y_pred_Test
# Toplam 164 gözlem

# ÖDEV1: Hazır fonksiyonları kullanmadan R^2, MSE ve MAPE değerlerini eğitim ve test kümeleri için 
# bulduran fonksiyonu yazınız. min_max döünüşümü, değerleri 0 ve 1 arasında yapıyor. Değerlerin 0
# içermesi MAPE değerinin sonsuz olmasına neden oluyor. Bu nedenle elde edilen dönüştürülmüş 
# değerleri geri dönüştürmek (ters dönüşüm yapmak) gerek. Yani öncelikle ters dönüşüm yapmamız
# gerek. (x-minx/maxx-minx)


# İlgili modelin farklı özelliklerini barındıran parametreye hiperparametre denir.
# Şimdi de 6 hiperparametre değeri ile deneyelim:
rfe1 = RFE(lm_RFE, n_features_to_select=6)
rfe1 = rfe1.fit(h_x_Train, h_y_Train)
list(zip(h_x_Train.columns, rfe1.support_, rfe1.ranking_))

# 6 değişken aldığımızda area, bathrooms, stories, hotwaterheating, airconditioning, parking
# değişkenlerini kullanır.

# Kaç değişkenin kullanılması gerektiğiyle ilgili bilgi almak isteyebiliriz.

# Cross validationla farklı değişken kombinasyonu yapıp en iyi değişken sayısını bulabiliriz.
len(h_x_Train.columns) # 13 sütun var. Maksimum 13 tane hiperparametre alabiliriz.

from sklearn.model_selection import cross_val_score, KFold, GridSearchCV

fold_CVGS = KFold(n_splits = 5, shuffle = True, random_state = 1907)

hyper_params_CVGS = [{'n_features_to_select': list(range(1, 14))}]
hyper_params_CVGS

# Model belirleyelim:
lm_CVGS = LinearRegression()
lm_CVGS.fit(h_x_Train, h_y_Train)
rfe_CVGS = RFE(lm_CVGS)

# GridSearch uygulayalım:
model_CVGS = GridSearchCV(estimator = rfe_CVGS,
                          param_grid = hyper_params_CVGS,
                          scoring = 'r2',
                          cv = fold_CVGS,
                          verbose  = 1,
                          return_train_score = True)

model_CVGS.fit(h_x_Train, h_y_Train)
# k = 5 aldı ve her birinde 13 tane denem yapıyor yani 5*13'ten 65 tane çözümleme yapıyor.

# En iyi değişken sayısını elde edelim:
model_CVGS.best_params_

# En iyi değişken sayısı için R^2 skorunu bulalım:
model_CVGS.best_score_

# İlgili sonuçları dataframe'e çevirelim:
result_CVGS = pd.DataFrame(model_CVGS.cv_results_)
result_CVGS

# Sonuçların görselleştirilmesi
import matplotlib.pyplot as plt
plt.figure(figsize=(16, 6));

plt.plot(result_CVGS['param_n_features_to_select'], result_CVGS['mean_test_score']);
plt.plot(result_CVGS['param_n_features_to_select'], result_CVGS['mean_train_score']);
plt.xlabel("number of features");
plt.ylabel("r-squared");
plt.title("optimal number of features");
plt.legend(["test score","train score"], loc= "upper left");
# kodları toplu çalıştır.

# Nihai Model
n_features_optimal =  12
lm_final = LinearRegression()
lm_final.fit(h_x_Train,h_y_Train)

rfe_final = RFE(lm_final,n_features_to_select=n_features_optimal)
rfe_final = rfe_final.fit(h_x_Train,h_y_Train)

# test kümesi için tahminler ve hata
import sklearn
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
y_pred_Test_final = lm_final.predict(h_x_Test)
r2 = sklearn.metrics.r2_score(h_y_Test, y_pred_Test_final)
mae= sklearn.metrics.mean_absolute_error(h_y_Test,y_pred_Test_final)
mse= sklearn.metrics.mean_squared_error(h_y_Test,y_pred_Test_final)
rmse= sklearn.metrics.mean_squared_error(h_y_Test,y_pred_Test_final)
print(r2,mae,mse,rmse)


# ÖDEV2: 12 değişkenli olacak şekilde rfe'yi (10 ve 6'yı biz belirledik ama cv ile en uygun 12 
# olduğunu gördük) 12 ile cv yapıp ordan hata ölçümlerini hesapla. Hazır kod ile yapabilirsin.

