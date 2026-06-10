class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        seen = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            seen[key].append(string)
        return list(seen.values())