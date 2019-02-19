class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        while x>=10:
            y=x
            div=1
            while y>=10:
                y=y/10
                div*=10
            right=x%10
            left=int(x/div)
            if right!=left:
                return False
            x=int((x-right*div)/10)
            while x<=div/10:
                if x%10!=0:
                    return False
                x=x/10
                div=div/10
        return True
p=Solution()
print p.isPalindrome(1000021)
