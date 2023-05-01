"""
s = aaab
op -> 3
"""


def pal_high(str2):
    count = 0
    for i in range(0, len(str2)-1): #0 ,4
        for j in range(len(str2)-1, 0, -1): #3 , 0
            if str2[i:j] == str2[i:j][::-1]:   #0,3 3,0
                if len(str2[i:j]) > count:
                    count = len(str2[i:j])
            else:
                pass
    return count


def check_pal(str1):
    stack = [i for i in str1]
    for i in range(len(stack)):
        for j in range(len(stack), 0, -1):
            if stack[i:j] == stack[j:i]:
                print("-1")
            else:
                for k in range(len(stack[i:j])):
                    final_str = stack[i:j].remove(stack[i:j][k])
                    if final_str == final_str[::-1]:
                        print("value of k is", k)
                        return k
                    else:
                        pass


#y = check_pal("bbba")
#print(y)

u = pal_high("bbba")
print(u)

