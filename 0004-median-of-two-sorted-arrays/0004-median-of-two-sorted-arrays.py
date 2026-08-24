class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        total_len=m+n
        half_len = (total_len+1)//2
        low,high=0,m
        while low<=high:
            i=(low+high)//2
            j=half_len  - i
            nums1_leftmax = float('-inf') if i==0 else nums1[i - 1]
            nums1_rightmin = float('inf') if i==m else nums1[i]

            nums2_leftmax = float('-inf') if j==0 else nums2[j - 1]
            nums2_rightmin = float('inf') if j==n else nums2[j]
            if nums1_leftmax <= nums2_rightmin and nums2_leftmax <= nums1_rightmin:
                if total_len % 2 == 1:
                    return float(max(nums1_leftmax,nums2_leftmax))
                else:
                    return (max(nums1_leftmax,nums2_leftmax)+ min(nums1_rightmin,nums2_rightmin))/2.0
            elif nums1_leftmax > nums2_rightmin:
                high=i-1
            else:
                low=i+1
        
            