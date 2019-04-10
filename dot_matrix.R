d<-read.table("projetETannier/A3GD8JZJ114-Alignment-HitTable.csv",sep=',',h=F)
d<-d[d$V2=="NC_003143.1",]

plot(c(),c(),xlim=c(1,4681143),ylim=c(1,4890491),xlab = "génome moderne",ylab="génome médiéval", main = 'Dot matrix des alignements')
#xlim=c(1,4681143),ylim=c(1,4890491)
segments(d$V7,d$V9,d$V8,d$V10)

d2<-d
i=1
filtres=c()
s=1500
while (i < length(d2[,1])) {
  #print(d2[(d2[i,7]==d2[,7] & d2[i,8]==d2[,8]),])
  subd2<-d2[(d2[,7]>=d2[i,7]-s & d2[,7]<=d2[i,7]+s & d2[,8]>=d2[i,8]-s & d2[,8]<=d2[i,8]+s) | 
              (d2[,9]>=d2[i,9]-s & d2[,9]<=d2[i,9]+s & d2[,10]>=d2[i,10]-s & d2[,10]<=d2[i,10]+s),]
  if (length(subd2[,1])>1) {
    filtres=rbind(filtres,subd2)
    d2<-d2[setdiff(rownames(d2),rownames(subd2)),]
  } else {
    i=i+1
  }
}

length(d2[,1])

#prise en compte du tx de similarité
d2_95<-d2[sqrt((d2_95$V8-d2_95$V7)^2+(d2_95$V9-d2_95$V10)^2)>=3000,]

length(d2_95[,1])
plot(c(),c(),xlim=c(2100000,2.4e6),ylim=c(1.8e6,2e6))
plot(c(),c(),xlim=c(1,4681143),ylim=c(1,4890491),xlab = "génome moderne",ylab="génome médiéval", main = 'Dot matrix avec graphe de comparaison')

#segments(d2$V7,d2$V9,d2$V8,d2$V10,col='green')
segments(filtre95$V7,filtre95$V9,filtre95$V8,filtre95$V10,col='green')
segments(filtres$V7,filtres$V9,filtres$V8,filtres$V10,col='red')
segments(d2_95$V7,d2_95$V9,d2_95$V8,d2_95$V10)

#boxplot(d2$V3,d2_95$V3,filtres$V3)

#adjacences
adj=c()
for (i in seq(length(d2_95[,1]))) {
  ha=min(d2_95[d2_95$V7>=d2_95[i,8],7])
  hb=d2_95[d2_95$V7==ha,9]
  vb=min(d2_95[d2_95$V9>=d2_95[i,10],9])
  va=d2_95[d2_95$V9==vb,7]
  adj=rbind(adj,c(d2_95[i,8],d2_95[i,10],ha,hb,va,vb))
}
head(adj)
length(adj[,1])

segments(adj[,1],adj[,2],adj[,3],adj[,4],col='green')
segments(adj[,1],adj[,2],adj[,5],adj[,6],col='purple')

points(adj[,1],adj[,2])

#comptage des cycles
library(igraph)
test <- data.frame(start=c(1,2,3,4), stop=c(2,3,1,5))
test
g <- graph.data.frame(test)
g
cycles <- t(sapply(3:dim(test)[1], function(x) {v=graph.motifs.no(g, size=x); c(x,v)}))
colnames(cycles) <- c("size","count")
cycles

