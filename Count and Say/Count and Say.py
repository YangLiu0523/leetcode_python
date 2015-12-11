class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = 1
        say = '1'
        
        while count < n:
            a = []
            b = []
            m = 0
            newsay = ''
            for i in range(len(say)):
                if i == 0 :
                    a.append(1)
                    b.append(say[0])
                    continue
                if say[i] == say[i-1]:
                    a[m] += 1
                else:
                    b.append(say[i])
                    a.append(1)
                    m+=1
            for i in range(len(a)):
                newsay = newsay + str(a[i]) + str(b[i])
            say = newsay
            count += 1
        
        return say
