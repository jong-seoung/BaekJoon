def solution(n, times):
    def can_process(mid):
        total_people = 0
        for time in times:
            total_people += mid // time
            if total_people >= n:  # 필요한 인원을 모두 처리하면 True
                return True
        return False

    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_process(mid):  # 해당 시간 내에 n명 이상 처리 가능
            answer = mid  # 최소 시간을 갱신
            right = mid - 1
        else:
            left = mid + 1

    return answer
