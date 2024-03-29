"""
A word is said to be perfect if it satisfies all the following criteria:

(1) All the vowels (a,e,i,o,u) should be present in the word.
(2) Let the vowels be represented as v1=a,v2=e,v3=i,v4=o,v5=u in lexical order.

    If i<j, then the first appearance of Vi in the word should come before the first appearance of Vj
    If i<j, then the count of Vi should be greater than or equal to the count of Vj.

Accept a word as input and do the following:
 (1) If it is a perfect word, print It is a perfect word
 (2) If the word is not a perfect word, print It is not a perfect word"""
flag=0
word = str(input())
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Generate a frequency distribution of vowels in word
for i in range(len(word)):
    if word[i] in vowels.keys():
        vowels[word[i]] += 1
print(vowels)

# Perform check - Count
if vowels['a']>=vowels['e']>=vowels['i']>=vowels['o']>=vowels['u']:
    print('It is a perfect word')
else:
    print('It is not a perfect word')