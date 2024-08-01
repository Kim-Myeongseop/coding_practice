class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def check(code):
            return True if int(code[-4:-2]) > 60 else False
            
        answer = 0
        for person in details:
            if check(person):
                answer += 1
        return answer
        