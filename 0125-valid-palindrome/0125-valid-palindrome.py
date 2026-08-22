class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        count = clean[::-1]
        if clean == count:
            return True
        else:
            return False

        