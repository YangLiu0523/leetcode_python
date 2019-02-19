class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        length = len(words[0])
        num = len(words)
        result = []
        for i in range(0,len(s)+1-length*num,length):
            now = i
            wordsOnce = copy.deepcopy(words)
            
            while len(wordsOnce) > 0:
                if s[i:i+length] in wordsOnce:
                    del wordsOnce[wordsOnce.index(s[i:i+length])]
                    i += length
                else:
                    break
            if len(wordsOnce) == 0:
                result.append(now)                
        return result
