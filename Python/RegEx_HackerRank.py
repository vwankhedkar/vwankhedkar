import re
str = "The rain in Spain"
print(re.findall(" ",str))
print(re.search(" ",str))
print(re.findall("ain",str))
print(re.search("ain",str))
print(re.split(" ", str))
print(re.sub(" ", "5", str))
x = re.search(r"\bS\w+", str)
print(x.span(), end=" ")
x = re.search(r"\bS\w+", str)
print(x.string)
print(x.group())
[' ', ' ', ' ']
<re.Match object; span=(3, 4), match=' '>
['ain', 'ain']
<re.Match object; span=(5, 8), match='ain'>
['The', 'rain', 'in', 'Spain']
The5rain5in5Spain
(12, 17) The rain in Spain
Spain
\A Returns a match if the specified characters are at the beginning of string
\b  Returns a match where the specified characters are at the
 beginning or at the end of a word
\B Returns a match where the specified characters are present, but
 NOT at the beginning (or at the end) of a word
 \d Returns a match where the string contains digits (numbers from
 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space
 character
\S Returns a match where the string DOES NOT contain a white
 space character
\w Returns a match where the string contains any word characters
 (characters from a to Z, digits from 0-9, and the underscore _
 character)
\W Returns a match where the string DOES NOT contain any word
 characters
\Z Returns a match if the specified characters are at the end of the
 string
***********************************************************************************
import re
pattern = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
IPv4 = re.compile(rf'^{pattern}\.{pattern}\.{pattern}\.{pattern}$')
IPv6 = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
def classify(addr):
    if IPv4.fullmatch(addr):
        return "IPv4"
    if IPv6.fullmatch(addr):
        return "IPv6"
    return "Neither"

N = int(input())
for _ in range(N):
    line = input()
    print(classify(line))
Input (stdin)
7
1050:1000:1000:a000:5:600:300c:326b
1050:1000:2000:ab00:5:600:300c:326a
1050:1000:3000:abc0:5:600:300c:326c
1051:1000:4000:abcd:5:600:300c:326b
22.231.113.64
22.231.113.164
222.231.113.64
Your Output (stdout)
IPv6
IPv6
IPv6
IPv6
IPv4
IPv4
IPv4
Expected Output
IPv6
IPv6
IPv6
IPv6
IPv4
IPv4
IPv4
******************************************************************
