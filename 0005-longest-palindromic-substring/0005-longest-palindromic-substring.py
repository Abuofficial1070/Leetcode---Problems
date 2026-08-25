class Solution:
    def longestPalindrome(self, s):
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]
        longest = ""
        for i in range(len(s)):
            odd = expandAroundCenter(i, i)   
            even = expandAroundCenter(i, i + 1)
            if len(odd) > len(even):
                current_longest = odd
            else:
                current_longest = even
            if len(current_longest) > len(longest):
                longest = current_longest
        return longest