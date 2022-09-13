class Solution:
    def longestCommonPrefix(strs):
        prefix = ''
        L = min([len(s) for s in strs])
        for i in range(L):
            ci = strs[0][i]
            for s in strs[1:]:
                if ci != s[i]:
                    return prefix
            prefix += ci
        return prefix
strs = ["flower","flow","flght"]
print(Solution.longestCommonPrefix(strs))
OUTPUT: ["flower","flow","flight"]
"fl"
