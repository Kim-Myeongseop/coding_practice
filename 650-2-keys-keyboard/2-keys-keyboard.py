class Solution:
    def minSteps(self, n: int) -> int:
        factors = []
        factor = 2
        while factor <= n:   # n이 계속 바뀌기 때문(n이 고정이라면 factor**2 <= n 까지만 확인해보면된다.)
            if n%factor == 0:   # 작은 값부터 확인하므로 소수만 확인할 수 있다.
                factors.append(factor)   # factor 로 못 나눌 때까지 나눈다.(복수)
                n = n//factor
            else:
                factor += 1   # factor로 못나누면 다음 factor 확인
        return sum(factors)

'''
ex) n = 24

처음은 무조건 copy로 시작해야하고, copy를 한다는 것은 1배를 한다고 해석할 수 있다.
paste를 할 때 마다 배수를 한 번씩 늘린다고 생각하면 된다.
copy는 가장 최근에 저장한 값 하나만 저장할 수 있기 때문에 결국 24를 만드려면,
24의 약수를 저장해야한다.
이때, 3 * 8 이라고 생각한다면, 총 3번(cpp) + 8번(cppppppp) 를 해야 24개를 만들 수 있다.
즉, 24를 인수들의 곱으로 분해하고 그 인수의 합이 정답이 된다.
띠리서 모든 인수로 분해하는 것이 가장 많은 곱으로 나타낼 수 있고, 합이 최소가 된다.

3 * 2 * 2 * 2
copy = 'A'
paste : 'AA'
paste : 'AAA'

copy = 'AAA'
paste : 'AAAAAA'

copy = 'A' * 6
paste : 'A' * 12

copy = 'A' * 12
paste : 'A' * 24
'''