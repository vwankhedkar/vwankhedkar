def isPalindrome(x):
    if x < 0:
        return False
    digit, n = 0, x
    while n:
        n, r = divmod(n, 10)
        print(n, r)
        digit = digit * 10 + r
    return digit == x
print(isPalindrome(121))
-------------------------------------
def isPalindrome(x):
    if x < 0:
        return False
    reverse = 0
    temp = x
    while temp:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
        print(reverse, temp)
    return reverse == x
print(isPalindrome(121))

OUTPUT : True
