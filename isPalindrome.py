import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s).lower()
        left = 0
        right = len(s) - 1

        while (left < right):
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True

string = "A man, a plan, a canal: Panama"
b = Solution()
print(b.isPalindrome(string))
**********************************************************
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s).lower()
        rev = ""
        for i in range(len(s)):
            rev += s[i]
            i -= 1
        return rev == s

string = "A man, a plan, a canal: Panama"
b = Solution()
print(b.isPalindrome(string))
