class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        seen = defaultdict(list)

        for i, string in enumerate(strs):
            key = "".join(sorted(string))
            seen[key].append(string)
        return list(seen.values())