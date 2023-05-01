def merge(L1 , L2):
    L3 = []
    length1 = len(L1)
    length2 = len(L2)
    print(list(zip(L1,L2)))

    for i in range(max(length1,length2)):
        if i < length1:
            L3.append(L1[i])
        if i < length2:
            L3.append(L2[i])




L1 = [2,6,8,3]
L2 = [1,9,34]

print(merge(L1,L2))