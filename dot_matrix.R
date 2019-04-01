d<-read.table("projetETannier/A3GD8JZJ114-Alignment-HitTable.csv",sep=',',h=F)
d<-d[d$V2=="NC_003143.1",]

plot(c(),c(),xlim=c(1,4681143),ylim=c(1,4890491))

segments(d$V7,d$V9,d$V8,d$V10)


