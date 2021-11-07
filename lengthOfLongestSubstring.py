class Solution:

    def lengthOfLongestSubstring(self, s):
        last_idx = {}
        max_len = 0
        start_idx = 0

        for i in range(0, len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]]+1)
            max_len = max(max_len, i-start_idx+1)
            last_idx[s[i]] = i
        return max_len                

b = Solution()
strg = "pwwkew"
print(b.lengthOfLongestSubstring(strg))
********************************************************************
class Solution:

    def lengthOfLongestSubstring(self, s):
        size = len(s)
        if size <= 1:
            return size

        for left in range(size):
            longest = 0
            seenChar = {}
            currentLength = 0
            sub = ""
            for right in range(left, size):
                currentChar = s[right]
                if currentChar not in seenChar:
                    currentLength += 1
                    seenChar[currentChar] = True
                    longest = max(longest, currentLength)
                    sub += currentChar
                else:
                    break
            return longest, sub

b = Solution()
strg = "abcdeabcbb"
print(b.lengthOfLongestSubstring(strg))
***************************************************************************
def lengthOfLongestSubstring(s):
    size = len(s)
    longest = 0

    if size <= 1:
        return size

    for left in range(size):
        seenChars = {}
        currentLength = 0
        for right in range(left, size):
            currentChar = s[right]

            if currentChar in seenChars:
                break
            else:
                currentLength += 1
                seenChars[currentChar] = True
                longest = max(longest, currentLength)
    return longest

if __name__ == '__main__':
    s = "abcdabcbb"
    print(lengthOfLongestSubstring(s))
