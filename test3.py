import math

def solution(x, y, r, d, target):
    count = 0
    base_angle = math.atan2(y, x)
    if base_angle < 0:
        base_angle += 2 * math.pi
    d_radian = math.radians(d)
    for mx, my in target:
        distance = math.sqrt(mx**2 + my**2)
        if distance > r:
            continue
        monster_angle = math.atan2(my, mx)
        if monster_angle < 0:
            monster_angle += 2 * math.pi
        angle_diff = abs(monster_angle - base_angle)
        if angle_diff > math.pi:
            angle_diff = 2 * math.pi - angle_diff
        if angle_diff <= d_radian:
            count += 1
    return count

x = -1
y = 2
r = 2
d = 60
target = [[0, 1], [-1, 1], [1, 0], [1, -2], [-2, -2]]

result = solution(x, y, r, d, target)
print(result)
""""""