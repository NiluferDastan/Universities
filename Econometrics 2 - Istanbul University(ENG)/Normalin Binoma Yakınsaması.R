function(x,n,p=0.05,alternative=c("two.sided","less","greater")) -> x
{ 
  if (n>=25) 
  { 
    if (alternative=="less") 
    { 
      mu=n*p 
      std<-sqrt(n*p*(1-p)) 
      if(x<mu) x<-x+0.5 else z<-x-0.5 
      z= zDonusum(x,mu,std) pvalue=pnorm(z) 
    } 
    return(list(z=z,pdegeri=pvalue)) 
  }
  if (n<25) 
  {
    binom.test(x,n,p,alternative="less") 
  }
binomTest(23,50,0.56,alternative="less")