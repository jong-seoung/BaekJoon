def solution(n, s):
    # 최대 값 계산
    mox = s // n
    na = s % n

    # mox가 0 이하인 경우 균등하게 나눌 수 없음
    if mox <= 0:
        return [-1]
    
    # 기본 값을 모두 mox로 초기화
    answer = [mox] * n
    
    # 나머지 값을 앞에서부터 분배
    for i in range(na):
        answer[i] += 1
    
    # 결과 반환 (정렬하여 균등 분배 확인 가능)
    return sorted(answer)
