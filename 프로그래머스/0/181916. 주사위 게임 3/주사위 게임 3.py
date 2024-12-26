from collections import Counter

def solution(a, b, c, d):
    num_count = Counter([a, b, c, d])
    num_len = len(num_count)
    
    if num_len == 1:
        return 1111 * a

    elif num_len == 2:
        counts = list(num_count.values())
        if 3 in counts:
            num1, num2 = sorted(num_count.keys(), key=lambda x: -num_count[x])
            return (10 * num1 + num2)**2
        else:
            nums = list(num_count.keys())
            return (nums[0] + nums[1]) * abs(nums[0] - nums[1])

    elif num_len == 3:
        for key, count in num_count.items():
            if count == 2:
                remaining = [k for k in num_count.keys() if num_count[k] == 1]
                return remaining[0] * remaining[1]

    else:
        return min(num_count.keys())