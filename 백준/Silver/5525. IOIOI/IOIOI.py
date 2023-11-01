N = int(input())
M = int(input())
S = list(input())
Pn = 'I'

for i in range(N):
    Pn += 'OI'

for i in range(M-2*N):
    for j in range(i+1, i+1+2*N):
        S[i] += S[j]

print(S.count(Pn))