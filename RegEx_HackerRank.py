
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
