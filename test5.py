def solution(foods):
    N = len(foods)
    if N < 3:
        return 0

    # 전체 만족도 합 계산
    total_sum = sum(foods)
    
    # 전체 합이 3으로 나누어떨어지지 않으면 나눌 수 없음
    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3  # 각 돼지가 가져야 하는 만족도 합
    count = 0
    
    # 누적 합 계산
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + foods[i]
    
    first_count = 0  # 첫 번째 돼지 만족도 합이 target인 경우의 수
    
    # 첫 번째 돼지와 두 번째 돼지의 구간을 탐색
    for i in range(1, N):  # i는 두 번째 돼지의 시작점
        # 첫 번째 돼지의 만족도 합 확인
        if prefix_sum[i] == target:
            first_count += 1
        
        # 두 번째 돼지의 만족도 합이 target인지 확인
        if prefix_sum[i] == 2 * target:
            count += first_count  # 첫 번째 돼지가 만족도를 맞춘 경우의 수를 누적
            
    return count

# 테스트
test_cases = [
    [1, 2, 3, 0, 3],  # 예상 출력: 2
    [4, 1],        # 예상 출력: 0
    [1, 1, 1, 1, 1, 1],  # 예상 출력: 1
]

for foods in test_cases:
    result = solution(foods)
    print(f"Input: {foods}")
    print(f"Output: {result}\n")