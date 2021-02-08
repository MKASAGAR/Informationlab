def pos(x):
    p = []
    for i in range(0,len(x)):
        if x[i] == '1':
            p.append(i)
    return p


def multi(a,b):
    result = []
    a = [i for i in a]
    b = [i for i in b]
    a = pos(a)
    b = pos(b)
    for i in a:
        for j in b:
            if i+j not in result:
                result.append(i+j)
            else:
                result.remove(i+j)
    return result


#g1 = "111"
g1 = str(input('Enter the value of g1:'))
#g2 = "101"

g2 = str(input('Enter the value of g2 :'))

#m= "1001111"

m=str(input('Enter the message:'))

print('G1= ', g1)
print('G2= ', g2)
print('Message= ', m)
c1 = multi(g1,m)
c2 = multi(g2,m)
max_num = max(max(c1),max(c2))
code = []
for i in range(0, max_num+1):
    if i in c1:
        j = "1"
    else:
        j = "0"
    if i in c2:
        k = "1"
    else:
        k = "0"
    code.append(j+k)
print('Code: ',code)

