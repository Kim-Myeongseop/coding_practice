# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         import math
#         if len(points) == 1:
#             return 1
#         point_dict = {}
#         for i in range(len(points)):
#             for j in range(len(points)):
#                 if i != j:
#                     if points[i][0] != points[j][0]:   # x좌표가 같지 않으면 기울기가 실수
#                         a = (points[i][1]-points[j][1]) / (points[i][0]-points[j][0])
#                         b = round(max(points[i][1] - a*points[i][0], points[j][1] - a*points[j][0]), 2)
#                     else:   # x좌표가 같으면 기울기가 무한대 / y절편 대신 x절편으로 직선을 구분
#                         a = 'inf'
#                         b = points[i][0]   # 이때는 x 좌표 기입

#                     if (a,b) not in point_dict:
#                         point_dict[(a,b)] = 1
#                     else:
#                         point_dict[(a,b)] += 1

#         print(point_dict)                        
#         answer = sorted(point_dict.items(), key=lambda x: x[1], reverse=True)[0][1]
#         answer = int(sqrt(answer + 1/4) + 1/2)

#         return answer

from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        D = defaultdict(set)
        if N <= 2:
            return N 
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                if y1 == y2:
                    k1, k2 = 'inf', y1
                elif x1 == x2:
                    k1, k2 = x1, 'inf'
                else:
                    k1, k2 = (x1-x2)/(y2-y1), (x2*y1-x1*y2)/(y2-y1)
                D[(k1,k2)].add(tuple(points[i]))
                D[(k1,k2)].add(tuple(points[j]))
        return max([len(i) for i in D.values()])