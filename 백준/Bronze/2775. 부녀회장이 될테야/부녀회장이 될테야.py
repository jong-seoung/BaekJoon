def a(k,n):
    for i in range(k+1):
        globals()[f'f{i}'] = []
    for i in range(1,n+2):
        f0.append(i)
    for i in range(k):
        globals()[f'f{i+1}'].append(globals()[f'f{i}'][0])
        for j in range(1,n+1):
            globals()[f'f{i+1}'].append(globals()[f'f{i}'][j]+globals()[f'f{i+1}'][j-1])
    return print(globals()[f'f{k}'][n-1])

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    a(k,n)
