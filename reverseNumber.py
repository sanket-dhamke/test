

num = 27
reverse = str(num)
print(reverse, '****')

reverse_num = reverse[::-1]
print(reverse_num,'#####')
reverse_no = 0
while num != 0:
    digit = num % 10
    reverse_no = reverse_no * 10 + digit
    num = num // 10

print(reverse_no)

str1 = "Hi Tilak true"
re_str = str1.split(' ')
rv = re_str[::-1]
rv = ' '.join(rv)
print(rv)

