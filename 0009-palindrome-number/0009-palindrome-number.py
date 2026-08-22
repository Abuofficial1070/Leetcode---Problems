class Solution:
    def isPalindrome(self, x: int) -> bool:
        count = 0 
        temp=x
        while x>0:
            y=x%10
            count=count*10 +y
            x=x//10
        return temp==count
        