# 16sRNA-clustering
Part1:
1.	Using biopython module, firstly find all the gi ids with search criteria “(((Streptococcus[Organism]) AND rRNA[Filter])) AND 16S ribosomal RNA Gene[Text Word]”
2.	Find the sequences with Seq.IO and write to a fasta file
3.	The taxids are extracted and saved separately
Part2
1.	Using pairwiseAlignment to pairwise align the sequences and save the scores as the pairwise similarity.
2.	Convert similary matrix to distance matrix.
3.	The following graph is the plot of hierarchical

5 sequences with taxid 83427 are outliers. 
They are:
KY082706.1 Uncultured Streptococcus sp. isolate DGGE gel band 9B_33 16S ribosomal RNA, partial sequence
KY082705.1 Uncultured Streptococcus sp. isolate DGGE gel band 8B_29 16S ribosomal RNA, partial sequence
KY082701.1 Uncultured Streptococcus sp. isolate DGGE gel band 4B_18 16S ribosomal RNA, partial sequence
KY082700.1 Uncultured Streptococcus sp. 16S ribosomal RNA, partial sequence
KY082697.1 Uncultured Streptococcus sp. isolate DGGE gel band 1M_1 16S ribosomal RNA, partial sequence
