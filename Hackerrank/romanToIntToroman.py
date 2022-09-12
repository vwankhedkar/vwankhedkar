class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5: 'V',
            4 : 'IV',
            1 : 'I'
        }
        ans = ""
        for key in dict.keys():
            val = num // key #Floor devide
            ans += val * dict[key]
            num -= val * key
        return ans
OUTPUT : 3
"III"
*************************************************************************
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i = 0
        while i < len(s):
            if i < len(s)-1 and d[s[i]] < d[s[i+1]]:
                ans += d[s[i+1]] - d[s[i]]
                i += 1
            else:
                ans += d[s[i]]
            i += 1
        return ans
OUTPUT: III
3
