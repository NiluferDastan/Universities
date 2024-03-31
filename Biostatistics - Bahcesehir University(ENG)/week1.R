# Basic Aritmetic Operations
192 + 250 #Addition
955 - 380 #Subtraction
20 * 100 #Multiplication
50/5   #Division
5^4    #Exponent
23^5
18 %% 7  #Modulo - Returns the reminder
(12 + 34) * 5
12 + 34 * 5
sqrt(9) #square
exp(10)
pi
exp(pi)
log(10) #default base exp(1)
?log
help(log)
log(100,base=10)
1/35436156 # e notation
74155546*6465413

#Assigning objects
x = 80
y <- 100
97 -> z     # = and <- is used for assigning
x = 23

x
x^2 + sqrt(x) + x * 2
x + y
z = x + y
z
var2 = sqrt(x^2+y^2)
x + 10
x = x + 10
x

q1 = 10
Q1 = 19

#cleaning variables
rm(x)
x
rm(y,z,var2) #could delete more than one variable at the time 
ls() #shows the names of each variables
rm(list=ls()) #delete all

#Vectors
##c() function can be used
c(1,32,43,54,65,76)
a = 10
x = c(1,4,23,43,12)
x

x + 10
x * 5 

sqrt(x)

g = 10
h = 20
x = c(1,4,2,4)
y = c(11,44,23,21,43,12)
c(g,30,x)
c(1,23,43,c(23,43,54,23))
c(x,y)
q = c(x,y,g,h,15) #vectors can be merged
q

##other ways to create a vector
vec1 = 1:10
vec1
vec2 = 15:5
vec2

vec3 = 11.2:34+4.3
vec3
vec4 = 11:(34+4.3)
vec4

a = 4
vec5=a:10
vec5


help(seq)
seq1 = seq(from=90, to=110, by = 2)#creates numbers with interval 2 between 90 and 110
seq1

seq2 = seq(from=30, to=60, length.out = 10)#creates 10 equally spaced numbers between 30 and 60
seq2

seq3 = seq(from=24, to=45+33, by=2)
seq3
