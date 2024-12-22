def solution(movie):
    movie_count = {}
    for m in movie:
        if m in movie_count:
            movie_count[m] += 1
        else:
            movie_count[m] = 1
    
    sorted_movies = sorted(movie_count.keys(), 
                         key=lambda x: (-movie_count[x], x))
    
    return sorted_movies

movie = ["spy", "ray", "spy", "room", "once", "ray", "spy", "once"]
print(solution(movie))  