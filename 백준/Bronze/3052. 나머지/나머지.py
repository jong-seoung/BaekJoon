b = []

for i in range(1,11):
    i = int(input())
    a = i % 42
    b.append(a)

c = list(set(b))
print(len(c))