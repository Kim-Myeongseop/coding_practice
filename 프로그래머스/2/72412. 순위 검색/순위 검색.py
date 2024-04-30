from bisect import bisect_left

def solution(info, query):
    a = {"java":"0", "cpp":"1", "python":"2"}
    b = {"backend":"0", "frontend":"1"}
    c = {"junior":"0", "senior":"1"}
    d = {"chicken":"0", "pizza":"1"}

    results = []
    for i in info:
        lang, posi, car, food, score = i.split(" ")
        results.append([a[lang], b[posi], c[car], d[food], int(score)])

    r = {}
    for result in results:
        _d = "".join(result[:4])
        if (r.get(_d)):
            r[_d].append(result[4])
        else:
            r[_d] = [result[4]];
    # print(r)    

    answer = []
    s_dp = {}
    for __i in r.keys():
        s_dp[__i] = False

    for q in query:
        lang, posi, car, f = q.split(" and ")
        food, score = f.split(" ")
        u1 = []; u2 = []; u3 = []; u4 = []
        if (lang == "-"):
            u1.append("0"); u1.append("1"); u1.append("2");
        else:
            u1.append(a[lang])

        if (posi == "-"):
            u2.append("0"); u2.append("1");
        else:
            u2.append(b[posi])

        if (car == "-"):
            u3.append("0"); u3.append("1");
        else:
            u3.append(c[car])

        if (food == "-"):
            u4.append("0"); u4.append("1");
        else:
            u4.append(d[food])

        count = 0
        for _u1 in u1:
            for _u2 in u2:
                for _u3 in u3:
                    for _u4 in u4:
                        s = _u1 +_u2 + _u3 + _u4
                        if r.get(s):
                            arr = r[s]
                            # print(arr)
                            if not s_dp[s]:
                                arr.sort()
                                s_dp[s] = True
                            f = bisect_left(arr,int(score))
                            count += len(arr) - f
        answer.append(count)
    return answer

# def solution(info, query):
#     answer = []
#     # 언어 3가지 : cpp, java, python : 24로 나눠서 나머지 0~7 / 8~15 / 16~23
#     # 직군 2가지 : backend, frontend : 8로 나눠서 나머지 0,1,2,3 / 4,5,6,7
#     # 경력 2가지 : junior, senior : 4로 나눠서 나머지 0,1 / 2,3
#     # 음식 2가지 : chicken, pizza : 2로 나눠서 나머지 0,1
#     word_dict = {"cpp":"0", "java":"1", "python":"2",
#                  "backend":"0", "frontend":"1",
#                  "junior":"0", "senior":"1",
#                  "chicken":"0", "pizza":"1"}
#     score_dict = {}
#     sign_dict = {}
#     for i in info:
#         a, b, c, d, score = i.split()
#         key = ''.join([word_dict[a], word_dict[b], word_dict[c], word_dict[d]])
#         if score_dict.get(key):
#             score_dict[key].append(int(score))
#         else:
#             score_dict[key] = [int(score)]
#             sign_dict[key] = 0
#     # print(score_dict)
    
#     for q in query:
#         # print(q.split())   # 0, 2, 4, 6, 7
#         num_people = 0
#         lang, _, job, _, year, _, food, score = q.split()
#         score = int(score)
#         lang = ["cpp","java","python"] if lang=='-' else [lang]
#         job = ["backend","frontend"] if job=='-' else [job]
#         year = ["junior","senior"] if year=='-' else [year]
#         food = ["chicken","pizza"] if food=='-' else [food]
#         for a in lang:
#             for b in job:
#                 for c in year:
#                     for d in food:
#                         key = ''.join([word_dict[a], word_dict[b], word_dict[c], word_dict[d]])
#                         if sign_dict.get(key) == None:
#                             continue
#                         if sign_dict[key] == 0:
#                             score_dict[key].sort()
#                             sign_dict[key] = 1
#                         # 이진 탐색
#                         search_arr = score_dict[key]
#                         l = 0
#                         r = len(search_arr) - 1
#                         while l <= r:
#                             if search_arr[(r+l)//2] == score:
#                                 l = (r+l)//2
#                                 # res = len(search_arr) - (r+l)//2
#                                 break
#                             elif search_arr[(r+l)//2] > score:
#                                 r = (r+l)//2 - 1
#                             else:
#                                 l = (r+l)//2 + 1
#                         res = len(search_arr) - l
#                         # if l > len(search_arr) - 1:
#                         #     res = 0
#                         # if r < 0:
#                         #     res = len(search_arr)
#                         # if l <= len(search_arr) - 1 and r >= 0 and l > r:
#                         #     res = len(search_arr) - l
#                         num_people += res
#         answer.append(num_people)
#     return answer