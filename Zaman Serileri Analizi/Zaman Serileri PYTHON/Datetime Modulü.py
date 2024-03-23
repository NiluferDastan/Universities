import datetime as dt
import pandas as pd

x=dt.datetime.now() #Şuan ki zamanı verir
print(x)

x=dt.datetime(2010,10,22) #İstediğimiz tarih nesnesini de verebiliyor.
print(x)

x=dt.time(13,24,10) #Saat ayarlanabilir.
print(x)

x=dt.datetime(2010,10,22,13,24,10) #Tek bir yapıda tarih ve saat verebilir.
print(x)

x=dt.date(2010,12,24)
x2=dt.time(12,23,12)
x3=dt.datetime.combine(x,x2)   #İki ayrı nesneyi tek bir nesne olarak birleştirebiliyorsunuz.
x4=dt.datetime.replace(x3,2011,10,30,15,48,26) #Replace an old datetime with new values for the specified fields.
print(x3)
print(x4)

x=dt.date(2010,12,24)
x2=dt.datetime.strftime(x, "%Y-%d-%m") #Transfiguration
print(x)
print(x2)

date=dt.date(2022,10,20)
date2=dt.date(2023,11,20)
diff=date2-dt.timedelta(days=396)  #Difference
print(diff)

date=dt.date(2022,10,20)
date2=dt.date(2023,11,20)
diff=date2-date  #Difference
print(diff.days)


date=["2022-05-01","2023-06-03","2021-02-03"]
data=[1000,2000,3000]
df=pd.DataFrame({"Date":date,"Income":data})
print(df)