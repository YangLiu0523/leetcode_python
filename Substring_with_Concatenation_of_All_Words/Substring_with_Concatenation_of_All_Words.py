class Solution(object):
    def findSubstring_mine(self, s, words):
        len_words = len(words)
        if words == []:
            return []
        len_word = len(words[0])
        wordsOnce = copy.deepcopy(words)
        end = 0
        i=0
        result = []
        
        while i < len(s)-len_words*len_word+1:
            
            while s[end:end+len_word] in wordsOnce:
                del wordsOnce[wordsOnce.index(s[end:end+len_word])]
                end += len_word
            if len(wordsOnce) == 0:
                result.append(i)
                wordsOnce.append(s[i:i+len_word])
                i += len_word
            elif len(wordsOnce) == len(words):
                i += len_word
                end = i
            else:
                wordsOnce.append(s[i:i+len_word])
                i+=len_word
        return result
    def findSubstring(self,s,words):
        result = []
        for i in range(len(words[0])):
            result_now = self.findSubstring_mine(s[i:],words)
            print i,result_now
            for j in result_now:
                if not i+j in result:
                    result.append(i+j)
        return result
