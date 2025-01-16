"""
Created on Mon Nov 11 10:18:21 2024

@author: haticeoral
"""
# Veri Madenciliği
# Hafta 7

# VİZE ÖDEVİ: Veri bul. Veriye  önişleme, aykırı değer tespiti dışarıya atma ,kayıp gölzem varsa 
# kurtul, dummy değişken tanımlamaak gerekşyorsa tanımla, basit doğrusal, RFE, çoklu doğrusal,
# yapay sinir ağları analizleri yap.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV

hitters = pd.read_csv('Hitters.csv')
dt = hitters.copy()
# Bu veri beyzbol sprocularına ait bir veri.

# Veri Seti Düzenlemesi
dt = dt.dropna() 

dummyVariables = pd.get_dummies(dt[['League', 'Division', 'NewLeague']])

y = dt['Salary']
x_ = dt.drop(['Salary', 'League', 'Division', 'NewLeague'], axis = 1).astype('float64')
x = pd.concat([x_, dummyVariables[['League_N', 'Division_W', 'NewLeague_N']]], axis = 1)

# Veri Seti Bölünmesi
dt_x_Train, dt_x_Test, dt_y_Train, dt_y_Test = train_test_split(x, y,
                                                                test_size = 0.20,
                                                                random_state = 2017)

type(dt_y_Train)
dt_y_Train = np.array(dt_y_Train)
dt_y_Test = np.array(dt_y_Test)

# Veri Ölçeklendirme
from sklearn.preprocessing import StandardScaler

# Bir ölçeklendirme nesnesi oluşturalım:
scalerANN = StandardScaler()

# Ölçeklendirme nesnesi ile eğiitm ve test seti ölçeklendirilir:
dt_x_Train_scaled = scalerANN.fit_transform(dt_x_Train)
dt_x_Test_scaled = scalerANN.transform(dt_x_Test)

# Eğitim kümesindeki min ve max değerlerine bakarak scale işlemi yapılmalı. Bu nedenle fit işlemi
# eğitim verisi üzerinden yapılır. Test verisi değerlerini bilmediğiöizi varsayarak fit işlemi
# yapmadan dönüştürme yapılır.

# Output matrix conversion
dt_y_Train = dt_y_Train.reshape(-1, 1)
dt_y_Test = dt_y_Test.reshape(-1, 1)

# Ölçeklendirme nesnesi ile eğitim ve test seti ölçeklendirilir.
dt_y_Train_scaled = scalerANN.fit_transform(dt_y_Train)
dt_y_Test_scaled = scalerANN.transform(dt_y_Test)
# Ters dönüşüm sağlandıktan sonra hatalar bulunmalı. Aksi takdirde bir işe yaramaz.

# MODEL OLUŞTURMA
from sklearn.neural_network import MLPRegressor

aNN = MLPRegressor(random_state = 1907).fit(dt_x_Train_scaled, dt_y_Train_scaled)

?aNN # Modele ilişkin bilgilere ulaşabiliriz. Hperparametreler, varsayılan değerler vs.

dir(aNN) # Bazı özellikleri verir. Bu özelliklerden;

aNN.random_state
aNN.loss # hata kare fonksiyonunu verir.
aNN.loss_ # hata kare değerini verir.
aNN.hidden_layer_sizes # Gizli tabaka birim sayısı. 19*100 tane ağırlığı bulmaya çalışır.
aNN.n_features_in_  # Bağımsız değişken sayısı
aNN.n_iter_ # İterasyon sayısı

# Train set tahmini
y_pred_aNN_Train = aNN.predict(dt_x_Train_scaled)
y_pred_aNN_Train[0:10]
# Test set tahmini
y_pred_aNN_Test = aNN.predict(dt_x_Test_scaled)
y_pred_aNN_Test[0:10]
# Bu tahminler gerçek tahminler değil. Bu tahminlere ters dönüşüm yapmamız gerek. Kendi 
# ortalamasından farkı alıp standart sapmasına bölüyordu. Bizim de bu işlemin tersinin yapıp ters
# dönüşüm yapmamız gerek. Ödevde de gerçek tahminleri bulmalıyız.

gercektahmin_ann_train = y_pred_aNN_Train * np.std(y_pred_aNN_Train) + np.mean(y_pred_aNN_Train)
gercektahmin_ann_train[0:10]
gercektahmin_ann_test = y_pred_aNN_Test * np.std(y_pred_aNN_Test) + np.mean(y_pred_aNN_Test)
gercektahmin_ann_test[0:10]

# Modeldeki metrikleri gerçek tahminler üzerinden hesaplatacağız.
# Eğitim seti hatası
from sklearn.metrics import mean_squared_error, r2_score

RMSE_aNN_Train = np.sqrt(mean_squared_error(dt_y_Train_scaled, gercektahmin_ann_train))
r2_aNN_Train = r2_score(dt_y_Train_scaled, gercektahmin_ann_train)
print(RMSE_aNN_Train, r2_aNN_Train)

# Test seti hatası
RMSE_aNN_Test = np.sqrt(mean_squared_error(dt_y_Test_scaled, gercektahmin_ann_test))
r2_aNN_Test = r2_score(dt_y_Test_scaled, gercektahmin_ann_test)
print(RMSE_aNN_Test, r2_aNN_Test)

# GridSearch Optimizasyonu

# Kaç gizli tabaka kullanılacak (hidden_layer_sizes) ve alpha hiperparametrelerini buldurmamız
# lazım.

# Bu hiper parametreler için bir sözlük nesnesi oluşturalım:
aNN_params = {'alpha': [0.1, 0.01, 0.02, 0.001, 0.0001],
              'hidden_layer_sizes': [(10,20), (5,5), (100,100)]}

# 3 tane gizli tabaka seçeneği oluşturduk.
# 5*3 = 15 farklı kombinasyon için çözümleme gerçekleştirilecek.

# Varsayılan hiperparametre değerleriye bir model oluşturalım:
aNNfCV = MLPRegressor(random_state=1907)

# K = 5 Fold CV oluşturulan parametre ızgarası oluşturalım:
aNN_CVGS = GridSearchCV(aNNfCV, aNN_params,
                        cv = 5,
                        n_jobs = -1,
                        verbose = 2).fit(dt_x_Train_scaled, dt_y_Train_scaled)

aNN_CVGS.best_params_

# En iyi hiperparametreleri kullanalım:
aNN_Best = MLPRegressor(alpha=0.1,
                        hidden_layer_sizes = (100,100),
                        random_state= 1907).fit(dt_x_Train_scaled, dt_y_Train_scaled)


# Train set tahmini
y_pred_aNN_Best_Train = aNN_Best.predict(dt_x_Train_scaled)
y_pred_aNN_Best_Train[0:10]

# Test set tahmini
y_pred_aNN_Best_Test = aNN_Best.predict(dt_x_Test_scaled)
y_pred_aNN_Best_Test[0:10]

# Elde ettiğimiz bu tahminler scale edilmiş eğitim ve test seti üzerindeki tahminlerdir. Yani bizim
# gerçek tahminlerimiz değildir. Bu nedenle modelin metriklerine bakmak için öncelikle bu tahminlere
# ters dönüşüm yaparak gerçek tahminleri elde etmeliyiz.

gercektahmin_ann_best_train = y_pred_aNN_Best_Train * np.std(y_pred_aNN_Best_Train) + np.mean(y_pred_aNN_Best_Train)
gercektahmin_ann_best_train[0:10]

gercektahmin_ann_best_test = y_pred_aNN_Best_Test * np.std(y_pred_aNN_Best_Test) + np.mean(y_pred_aNN_Best_Test)
gercektahmin_ann_best_test[0:10]

# Şimdi bu gerçek tahminler için metrikleri hesaplayalım:
# Train seti için
RMSE_aNN_Best_Train = np.sqrt(mean_squared_error(dt_y_Train_scaled, gercektahmin_ann_best_train))
r2_aNN_Best_Train = r2_score(dt_y_Train_scaled, gercektahmin_ann_best_train)
print(RMSE_aNN_Best_Train, r2_aNN_Best_Train)

# Test seti için
RMSE_aNN_Best_Test = np.sqrt(mean_squared_error(dt_y_Test_scaled, gercektahmin_ann_best_test))
r2_aNN_Best_Test = r2_score(dt_y_Test_scaled, gercektahmin_ann_best_test)
print(RMSE_aNN_Best_Test, r2_aNN_Best_Test)

# Burada en GSCV modelinin tahmin performansı daha kötü çıktı. Bunun sebebi hiperparametre
# değerlerini elimizle girdiğimiz için olabilir.
# Eğer varsayılan hiperparametre değerleri daha iyi sonuç veriyorsa, varsayılan hiperparametre 
# değerlerini bulup o değerleri de bu GSCV modeline eklersek bu model daha iyi bir tahmin 
# performansı gösterebilir.

# K EN YAKIN KOMŞU ANALİZİ
from sklearn.neighbors import KNeighborsRegressor

# Model Oluşturma ve Uydurma
kNN = KNeighborsRegressor().fit(dt_x_Train, dt_y_Train)

?kNN # bu işlemi her modele yapmamızı tavisye ediyor çünkü model hakkına hiperparametreleri veriyor.
dir(kNN)

kNN.metric
kNN.neighbors
kNN.weights

y_pred_knn_Train = kNN.predict(dt_x_Train)
y_pred_knn_Train[0:10]

y_pred_knn_Test = kNN.predict(dt_x_Test)
y_pred_knn_Test[0:10]

# kNN modeli standartlaştırılmış train ve test verileri üzerinden değil orijinal train ve test
# verileri üzerinden eğitilmiştir. Bu nedenle tahminler de gerçek train ve test set üzerinden 
# oluşturulmuş olup gerçek tahminlerdir.
# Bu tahminler için modelin metriklerini bulalım:
RMSE_knn_Train = np.sqrt(mean_squared_error(dt_y_Train, y_pred_knn_Train))
r2_knn_Train = r2_score(dt_y_Train, y_pred_knn_Train)
print(RMSE_knn_Train, r2_knn_Train)

# Test seti hatası
RMSE_knn_Test = np.sqrt(mean_squared_error(dt_y_Test, y_pred_knn_Test))
r2_knn_Test = r2_score(dt_y_Test, y_pred_knn_Test)
print(RMSE_knn_Test, r2_knn_Test)

kNN_params = {'n_neighbors': np.arange(1, 30, 1)}
kNN = KNeighborsRegressor()

kNN_CVGS = GridSearchCV(kNN, kNN_params, cv = 10).fit(dt_x_Train, dt_y_Train)

# Tüm uydurulmuş alternatif modeller içerisinden en iyi olanın parametresi:
kNN_CVGS.best_params_

# Tüm uydurulmuş alternatif modeller içerisinden en iyi olanın parametreleri ile model uyduralım:
kNN_Tuned_CVGS = KNeighborsRegressor(n_neighbors= kNN_CVGS.best_params_['n_neighbors']).fit(dt_x_Train, dt_y_Train)

# Tüm uydurulmuş alternatif modeller içerisinden en iyi olanın parametreleri ile uydurulan modele
# ilişkin 
# Train seti tahminleri:
y_pred_knn_tuned_CVGS_train = kNN_Tuned_CVGS.predict(dt_x_Train)
# Test seti tahminleri:
y_pred_knn_tuned_CVGS_test = kNN_Tuned_CVGS.predict(dt_x_Test)

# Bu gerçek tahminlerin için modelin train set üzerinden metrikleri:
RMSE_knn_tuned_CVGS_Train = np.sqrt(mean_squared_error(dt_y_Train, y_pred_knn_tuned_CVGS_train))
R2_knn_tuned_CVGS_Train = r2_score(dt_y_Train, y_pred_knn_tuned_CVGS_train)
print(RMSE_knn_tuned_CVGS_Train, R2_knn_tuned_CVGS_Train)

# Test set için:
RMSE_knn_tuned_CVGS_Test = np.sqrt(mean_squared_error(dt_y_Test, y_pred_knn_tuned_CVGS_test))
R2_knn_tuned_CVGS_Test = r2_score(dt_y_Test, y_pred_knn_tuned_CVGS_test)
print(RMSE_knn_tuned_CVGS_Test, R2_knn_tuned_CVGS_Test)
