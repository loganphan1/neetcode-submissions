class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ", "")
        s= "".join([c for c in s if c.isalnum()])
        return s[::-1] == s
      
        