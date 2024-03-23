y <- matrix(c(35,42,24,27,37),5,1,byrow = F)
X <- matrix(c(1,1,1,1,1,
              10,15,18,24,30,
              50,75,90,120,150),5,3,byrow = F)
b <- solve(t(X/X%*%X)%*%t(X)%*%y))
#Tam ilişki olduğu için tahmin edilemedi

#Güçlü ilişki varsa korelasyonun 1'e yakın olduğu durumda B1 x1 ile beraber x2'nin de etkisini içerecek.

veri <- data.frame(y=c(16,23,15,18,28),
                   x1=c(6,5,3,4,5),
                   x2=c(5,4,5,3,3),
                   x3=c(9,9,5,7,9))
reg <- lm(y~x1+x2+x3,data = veri)
summary(reg)

#0.05'ten hepsi büyük olduğu için hepsi efektsiz, parametreler anlamlı değil.Ama R2 yüksek
#Güçlü bir ilişki olduğu için çoklu doğrusal bağlantı olabilir VIF bakarız.
vif(reg)
veri_x=veri[,2:4]
install.packages("corpcor")
library("corpcor")
cor2pcor(cov(veri_x))
#Hata terimleri bir diğerine etkiliyorsa otokorelasyon var diyoruz.
#Otokorelasyon olmaması temel varsayımlarımızdan biriydi.

#Modelde sabit terim olmalı (orjinden geçen denklemde uygulanamaz(sabit terim yoktur))
#Durbin-Watson
reg1 <- summary(lm(comsales~indsales,data=blaisdell))
ut <- reg1$residuals
ut_1 <- lag(ut,n=1)
ut_1
as.data.frame(ut)
as.data.frame(ut_1)
res_data <- cbind(ut,ut_1)
res_data <- as.data.frame(res_data[2:20,])
ut_ut_1 <- sum((res_data$ut-res_data$ut_1)^2)
utsq <- sum((reg1$residuals)^2)
dw=ut_ut_1/utsq
dw
#post otokorelasyon

