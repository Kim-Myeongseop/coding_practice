def solution(genres, plays):
    answer = []
    hash_table = {}
    max_genre = {}
    for i in range(len(genres)):
        if hash_table.get(genres[i]):
            hash_table[genres[i]].append(i)
            max_genre[genres[i]] += plays[i]
        else:
            hash_table[genres[i]] = [i]
            max_genre[genres[i]] = plays[i]
    for genre in sorted(max_genre, key=lambda x: max_genre[x], reverse=True):
        answer.extend(sorted(hash_table[genre], key=lambda x: (plays[x], -x), reverse=True)[:2])
    return answer