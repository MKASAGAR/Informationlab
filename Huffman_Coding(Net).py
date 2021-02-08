#huffman coading
from heapq import heapify, heappop, heappush
from collections import defaultdict

mess = "HAPPY HAPPY"

freq = defaultdict(int)

for ch in mess:
    freq[ch] += 1

print("Frequency: ", freq)

heap = [[fq, [sym, ""]] for sym, fq in freq.items()]
heapify(heap)

while len(heap)>1:
    right = heappop(heap)
    left = heappop(heap)

    for pair in right[1:]:
        pair[1] = '0' + pair[1]
    for pair in left[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap, [right[0]+left[0]] + right[1:] + left[1:])

code = []
for ch in heap:
    for c in ch:
        code.append(c)
code = code[1:]
print('Code: ',code)

bit = ''
for ch in mess:
    for c in code:
        if ch == c[0]:
            bit = bit + c[1]
            break
print('code: ',bit)

decode = ''
c = ""
for b in bit:
    c = c + b
    for co in code:
        if c == co[1]:
            decode = decode + co[0]
            c = ''
            break

print('decode: ',decode)
