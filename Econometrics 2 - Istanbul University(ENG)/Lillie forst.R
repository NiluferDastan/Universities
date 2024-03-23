library(nortest)
veri<- read.csv2("C:/Users/pc/Desktop/Nilüfer/R Uygulamaları/kolesterol_veri_seti.csv",header=T,sep =";",dec = ",")

s_veri <- split(veri,veri$cinsiyet)

p<- c()
for (i in 1:length(s_veri)) {
  v <-unlist(as.vector(s_veri[[i]][2]))
  t <-lillie.test(v)
  p[i] <- t$p.value
}
print(p)
test <- wilcox.test(yaş~cinsiyet,data=veri,alternative="two.sided")
print(test)

#eğer cinsiyete göre yaş verileri ayrı ayrı incelendiğinde normal dağılım gösterseydi
#bağımsız örneklemler t-testi uygulanacaktı.verilerin normal dağıldığıı varsayalım.
#Öncelikle varyanslların homojenliğine bakılması gerekir.


leveneTest(yaş~cinsiyet,data=veri,center=mean)
test<- t.test(yaş~cinsiyet,data=veri,var.equal=T,alternative="two.sided")
print(test)

#Eğer varyansların homojenlik varsayımı sağlanmasaydı bu durumda

test<- t.test(yaş~cinsiyet,data=veri,var.equal=F,alternative="two.sided")
print(test)
##
#3.aydaki kolestrol ile 6.aydaki kolesterol arasında anlamlı bir farklılık var mıır?
D<- veri$kol_3ay~kol_6ay
lillie.test(D)
test<-t.test(veri$kol_3ay,veri$kol_6ay,paired=T,alternative="two.sided")
print(test)

#Eğitim öncesi kilo ile eğitim sonrası kilo arasında anlamlı farklılık var mıdır?

test<-wilcox.test(veri$kilo_önce,veri$kilo_sonra,paired=T,alternative="two.sided")
print(test)

#cinsiyete göre glikoz değerleri açısından anlamlı bir farklılık var mıdır?


d<- veri$kilo_önce~veri$kilo_sonra
lillie.test(d)

test<-wilcox.test(veri$kilo_önce,veri$kilo_sonra,paired=T,alternative="two.sided")
print(test)