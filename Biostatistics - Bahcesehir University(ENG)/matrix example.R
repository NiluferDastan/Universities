matrix(c(24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70),nrow=4,ncol=6,byrow=TRUE)
matris <- matrix(c(24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70),nrow=4,ncol=6,byrow=TRUE)

rectangular_matrix <- matrix[4]
rectangular_matrix
ikinci_satir <- matris[2,]
besinci_satir <- ikinci_satir*5
matris <- rbind(matris,besinci_satir)
matris