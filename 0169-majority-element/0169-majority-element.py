class Solution(object):
    def majorityElement(self, nums):
        fr={}
        for i in nums:
            if i in fr:
                fr[i]+=1
            else:
                fr[i]=1
        for key in fr:
            if fr[key]>len(nums)//2:
                return key
        