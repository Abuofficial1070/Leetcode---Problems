class Solution(object):
    def missingNumber(self, nums):
        i=0
        n=len(nums)
        while i<n:
            corr_pos=nums[i]
            if corr_pos<n and nums[i]!=nums[corr_pos]:
                nums[i],nums[corr_pos]=nums[corr_pos],nums[i]
            else:
                i+=1
        for i in range(0,len(nums)):
            if nums[i]!=i:
                return i
        return n
        