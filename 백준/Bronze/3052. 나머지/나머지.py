num = []
result = []
for i in range(10):
    num.append(int(input()))

for i in num:
    a = i % 42
    result.append(a)

print(len(set(result)))