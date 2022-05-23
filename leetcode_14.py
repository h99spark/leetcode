class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        for i, c in enumerate(strs[0]):
            for word in strs[1:]:
                if c != word[i]:
                    return strs[0][:i]
        return strs[0]

