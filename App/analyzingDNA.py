from oureertree import *

# dna_seq='ggagttagagatcggatactgaagttaacgaaactccaggtcataggggctggaatggctcgtgtcgactcgctgactgagcacgtacgggcggcatggctgaacactgtggggctcacttagcaatctagaacgacgattgaccgagggcagaaatcgtccttgtttgccgcgagtgtgagtttgttccaggagcttggagcagagctcgccaattctcgcttatgcctaacagcgagaccggagaatgacgggtgtcgatctagcgtagtggccgatgtgacgagagcttatcacaagggtgcattcatttcgggcgttgtagccgggactctctctcacaggttgcagatattatggtacactgacgtactagaaaggctacattggtgtatcatacgctgcaatatcagtgaccaagtggatccggtcgggaggtagatgccgcatgttcctacccatgggcagcgcatatacacg'

# get all sub palindromes


def get_subpalindromes(dna_seq):
    eertree = Eertree()
    eertree.addStringToTree(dna_seq)
    pals = eertree.getPalindromes()
    return pals


# Get longest palindrome
def longest_pal(pals):
    return max(pals, key=len)


# Get instablity score -- long pals / total pals
#threshold_length = 8


def instability_rate(pals, threshold_length):
    long_pals = 0
    for i in pals:
        if len(i) >= threshold_length:
            long_pals += 1

    return round(long_pals/len(pals), 2)

#print (instability_rate(pals,threshold_length))
