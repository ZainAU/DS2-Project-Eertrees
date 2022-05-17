from ourEertree import * 

dna_seq='ggagttagagatcggatactgaagttaacgaaactccaggtcataggggctggaatggctcgtgtcgactcgctgactgagcacgtacgggcggcatggctgaacactgtggggctcacttagcaatctagaacgacgattgaccgagggcagaaatcgtccttgtttgccgcgagtgtgagtttgttccaggagcttggagcagagctcgccaattctcgcttatgcctaacagcgagaccggagaatgacgggtgtcgatctagcgtagtggccgatgtgacgagagcttatcacaagggtgcattcatttcgggcgttgtagccgggactctctctcacaggttgcagatattatggtacactgacgtactagaaaggctacattggtgtatcatacgctgcaatatcagtgaccaagtggatccggtcgggaggtagatgccgcatgttcctacccatgggcagcgcatatacacg'

eertree.addStringToTree(dna_seq)

# Get subpalindromes
pals = eertree.getPalindromes()
# print(pals)


# Get longest palindrome
longest_pal=max(pals,key=len)
# print (longest_pal)


# Get instablity score -- long pals / total pals
threshold_length=int(input("enter threshold value: "))

def instability_rate(pals,threshold_length):
    long_pals=0
    for i in pals:
        if len(i)>=threshold_length:
            long_pals+=1

    return round(long_pals/len(pals), 2)

#print (instability_rate(pals,threshold_length))