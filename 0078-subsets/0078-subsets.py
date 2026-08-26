class Solution:
    def subsets(self, nums):
        result = [[]]

        for num in nums:
            new = []

            for subset in result:
                new.append(subset + [num])

            result += new

        return result