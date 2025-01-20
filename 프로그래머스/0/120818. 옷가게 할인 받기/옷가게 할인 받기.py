def solution(price):
    answer = 0
    sale = 0
    if price >= 500000:
        sale = 20
    elif price >= 300000:
        sale = 10
    elif price >= 100000:
        sale = 5
    else:
        pass
    print(sale)
    answer = int(price - (price * (sale/100)))
    return answer