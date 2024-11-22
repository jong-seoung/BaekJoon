def solution(genres, plays):
    genre_play_count = {}
    for genre, play in zip(genres, plays):
        if genre not in genre_play_count:
            genre_play_count[genre] = 0
        genre_play_count[genre] += play

    genre_songs = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, i))  

    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)

    answer = []
    for genre in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([idx for _, idx in songs[:2]])

    return answer
