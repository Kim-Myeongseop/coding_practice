class Solution:    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        answer = []
        dictionary = sorted(dictionary, key=lambda x: len(x))
        sentence = sentence.split()
        for word in sentence:   # cattle
            for root in dictionary:
                if len(root) > len(word):
                    sign = False
                    continue
                sign = True
                for i in range(len(root)):
                    if root[i] != word[i]:
                        sign = False
                        break
                if sign:
                    answer.append(root)
                    break
            if not sign:
                answer.append(word)
        return ' '.join(answer)

