class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memoization = {}
        def compute(expression):
            if expression in memoization:
                return memoization[expression]
            result = []
            
            for i in range(len(expression)):
                c = expression[i]
                if c in '+-*':
                    left_result = compute(expression[:i])
                    right_result = compute(expression[i+1:])
                    for left_case in left_result:
                        for right_case in right_result:
                            if c == '+':
                                result.append(left_case + right_case)
                            elif c == '-':
                                result.append(left_case - right_case)
                            else:
                                result.append(left_case * right_case)
            
            if not result:   # 아무 값도 추가 되지 않았으면 : expression에 연산자가 없음 즉, 숫자만 남음
                result.append(int(expression))

            memoization[expression] = result
            return result
        return compute(expression)

        '''
        Devide and Conquer
        compute 함수를 만든다. 표현식으로 만들 수 있는 결과를 list로 return
        n개의 연산자가 있다면, 각 연산자 기준으로 왼쪽 식과 오른쪽 식을 나눠서 계산하고,
        왼쪽 식의 list의 원소와 오른쪽 식의 list의 원소를 조합하여 최종 결과를 만드는 방식으로 합친다.
        
        Memoization
        여기에 표현식을 key로, 이에 대응되는 결과 list를 value로 하여 dict에 저장하여 중복 연산 방지

        예를 들어, 
        연산자가 3개라면 각 연산자에 대해 좌우를 나눈다.
        연산자가 1개거나 숫자만 있으면 계산하면 된다.
        2개 이상이면 똑같이 연산자 2개에 대해 for문을 돌면 된다.
        '''
