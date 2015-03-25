#!/usr/bin/python
#Filename:Integer_To_Roman.py

class Solution:
    def intToRoman(self,num):
        if num<=0 or num>=4000:
            return ''
        result=''
        s1=['','I','II','III','IV','V','VI','VII','VIII','IX','X'];
        s10=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC','X'];
        s100=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM','M'];
        s1000=['','M','MM','MMM'];
        result=s1000[int(num/1000)]
        num=num-int(num/1000)*1000
        result=result+s100[int(num/100)]
        num=num-int(num/100)*100
        result=result+s10[int(num/10)]
        num=num-int(num/10)*10
        result=result+s1[num]
        return result

print Solution().intToRoman(123)
