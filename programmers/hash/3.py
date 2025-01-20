def solution(phone_book):
    answer = True
    phone_book.sort()

    # 인접한 전화번호들끼리 접두어 관계를 확인
    for i in range(len(phone_book) - 1):
        # 현재 전화번호가 다음 전화번호의 접두어인지 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return answer


phone_book = ["119", "97674223", "1195524421", "45"]
solution(phone_book)
