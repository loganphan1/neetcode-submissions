class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1= {}
        string2 = {}

        for char in s:
            string1[char] = string1.get(char,0)+1
        for char in t:
            string2[char] = string2.get(char,0)+1
        return string1==string2