class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            count = target - j
            if count in seen:
                return [seen[count], i]
            seen[j]= i