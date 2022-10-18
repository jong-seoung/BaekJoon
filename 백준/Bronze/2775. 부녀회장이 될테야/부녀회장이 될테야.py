T = int(input()) # 테스트 횟수

for t in range(T):
    K = int(input()) # 층수
    N = int(input()) # 호수
    p1 = [] # 1층 사람수
    p2 = [] # 전체 사람수

    for i in range(1,15): # 1층 사람수 넣기
        p1.append(i)

    for k in range(K):
        p = 0
        for n in range(N):
            p+=p1[n]
            p2.append(p)
        p1.clear()
        p1 = [] + p2
        p2.clear()
        N-1
        
    print(p1[N-1])