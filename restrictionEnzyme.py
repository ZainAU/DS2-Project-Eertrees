from ourEertree import *
str1='XZYGAATTC'
str2='CTTAAGXYZ'
double_stranded_dna=str1+str2
print('double stranded dna', double_stranded_dna)

eertree=Eertree()
eertree.addStringToTree(double_stranded_dna)
pals= eertree.getPalindromes()
print ('pals', pals)

for i in pals:
    if i =='GAATTCCTTAAG':
        print ('Recognition Sequence of Escherichia coli identified, EcoR1 enzyme to cut the DNA strands')
        dna_cut=pals.index(i)
        part_in_str1=i[0:6]
        str1_broken1=str1[0:str1.index(part_in_str1)+1]
        str1_broken2=str1[str1.index(part_in_str1)+1:]
        # print(str1_broken2)

        part_in_str2=i[6:]
        str2_broken1=str2[0:str2.index(part_in_str2)+5]
        str2_broken2=str2[str2.index(part_in_str2)+5:]
        #print(str2_broken2)

    if i =='GGATCCCCTAGG':
        print ('Recognition Sequence of Bacillus amyloliquefaciens identified, BamH1 enzyme to cut the DNA strands')
        dna_cut=pals.index(i)
        part_in_str1=i[0:6]
        str1_broken1=str1[0:str1.index(part_in_str1)+1]
        str1_broken2=str1[str1.index(part_in_str1)+1:]
        # print(str1_broken2)

        part_in_str2=i[6:]
        str2_broken1=str2[0:str2.index(part_in_str2)+5]
        str2_broken2=str2[str2.index(part_in_str2)+5:]
        #print(str2_broken2)


print ('Double stranded DNA 1 \n', str1_broken1, '\n', str2_broken1)
print ('Double stranded DNA 2 \n', str1_broken2, '\n', str2_broken2)
