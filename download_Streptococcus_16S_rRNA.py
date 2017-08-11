#python version 3.5
#!/usr/bin/python
import Bio
from Bio import Seq.IO

search_string = "(((Streptococcus[Organism]) AND rRNA[Filter])) AND 16S ribosomal RNA Gene[Text Word]"
handle = Entrez.esearch(db='nucleotide',term=search_string,retmax=10000)
record = Entrez.read(handle)
gi_list = record["IdList"]
gi_str = ",".join(gi_list)
handle = Entrez.efetch(db="nuccore", id=gi_str, rettype="gb", retmode="text")
records = SeqIO.parse(handle,"gb")
seq=[]
for record in records:
    seq.append(record)

SeqIO.write(seq,"/sc/orga/projects/zhuj05a/Wenhui/HBV/16srna/Streptococcus_16S_rRNA.fasta","fasta")

#extract taxid
tax=[]
for i in range(len(seq)):
    tax.append(seq[i].features[0].qualifiers.get('db_xref')[0].split(":")[1])

f=open('/sc/orga/projects/zhuj05a/Wenhui/HBV/16srna/taxonid','w')
for i in range(len(tax)):
    f.write("%s\n" % tax[i])
f.close()
