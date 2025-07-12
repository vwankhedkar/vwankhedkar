def memoize(fn):
    cache = {}
    def helper(x):
        if x not in cache:
            # The @memoize decorator is used to cache the results of the factorial function. 
            cache[x] = fn(x)
        return cache[x]
    return helper
@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(3)
print(result)    ===>  6
***********************************************************************
def caesar_cipher(text, shift) :
    result = ""
    for char in text:
        if char.isalpha() :
            # Determine if the character is uppercase or lowercase
            is_upper = char. isupper()
            char = char.lower() # Convert to lowercase for shifting
            shifted = chr(((ord(char) - ord('a' ) + shift) % 26) + ord( 'a' ))
            if is_upper:
                shifted = shifted.upper() # Convert back to uppercase
                result += shifted
            else:
                result += char # Non-alphabet characters remain unchanged
    return result
# Example usage:
text = "Hello, World! "
shift = 3
encrypted = caesar_cipher(text, shift)
decrypted = caesar_cipher(encrypted, -shift)
print("Original: " , text)
# Original: Hello, World!
print("Encrypted: " , encrypted)
print("Decrypted: ", decrypted) # Decrypted: Hello, World!
C:\Users\vwank\PycharmProjects\Python_Cucumber\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\Python_Cucumber\.venv\Scripts\tryPyProgs.py 
Original:  Hello, World! 
Encrypted:  KelloZorld
Decrypted:  HelloWorld
************************************************************************************************
package com.tryPrograms;
public class RemoveDuplicates {
	public static int findMissingNumber(int[] arr, int n) {
		int expectedSum = n * (n + 1) / 2;
		int actualSum = 0;
		for (int num : arr) {
			actualSum += num;
		}
		return expectedSum - actualSum;
	}
	public static void main(String[] args) {
		int[] numbers = {1, 2, 4, 6, 3, 7, 8};
		int n = 8; 
		System.out.println("Missing number : " +findMissingNumber(numbers, n));
	}
}    =====>    Missing number : 5
************************************************************************************************
package com.tryPrograms;
public class RemoveDuplicates {
	public static boolean areAnagram(String str1, String str2) {
		str1 = str1.replaceAll("\\s", "").toLowerCase();
		str2 = str2.replaceAll("\\s", "").toLowerCase();
		if (str1.length() != str2.length()) {
			return false;
		}
		char[] charArray1 = str1.toCharArray();
		char[] charArray2 = str2.toCharArray();
		java.util.Arrays.sort(charArray1);
		java.util.Arrays.sort(charArray2);
		return java.util.Arrays.equals(charArray1, charArray2);
	}
	public static void main(String[] args) {
		String s1 = "Listen";
		String s2 = "Silent";
		System.out.println("\""+s1 + "\" and \"" + s2 + "\" are anagrams:" +areAnagram(s1,s2));
	}
}  ===>    "Listen" and "Silent" are anagrams:true
************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************
************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************
