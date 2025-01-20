from math import ceil


def solution(progresses, speeds):
    # 각 작업이 완료되는데 필요한 일 수 계산
    days_to_complete = [ceil((100 - progress) / speed)
                        for progress, speed in zip(progresses, speeds)]

    # 결과를 담을 리스트
    deployment_counts = []

    # 첫 번째 작업의 배포 기준일
    current_deployment_day = days_to_complete[0]
    count = 0

    for day in days_to_complete:
        if day <= current_deployment_day:
            # 배포 기준일 안에 완료 가능한 작업
            count += 1
        else:
            # 새로운 배포 기준일 시작
            deployment_counts.append(count)
            count = 1
            current_deployment_day = day

    # 마지막 배포 추가
    deployment_counts.append(count)

    return deployment_counts
