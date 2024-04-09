class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        iterations = 0
        idx = 0
        length = len(tickets)
        while tickets[k] > 0:
            if tickets[idx] != 0:
                tickets[idx] -= 1
                iterations += 1
            
            if idx < length-1:
                idx += 1
            elif idx == length-1:
                idx = 0
        return iterations