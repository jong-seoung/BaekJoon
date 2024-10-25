T = int(input())
Q = 25
D = 10
N = 5
P = 1
result = [0,0,0,0]    

for i in range(T):
    change = int(input())

    change = change

    result[0] = int(change//Q)
    change = change%Q

    result[1] = int(change//D)
    change = change%D

    result[2] = int(change//N)
    change = change%N
    result[3] = int(change//P)
    
    print(*result)