from oureertree import *
from analyzingDNA import *

#string1 = 'tagccgcgatacgctggttgcgcgccacgccgagctcaactatccgtccatccgaagcctttcacttagttaactataatttttgacatctcagccgcgactagtgaagtccgttcgcatgcttgacccatgactacgaggaaggagaccgtagaaggtgttgttaggtctccatcctggttagcctagtgattcggcattcacggtcccgatctcgaaacaatttcatgttaagaacaaagcacctgatggacacccaccctaacggccggcgccccgtaacatcgggcaaggagaatagtaagaacgagttttatccctgagggttgttgattgtcgttatgtagggttccggagtatcggacgtgataggtgtagcttgcgcctttggtcagggatgacgacgatagctcatcttcaaatcttccagtccttcttccggccgttggttggtctaggaagccgcgagatcgcattagtaacatctttgagcttgaacccggagaagatttgttcgaacgtgagtgccaccacaaatgtatccctgacgttagccgtgattaccagacgacctaactgctgagttgtgctgttatcccaaactgctaatcctcttgacgggctgtctagcttaaaacagtcacagagtgttcccaggtcgcgcttaagctcctcttagaggccaaggatgtctatggtgtcccgcgaccatgtcgccgatatatacttgggtgtttagtcccccccagttaccgtaaatagcacctctgacaaacctgcagctcgccggtagaagccatttacgtattaacgtatggaacgcacaaaccggaatgagatatcgataggtctaccagaggatcgcgttaaaaaactgcaaggtgactactgataatttggtcgtactcaataagtactgtcgcgactagggctatccatcccaagtgtaaacgggggttgacgatgctcgtgtaccaattacgggccgacctgacacaac'
# string2 = 'gctggactcattactttacgggagagaggtagacatagtacggagggaatctatcgcgacctatcgctaggttgaggcgggatccacggccgtcagagagggaggcaaagcgcgctgcacctgcgcacacgaggggccaacgccttagggttcgcgctctacaagtgcgcgcctttaagcctaacgttctctgaccacgtcaggttgtcaaggcgcttcaatgtattatcgatttgtacggccgctgctagggctcataacacgggtaattgagagacatcagagacttaagcgtcttaaattgattcccggtataacggcgacttcagaccaaggtgttgcttcgattgtcgtagttcgtagcttcggactccaaagtggaactcgcggagacaacacgatgctgcgatctctgacccgttaacacacagatttataattctgacattatttgctattcccctcaataggccggggacccgttaagcgtgtagggctgtgcgatgaaggagcgcctgtgtagctgcgtggcaagccatctgcaagtcgtaatctagtccctcgtgtttatggtgggccagtcggtactctagaacacgactgcacatcttaacgactcccttgtgcgccggcgggcaagcgccgcgtggttgttttacaaacgttttctagtctggctctgaggttgggttcggtaggccggccgtgatgtgtcccccgtgtaggcccgaaataacggatccccttacctctaacaaacagcgcgtacaacttggtgtggtgcctgatcgatacgctaaggcttttgcctcctcctgctggagggacgtagactaagggtaggcacttcgccgaaggccttctttgcttgaacagcactgtctgcacaggctcccaagacccttcaacatacagacactataaaggccctgagtgcgcggacaaacgttgaccaagaccgtacctgtgcgggttctgcaatataggttcctggcactga'

# eertree1 = Eertree()
# eertree2 = Eertree()
# eertree1.addStringToTree(string1)
# eertree2.addStringToTree(string2)

# lst1 = eertree1.getPalindromes()
# lst2 = eertree2.getPalindromes()

# Get similar palindromes


def similar_palindromes(lst1, lst2):

    similar = list()
    for i in lst1:
        if i in lst2:
            similar.append(i)
    return similar


# similar_palindromes(string1, string2)


# Similarity Score
def similarity_score(similar, lst1, lst2):
    return len(similar)/(len(lst1)+len(lst2))


# Get string instbility score and which one is more instable
def instability_comparission(lst1, lst2):
    threshold_length = 8

    instability_score_str1 = instability_rate(lst1, threshold_length)
    #print ('1  ',instability_score_str1)
    instability_score_str2 = instability_rate(lst2, threshold_length)
    #print('2  ',instability_score_str2)

    if instability_score_str1 > instability_score_str2:
        return('DNA string 2 is more instable than DNA string 1 by ' +
               str(instability_score_str1-instability_score_str2))
    elif instability_score_str1 == instability_score_str2:
        return('Both string are equally instable with' +
               str(instability_score_str2) + ' instable rate')
    else:
        return('DNA string 1 is more instable than DNA string 2 by ' +
               str(instability_score_str2-instability_score_str1))
