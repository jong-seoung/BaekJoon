def solution(elements):
    n = len(elements)
    extended = elements * 2  # 원형 배열처럼 작동하게 배열을 두 번 붙임
    lst = set()  # 고유한 부분 수열 합 저장
    
    for length in range(1, n + 1):  # 부분 수열 길이
        for start in range(n):  # 시작 인덱스
            # 시작점부터 길이만큼 합을 계산
            subarray_sum = sum(extended[start:start + length])
            lst.add(subarray_sum)  # 합을 집합에 추가
    
    return len(lst)  # 고유한 합의 개수 반환
