class Solution(object):
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n // 2):
            temp = s[i]
            s[i] = s[n - 1 - i]
            s[n - 1 - i] = temp