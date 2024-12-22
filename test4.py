from collections import defaultdict

def solution(total_sp, skills):
    # 노드 개수 파악
    max_node = 0
    for skill in skills: 
        max_node = max(max_node, skill[0], skill[1]) 

    # 부모-자식 관계 생성
    children = [[] for _ in range(max_node + 1)]
    parents = [0] * (max_node + 1)

    for skill in skills:  
        parent, child = skill[0], skill[1]
        children[parent].append(child)
        parents[child] = parent

    # 루트 노드와 리프 노드 찾기
    root = 1  # 문제에서 1번 노드가 루트
    leaves = []
    for i in range(1, max_node + 1):
        if not children[i]:
            leaves.append(i)

    # 각 리프 노드별 필요한 최소값 찾기
    def find_min_leaf_value():
        left, right = 1, total_sp

        while left < right:
            mid = (left + right + 1) // 2

            # 각 리프에 mid 값을 할당했을 때 가능한지 확인
            leaf_values = [mid] * len(leaves)
            node_values = [0] * (max_node + 1)

            # 리프 노드에 값 할당
            for i, leaf in enumerate(leaves):
                node_values[leaf] = leaf_values[i]

            # 상향식으로 부모 노드 값 계산
            valid = True
            total = sum(leaf_values)

            # 리프가 아닌 노드들의 값 계산
            non_leaves = set(range(1, max_node + 1)) - set(leaves)
            for node in sorted(non_leaves, reverse=True):
                if children[node]:
                    node_values[node] = sum(node_values[child] for child in children[node])
                    total += node_values[node]

            if total <= total_sp:
                left = mid
            else:
                right = mid - 1

        return left

    # 최적의 리프 노드 값 찾기
    leaf_value = find_min_leaf_value()

    # 결과 배열 생성
    result = [0] * (max_node + 1)
    for leaf in leaves:
        result[leaf] = leaf_value

    # 나머지 노드 값 계산
    non_leaves = set(range(1, max_node + 1)) - set(leaves)
    for node in sorted(non_leaves, reverse=True):
        if children[node]:
            result[node] = sum(result[child] for child in children[node])

    return result[1:]  # 0번 인덱스 제외하고 반환

total_sp = 121
skills = [[1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]
print(solution(total_sp, skills))
