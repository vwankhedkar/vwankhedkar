class Solution:
    def addBinary(a: str, b: str) -> str:
        total = int(a) + int(b)
        if total == 0:
            return "0"
        carry = 0
        result = ""
        while total > 0:
            lastdigit = total % 10 + carry
            binary, carry = lastdigit % 2, lastdigit // 2
            result += str(binary)
            total = total // 10
        if carry != 0:
            result += str(carry)
        return result[::-1]
print(Solution.addBinary('11','1'))
Output : 100
