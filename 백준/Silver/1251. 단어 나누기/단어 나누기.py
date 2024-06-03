word = list(map(str, input()))
temp = []
res = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        temp.append(a+b+c)

for _ in temp:
    res.append(''.join(_))

print(sorted(res)[0])