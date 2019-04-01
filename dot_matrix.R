d<-read.table("projetETannier/A3GD8JZJ114-Alignment-HitTable.csv",sep=',',h=F)
d<-d[d$V2=="NC_003143.1",]

plot(c(),c(),xlim=c(1,4681143),ylim=c(1,4890491))

segments(d$V7,d$V9,d$V8,d$V10)

d2<-d
liste=c()
for (i in seq(length(d2[,1])-1)) {
  
  d[(d[i,7]==d[,7] & d[i,8]==d[,8]) | (d[i,9]==d[,9] & d[i,10]==d[,10]),]
  
  
  d2<-d2[-liste,]
  liste=c()
}

