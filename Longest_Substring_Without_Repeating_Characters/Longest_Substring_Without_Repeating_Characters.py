class Solution:
    #@return an integer
    def lengthOfLongestSubstring(self,s):
        lastRepeating=-1
        longestSubstring=0
        positions={}
        for i in range(0,len(s)):
            if s[i] in positions and lastRepeating<positions[s[i]]:
                lastRepeating=positions[s[i]]
            if i-lastRepeating>longestSubstring:
                longestSubstring=i-lastRepeating
            positions[s[i]]=i
        return longestSubstring
