from collections import Counter


def solution(participant, completion):
    # 참가자와 완주자의 이름 빈도수 계산
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    # 차집합을 이용해 완주하지 못한 선수의 이름을 찾음
    for name in participant_count:
        if participant_count[name] != completion_count[name]:
            return name


participant = ["kiki", "kiki", "eden"]
completion = ["eden", "kiki"]

solution(participant, completion)
