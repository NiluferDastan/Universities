Halka açık içme suyu kaynaklarındaki arsenik konsantrasyonu potansiyel bir sağlık riskidir. Bir araştırmacı, A ve B bölgelerindeki bazı alanlardaki halka açık içme suyu kaynaklarındaki arsenik konsastrasyonunu (ppb)


A_bolg <- c(3,7,25,10,15,6,12,25,15,7)
B_bolg <- c(48,44,40,38,33,21,20,12,1,18)

A bölgesi ve B bölgesi birbirinden bağımsız iki değişken olduğu için iki ayrı grubu karşılaştırırız.Öncelikle normallik
varsayımını kontrol ederiz.
shapiro.test(A_bolg)  # p değeri = 0.1861 > 0.05 olduğundan normallik varsayımı sağlanır
shapiro.test(B_bolg)  # p değeri = 0.6764 > 0.05 olduğundan normallik varsayımı sağlanır

Bu durumda bağımsız örneklemler için t-test uygularız.Öncelikle verileri bağlamamız gerekiyor.
veri <- c(A_bolg,B_bolg)
grup <- c(rep("A_bolg",length(A_bolg)),rep("B_bolg",length(B_bolg)))
birlest_veri <- data.frame(veri,grup)
library(car)
leveneTest(veri~grup,birlest_ve
wilcox.test(A_bolg,B_bolg,paired = T)
Varyansların homojenliği testi için p değeri =0.01248<0.05 olduğundan homojenlik sağlanmaz. Bu yüzden Ho reddedilir

eğit_önc <- c(90,89,76,92,91,73,65,88,75,85)
eğit_sonr <- c(97,93,85,86,99,74,70,92,83,92)

Gruplar öncesi-sonrası testi olduğu için bağımlı t örneklem testi uygulanır ama öncelikle normallik kontrolü yapılır
normallik varsayımı sağlarsa t test
d <- eğit_önc-eğit_sonr    #Farkları d ile bulduk
shapiro.test(d)     
P değeri=0.032<0.05 olduğundan normallik varsayımı sağlanmaz bu yüzden wilcoxon işaretli sıra testini yaparız.Artık hipotezi kurabiliriz.
Ho: Eğitimden öncesi ve sonrası çalışanların performansları arası farklılık  yoktur.
H1: Eğitimden öncesi ve sonrası çalışanların performansları arası farklılık  vardır
library(nortest)
wilcox.test(eğit_önc, eğit_sonr, paired = T) 
Wilcoxon testi sonucu p değeri=0.02465<0.05 olduğundan Ho reddedilir.Yani eğitimden öncesi ve sonrası çalışanların performansları arası farklılık  vardır

hava <- c("Yağmurlu","Yağmurlu","Yağmurlu","Yağmurlu","Yağmurlu","Günesli","Günesli","Günesli","Günesli","Günesli",)
sıcaklık <- c("Soğuk","Ilıman","Ilıman","Soğuk","Soğuk","Soğuk","Sıcak","Sıcak","Ilıman","Ilıman")
nem <- c("Normal","Yüksek","Normal","Normal","Normal","Normal","Yüksek","Yüksek","Yüksek","Yüksek")
data_frame <- data.frame(hava,sıcaklık,nem)
print(data_frame)

capraz_tablo <- table(hava,sıcaklık,nem) 
print(capraz_tablo)

yüzdelik_capraz_tablo <- prop.table(capraz_tablo)
print(round(100*yüzdelik_capraz_tablo,3))

x <- rnorm(1000,mean = 5,sd=2)
oyf <- dnorm(1000,mean = 3.42,sd=0.2)
boxplot(x,oyf,type="box",xlim = c(-4.4,-2.5))
hist(x)

A)P(x>=4)
1-pbinom(4,18,0.05)
B)p(x<=4)
pbinom(2,18,0.05)
C)P(2<=x<=4)
pbinom(4,18,0.05)-pbinom(2,18,0.05)

soru 8 
n=2000
p=0.001 olasılık çok düşük olduğundan poissona yakınsar
A)P(x=3)
dpois(x=3,lambda=2000*0.001)
B)P(x>=2)
1-ppois(2,2000*0.001)

matris <- runif(9,min = 1,max = 5)
x <- matrix(matris, nrow=3,ncol=3)
dimnames<- list(c("1.satır","2.satır","3.satır"),c("1.sütun","2.sütun","3.sütun"))
x