class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        digits_s = [0] * 10
        digits_g = [0] * 10
        for c, d in zip(secret, guess):
            if c == d:
                bull += 1
            else:
                digits_s[int(c)] += 1
                digits_g[int(d)] += 1
        
        cow = 0
        for i in range(10):
            cow += min(digits_s[i], digits_g[i])
        return str(bull) + 'A' + str(cow) + 'B'
        
