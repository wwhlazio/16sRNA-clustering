#version: 3.3.1
library(seqinr)
require("Biostrings")
seqs <- read.fasta("/sc/orga/projects/zhuj05a/Wenhui/HBV/16srna/Streptococcus_16S_rRNA.fasta")
nseq=length(seqs)
mat=matrix(0,nrow=nseq,ncol=nseq)
for(i in 1:(nseq-1)){
	for(j in (i+1):197){
		 mat[i,j]=score(pairwiseAlignment(toString(seqs[[i]]), toString(seqs[[j]])))
	}
	print(i)
}

matx=mat+t(mat)
taxid=read.table('/sc/orga/projects/zhuj05a/Wenhui/HBV/16srna/taxonid',as.is=T)
colnames(matx)=taxid[[1]]
row.names(matx)=taxid[[1]]
d<-dist(matx)
fit <- hclust(d, method="complete")
par(cex=0.6,font=2)
plot(fit)
dev.print(pdf,'/sc/orga/projects/zhuj05a/Wenhui/HBV/16srna/cluster.pdf')
