from itertools import combinations

def solution(orders, course):
    answer = []
    
    course_list = [{} for _ in range(len(course))]
    for order in orders:
        for i in range(len(course)):
            for case in combinations(order, course[i]):
                case = ''.join(sorted(case))
                course_list[i][case] = course_list[i].get(case, 0) + 1
    
    for c in course_list:
        for key in c:
            if c[key] == max(c.values()) and c[key] > 1:
                answer.append(key)
    return sorted(answer)