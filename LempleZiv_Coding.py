#data = "BAABABBBAABBBABBB"
#data = '000101111010010100'
data=str(input('Enter the message value : '))

data = [i for i in data]
code = ""
code_l = []

for i in data:
    if i not in code_l:
        code_l.append(i)
l = len(code_l)
for i in data:
    code = code + i
    if code not in code_l:
        code_l.append(code)
        code = ""
output = []
for i in range(l, len(code_l)):
    word = code_l[i]
    last = word[-1]
    first = word[:-1]
    index1 = 1 + code_l.index(first)
    index_bin = format(index1,'b')
    output.append(str(index_bin)+last)

print('Different symbol: ',code_l)
print('Code: ', output)

