class Solution:
    def lengthOfLastWord(s):
        counter = 0
        letters_started = False
        for letter in s[::-1]:
            if not letters_started and not letter.isspace():
                letters_started = True
            if letters_started and letter.isalpha():
                counter += 1
            elif letters_started:
                break
        return counter
s = "Hello World"
print(Solution.lengthOfLastWord(s))
s = "   fly me   to   the moon  "
print(Solution.lengthOfLastWord(s))
s = "luffy is still joyboy"
print(Solution.lengthOfLastWord(s))
