# Load dataset 
spotify_data <-read.csv("C:/Users/pc/spotify_2023.csv") #CSV excel formatı
mode_data <-spotify_data[!is.na(spotify_data$mode),] #This command provides delete missing values(NA) 
spotify_data

spotify_data$c_sharp <- as.numeric(spotify_data$key == 'C#')

spotify_data$after_2020 <- as.numeric(spotify_data$released_year > 2020)

#Graph 1: Scatterplot of Danceability Percentage as a Function of BPM
#danceability_percent : Percentage indicating how suitable the song is for dancing #Standardization(percent)

#Creating New Dataset
Dance_BPM <- spotify_data[spotify_data$bpm & spotify_data$danceability_percent,] #&(Birleşim or ve) # , (sonrasını tamamen al)

#I need to upgrade R for running the packages
#conda install -c r r-essentials

#Graphing
#plot(Dance_BPM$danceability_percent ~ Dance_BPM$bpm)

plot(Dance_BPM$danceability_percent ~ Dance_BPM$bpm, col ="blue", pch = 12,
    main = "Danceability Percent vs BPM", xlab = "BPM (Beats Per Minute)", ylab="Danceability Percent")


#Bar Graph of the Frequency of Different Musical Keys 
#Creating New Data Table
key_table <- table(spotify_data$key)


#Graphing
key_table
summary(key_table)  #858 verimiz (NA(missing),0 bunlar eksilmiş)

barplot(key_table, 
        beside=TRUE,
        col= c('blue','blue','red','green','white','white','violet','yellow',
                                      'yellow','orange','orange','blue','blue'),
        main="Frequency of Different Musical Keys", #Title - Başlık
        ylab="Frequency", #y-ekseni başlık
        xlab="Key")       #x-ekseni başlık

#Graph 3: Boxplot of Tempo (BPM) for Popular Major and Minor(mode sütunu)  Key Songs
boxplot(spotify_data$bpm ~ spotify_data$mode,  #(y,x)
       names=c('Major','Minor'),               #mode içinde minor ve major kategorilerim var
       col=rainbow(2),
       main="Tempo (BPM) for Popular Major and Minor Key Songs",
       ylab="BPM",
       xlab="Mode")

#Graph 4: Histogram valence percent in Spotify
#valence_percent: Positivity of the song's musical content
hist(spotify_data$valence_percent,
    main = "Valence Percents for 2023s Most Famous Songs",
    xlab = "Valence Percent",
    ylab = "Frequency")

mean(spotify_data$valence_percent) #mean= total of numbers/953

median(spotify_data$valence_percent) #475.verinin değeri (bütün veriler küçükten büyüğe sıralandığında tam ortada kalan değer)

####ALIŞTIRMA
#Graph 3: Boxplot of Comparing Playlists(Apple vs Spotify)
boxplot(spotify_data$bpm ~ spotify_data$mode,
       names=c('apple','spotify'),
       col=rainbow(2),
       main="Comparing playlist between Apple and Spotify")

proportion_major_key <- mean(spotify_data2$mode == "Major") #Mode sütunundan major olanların ortalamasını al.
proportion_major_key

number_songs <- nrow(spotify_data2)
number_songs

expected_proportion <- 0.5

#Conducting hypothesis testing
alpha <- 0.1
# z = (0.577124868835257 - 0.5) /0.5^2/953
z_statistic <- (proportion_major_key - expected_proportion)/sqrt((expected_proportion * (1-expected_proportion))/number_songs)
p_value <- 2*(1-pnorm(abs(z_statistic)))

#output results
cat("Z-statistic value is:", z_statistic, "\n")

#2.Solution
z_stat <- (proportion_major_key - 0.5) / sqrt((0.5*(1-0.5))/number_songs)
z_stat
#Two-tailed p-value
p_val <- 2*pnorm(z_stat, lower.tail=FALSE)
p_val   #0.05'ten yüksekse anlamlı bir farklılık vardır. 
#H0: Proportion is equal 50%  mu=0.50
#H1: Proportion is not equal 50% mu =/ 0.50

# 99% Confidence Interval
Z <- 2.576 #for a %99 confidence interval  %95=1.96, %90=1.64
se <- sqrt((proportion_major_key*(1-proportion_major_key))/number_songs)   
#standard error
ci_lower <- proportion_major_key - Z*se
ci_upper <- proportion_major_key + Z*se      #(0.57-z*standard error, 0.57 , 0.57+z*standard error)
#Print the confidence interval
cat(paste("99% confidence interval: [", ci_lower,",", ci_upper, "]"))


#Print the confidence interval
print(paste("99% confidence interval: [", ci_lower,",", ci_upper, "]"))

#Average bpm of songs
average_bpm <- mean(spotify_data$bpm, na.rm=TRUE)

#t-test
t_test <- t.test(spotify_data$bpm, mu = 124, na.action =na.omit) #x ve y sütunundaki kayıp verileri çıkartır

#Print the test statistic and p-value
cat(paste("Test statistic:", t_test$statistic))

cat(paste("P-value:", t_test$p.value))

# b) %90 Confidence Interval
z <- 1.645 #for a 90% ci
se <- sqrt((average_bpm*(1000-average_bpm))/number_songs)
# standard error
ci_lower <- average_bpm - z*se
ci_upper <- average_bpm + z*se
#Print the ci
cat(paste("90% confidence interval: [", ci_lower,",", ci_upper, "]"))



