def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
        
    return answer

# 다른 풀이 1 : 시간 초과 발생
# def solution(A,B):
#     minimum = 0
#     for idx in range(len(B)):
#         minimum += A[idx] * B[idx]
    
#     c = [0] * len(A)
#     i = 0
#     while i < len(A):
#         if c[i] < i:
#             if i%2 == 0:
#                 A[0], A[i] = A[i], A[0]
#             else:
#                 A[c[i]], A[i] = A[i], A[c[i]]
#             temp = 0
#             for idx in range(len(B)):
#                 temp += A[idx] * B[idx]
#             if temp < minimum:
#                 minimum = temp
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
            
#     return minimum