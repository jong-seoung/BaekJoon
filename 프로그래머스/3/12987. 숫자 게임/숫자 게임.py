def solution(A, B):
    A.sort()
    B.sort()
    
    a_index, b_index = 0, 0
    score = 0
    
    while a_index<len(A) and b_index<len(B):
        if B[b_index] > A[a_index]:
            score += 1
            a_index += 1
        b_index += 1
    return score