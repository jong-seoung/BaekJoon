N = input().upper()
N_set = list(set(N))
N_list = []

for i in N_set:
    n = N.count(i)
    N_list.append(n)
if N_list.count(max(N_list)) > 1:
    print("?")
else:
    print(N_set[N_list.index(max(N_list))])
    