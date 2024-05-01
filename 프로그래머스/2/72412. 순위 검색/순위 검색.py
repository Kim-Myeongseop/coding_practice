from bisect import bisect_left

def solution(info, query):
    answer = []
    # 언어 3가지 : cpp, java, python : 24로 나눠서 나머지 0~7 / 8~15 / 16~23
    # 직군 2가지 : backend, frontend : 8로 나눠서 나머지 0,1,2,3 / 4,5,6,7
    # 경력 2가지 : junior, senior : 4로 나눠서 나머지 0,1 / 2,3
    # 음식 2가지 : chicken, pizza : 2로 나눠서 나머지 0,1
    word_dict = {"cpp":"0", "java":"1", "python":"2",
                 "backend":"0", "frontend":"1",
                 "junior":"0", "senior":"1",
                 "chicken":"0", "pizza":"1"}
    score_dict = {}
    sign_dict = {}
    for i in info:
        a, b, c, d, score = i.split()
        key = ''.join([word_dict[a], word_dict[b], word_dict[c], word_dict[d]])
        if score_dict.get(key):
            score_dict[key].append(int(score))
        else:
            score_dict[key] = [int(score)]
            sign_dict[key] = 0
    # print(score_dict)
    
    for q in query:
        # print(q.split())   # 0, 2, 4, 6, 7
        num_people = 0
        lang, _, job, _, year, _, food, score = q.split()
        score = int(score)
        lang = ["cpp","java","python"] if lang=='-' else [lang]
        job = ["backend","frontend"] if job=='-' else [job]
        year = ["junior","senior"] if year=='-' else [year]
        food = ["chicken","pizza"] if food=='-' else [food]
        for a in lang:
            for b in job:
                for c in year:
                    for d in food:
                        key = ''.join([word_dict[a], word_dict[b], word_dict[c], word_dict[d]])
                        if sign_dict.get(key) == None:
                            continue
                        if sign_dict[key] == 0:
                            score_dict[key].sort()
                            sign_dict[key] = 1
                        # 이진 탐색
                        search_arr = score_dict[key]
                        # l = 0
                        # r = len(search_arr) - 1
                        # while l <= r:
                        #     if search_arr[(r+l)//2] == score:
                        #         l = (r+l)//2
                        #         break
                        #     elif search_arr[(r+l)//2] > score:
                        #         r = (r+l)//2 - 1
                        #     else:
                        #         l = (r+l)//2 + 1
                        l = bisect_left(search_arr, score)
                        res = len(search_arr) - l
                        num_people += res
                        
        answer.append(num_people)
    return answer