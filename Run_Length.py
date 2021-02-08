#d = "000000111111111111110000000000000111111111"

d=str(input('Enter the message:'))

print('Message: ', d)
d = d + "."
data = [i for i in d]
run_list = []
data_list = []
run = 0
for i in range(0,len(data)-1):
    if data[i] == data[i+1]:
        run = run + 1
    else:
        run_list.append(format(run+1, 'b'))
        data_list.append(data[i])
        run = 0

print(run_list)
print(data_list)
output = []
max_len = len((max(run_list, key=len)))
for i in run_list:
    if len(i) < max_len:
        diff = max_len - len(i)
        i = '0'*diff + i
        output.append(i)
    else:
        output.append(i)
print("Code: ")
for i in range(0,len(data_list)):
    print(data_list[i]+output[i])

