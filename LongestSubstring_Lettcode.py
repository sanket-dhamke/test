"""
s= abcbbbjk
op: 3
abc

s=bbbb
o/p= 1
b
"""


def count_substring_length(str1):
    count = 0
    d = {}
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if len(list(str1[i:j])) == len(set(str1[i:j])):
                if count < len(list(str1[i:j])):
                    count = len(list(str1[i:j]))
                    d[count] = str1[i:j]

    L = max(d.keys())
    for i,j in d.items():
        if i == L:
            return i,j





print(count_substring_length("abcbbbad"))


