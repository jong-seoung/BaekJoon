while True:
    try:
        k1, k2, k3 = map(int, input().split())
        result = max(k2 - k1, k3 - k2)
        print(result-1)
    except:
        break