def common(L1,L2):
    L3 = L1 - L2
    return(L3)

L1 = [2,3,4,5,8,2]
L2 = [1,2,5,9,11]
L3 = [i for i in L2 if i not in L1]
print(L3)


e2i = {e: i for (i, e) in enumerate(L1)}
print(e2i.keys())


#common(L1 , L2)
    