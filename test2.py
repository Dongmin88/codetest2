def solution(P, N):
    ampm, time = P.split()
    hour, minute, second = map(int, time.split(':'))
    
    if ampm == "PM" and hour != 12:
        hour += 12
    elif ampm == "AM" and hour == 12:
        hour = 0
    
    total_seconds = hour * 3600 + minute * 60 + second
    total_seconds += N
    total_seconds %= 86400  
    
    hour = total_seconds // 3600
    total_seconds %= 3600
    minute = total_seconds // 60
    second = total_seconds % 60
    
    return f"{hour:02d}:{minute:02d}:{second:02d}"

P = "PM 01:00:00"
N = 10
print(solution(P, N))

P = "PM 11:59:59"
N = 1
print(solution(P, N))