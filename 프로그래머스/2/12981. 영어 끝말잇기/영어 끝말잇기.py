def solution(n, words):
    answer = [0,0]
    word_list = []
    last_char = words[0][0]
    for i, word in enumerate(words):
        if word not in word_list:   # 단어장에 없으면 진행
            if word[0] == last_char:
                last_char = word[-1]
                word_list.append(word)
            else:   # wrong word
                answer = [i%n + 1, (i-i%n)/n + 1]
                break
            
        else:   #  단어장에 있는 단어가 오면
            answer = [i%n + 1, (i-i%n)/n + 1]   # i+1 번째 단어
            break

    return answer