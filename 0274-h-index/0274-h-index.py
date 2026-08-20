class Solution(object):
    def hIndex(self, citations):
        citations = self.mergeSort(citations)

        n = len(citations)
        h = 0
        for i in range(n):
            papers = n - i
            if citations[i] >= papers:
                h = papers
                break
        return h
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res