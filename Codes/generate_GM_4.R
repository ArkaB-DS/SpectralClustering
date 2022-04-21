set.seed(42)
# install.packages("distr")
library(distr)

## Construct the distribution object.
myMix <- UnivarMixingDistribution(Norm(mean=-12, sd=3), 
                                  Norm(mean=2, sd=1),
                                  Norm(mean=15, sd=2),
                                  Norm(mean=30, sd=3),
                                  mixCoeff=c(0.4, 0.2, 0.3, 0.1))
## ... and then a function for sampling random variates from it
rmyMix <- r(myMix)

## Sample a million random variates, and plot (part of) their histogram
x <- rmyMix(1e6)
hist(x[x>-100 & x<100], breaks=100, col="grey", main="")
x <- as.data.frame(x)
write.table(x, file = "generate_GM.csv", sep = ",",
	row.names = F, col.names = F)