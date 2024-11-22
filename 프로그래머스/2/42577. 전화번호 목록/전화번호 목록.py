def solution(phone_book):
    hash_map = {}
    # 모든 전화번호를 해시 테이블에 저장
    for number in phone_book:
        hash_map[number] = True

    # 각 번호가 다른 번호의 접두사인지 검사
    for number in phone_book:
        prefix = ""
        for digit in number:
            prefix += digit
            # 접두사가 해시 테이블에 존재하며, 현재 번호와 다른 경우
            if prefix in hash_map and prefix != number:
                return False
    return True