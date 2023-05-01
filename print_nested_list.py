'''
s = [[[2, 1]], [[6, 9]], [8, 34], 12]
'''

def print_list(L):
    for i in L:
        if type(i) is int:
            print(i)
        if type(L[i]) is list:
            for j in i:
                print_list(j)


L = [2,3,[3,4,5],9]
print(print_list(L))
