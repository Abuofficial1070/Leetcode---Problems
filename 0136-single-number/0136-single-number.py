class Solution(object):
    def singleNumber(self, nums):
        s={}
        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        for i in nums:
            if s[i]==1:
                return i