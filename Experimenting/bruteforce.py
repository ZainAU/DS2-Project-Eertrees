def isPalidromic(s, i, j):
    if (i > j):
        return 1
    if (i == j):
        return 0
    return isPalidromic(s, i+1, j-1)


def print_substrings(s):
    i, j = 0, 0
    substrings = []
    for i in range(0, len(s)+1):
        for j in range(0, len(s)+1):
            substrings.append(s[i:j])
    return substrings


# print(print_substrings("google"))

# "a sa".__reversed__()


def returnPalindromes(s):
    palindromes = []
    substrings = []
    for i in range(0, len(s)+1):  # O(n)
        for j in range(0, len(s)+1):  # O(n)
            substrings.append(s[i:j])
    for x in substrings(s):  # worst case O(n)
        print(x)
        if x == "":
            continue
        if x == x[::-1]:
            palindromes.append(x)
    return palindromes  # O(n^3)


print(returnPalindromes("google"))
