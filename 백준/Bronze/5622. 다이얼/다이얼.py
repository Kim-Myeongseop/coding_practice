import sys
from string import ascii_uppercase
#input = sys.stdin.readline

num_list = [3]*3 + [4]*3 + [5]*3 + [6]*3 + [7]*3 + [8]*4 + [9]*3 + [10]*4
dial_dict = {ascii_uppercase[i]:num_list[i] for i in range(len(num_list))}

num_string = input()

answer = 0
for c in num_string:
    answer += dial_dict[c]

print(answer)

