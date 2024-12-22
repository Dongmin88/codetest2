def solution(foods):
    N = len(foods)
    if N < 3:
        return 0


    total_sum = sum(foods)
    

    if total_sum % 3 != 0:
        return 0
    
    target = total_sum // 3  
    count = 0
    
    # 누적 합 계산
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + foods[i]
    
    first_count = 0  

    for i in range(1, N):  
        if prefix_sum[i] == target:
            first_count += 1
        
        if prefix_sum[i] == 2 * target:
            count += first_count  
            
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