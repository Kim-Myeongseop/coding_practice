class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        word_list = []
        sent_len = 0

        for word in words:
            sent_len += len(word)

            if sent_len+len(word_list)-1 < maxWidth:
                word_list.append(word)
            else:
                if len(word_list) == 1:
                    sentence = word_list[0]
                    sentence += ' '*(maxWidth-len(word_list))
                
                else:
                    a = (maxWidth-sent_len+len(word)) // (len(word_list)-1)
                    b = (maxWidth-sent_len+len(word)) % (len(word_list)-1)
                    sentence = (' '*a).join(word_list)
                    sentence = sentence.replace(' '*a, ' '*(a+1), b)
                
                sentence = sentence[:maxWidth]
                result.append(sentence)

                word_list = [word]
                sent_len = len(word)

        last_sent = ' '.join(word_list)
        result.append(last_sent + ' '*(maxWidth-len(last_sent)))

        return result


