class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        if dividend < 0:
            flag = -1
            dividend = - dividend
        
        if divisor < 0:
            if flag == -1:
                flag = 1
                divisor = -divisor
            else:
                flag = -1
                divisor = -divisor
                
        result = 0
        while dividend>=divisor:
            n=0
            while (divisor<<n) <= dividend:
                n+=1
            dividend -= divisor<<(n-1)
            result += 1<<(n-1)
        
        if result > 2147483647 and flag == 1:
            result = 2147483647
        elif result >2147483648 and flag == -1:
            result = 2147483648
        
        if flag == -1:
            return -result
        else:
            return result
        
