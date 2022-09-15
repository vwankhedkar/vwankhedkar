class Solution:
    def plusOne(digits):
        return str(int(''.join([str(i) for i in digits]))+1)
------------------------------------------------------------
class Solution:
    def plusOne(digits):
        finded = False
        index = -1
        last_index = 0
        while True:
            if not finded:
                try:
                    digits[index]
                except IndexError:
                    digits.insert(index,0)
                    finded = True
                    last_index = 0
                    continue
                if digits[index] != 9:
                    finded = True
                else:
                    index = -1
            else:
                digits[index] = digits[index]+1
                for i in range(index+1, last_index):
                    digits[i] = 0
                break
        return digits

digits = [4,3,2,1]
print(Solution.plusOne(digits))
digits = [1,2,3]
print(Solution.plusOne(digits))
digits = [9]
print(Solution.plusOne(digits))
