class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {}
        string2 = {}
        for char in s:
            if char in string1:
                string1[char] = string1[char] + 1
            else:
                string1[char] = 1
        for char in t:
            if char in string2:
                string2[char] = string2[char] + 1
            else:
                string2[char] = 1
        if string1 == string2:
            return True
        else:
            return False