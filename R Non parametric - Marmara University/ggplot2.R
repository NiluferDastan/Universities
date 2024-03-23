wcgsdata <- read.csv2("C:/Users/pc/Desktop/wcgsdata.csv")
View("wcgsdata")
wcgsdata <- read.table(file.choose("C:/Users/pc/Desktop/wcgsdata.csv"),header = T, dec=".",sep = ",")
df_ex2 = data.frame(first_column = c(34,35,36,38,39,40,41,42,43,44,45,46,47,49,52,53,56,58,59,60,62,63,65,66),
                    second_column = c("A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B"))
length(first_column)
length(second_column)
quantile(first_column,probs=c(0.3,0.6))  #gives 30th and 60th percentile

lab_info = list(row_names=c("ali","sude","fatih"),
                age=c(23,30,22)
                
ggplot() + geom_point(aes(c1,c2))
ggplot()
ggplot(aes(c1,c2)) +
  geom_path()

ggplot(aes(c1,c2)) + 
  geom_point()

wcgsdata$weight

ggplot(rat,aes(x = weight, y = WHR)) + 
  geom_point()


#-- setting color,shape,size...
vignette("ggplot2-specs")
# color: the stroke color, the circle outline
# stroke: the stroke width
# fill: color of the circle inner part
# shape: shape of the marker. See list in the ggplot2 section
# alpha: marker transparency, [0->1], 0 is fully transparent
# size: marker size
rat1 = rat
rat = rat1[1:500,]

ggplot(rat,aes(x = weight, y = WHR)) + 
  geom_point(size = 3)

ggplot(rat,aes(x = weight, y = WHR)) + 
  geom_point()

ggplot(rat,aes(x = weight, y = WHR)) + 
  geom_point(size = 3,color = "blue", alpha=0.8)

ggplot(rat,aes(x = weight, y = WHR)) + 
  geom_point(size = 3,color = "blue", alpha=0.8,shape = "square")

ggplot(rat,aes(x = weight, y = WHR)) + 
  geom_point(size = 3,color = "red", alpha=0.8,shape = "square filled",
             stroke = 1,fill="black")

#students turn

ggplot(rat,aes(x = weight, y = WHR,color = smoking)) + 
  geom_point()

ggplot(rat,aes(x = weight, y = WHR,color = exercise)) + 
  geom_point()

ggplot(rat,aes(x = weight, y = WHR,color = age)) + 
  geom_point()

ggplot(rat,aes(x = weight, y = WHR,size = BMI)) + 
  geom_point()

ggplot(rat,aes(x = weight, y = WHR,size = BMI, color = smoking)) + 
  geom_point()

ggplot(rat,aes(x = weight, y = WHR,color = smoking,shape = drinkany)) + 
  geom_point()

ggplot(rat,aes(x = weight, y = WHR,color = smoking,shape = drinkany)) + 
  geom_point(size = 3)


ggplot(rat,aes(x = weight, y = WHR, shape = drinkany)) + 
  geom_point(size = 3, color = "blue")

ggplot(rat, aes(x = weight, y = WHR, color = smoking, shape = smoking)) + 
  geom_point(size = 3)


ggplot(rat, aes(x = weight, y = WHR, color = smoking, shape = smoking)) + 
  geom_point(size = 3, color = "blue") 









