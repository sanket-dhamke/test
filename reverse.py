'''
s1 = "Hi San"
op1 = nas iH

s2 = "Hi San"
op2 = "San Hi"

no = 125
op = 521
'''

def rev_ch(s):
    return s[::-1]


def rev_word(s):
    L = s.split(" ")
    return " ".join(L[::-1])


def rev_no(no):
    return no[::-1]


print(rev_ch("Hi San"))
print(rev_word("Hi San"))
print(rev_no("125"))