//Method Overriding
package WebHandling;
class Bank{
	int getRateOfInterest() {return 0;}
}
class SBI extends Bank {
	int getRateOfInterest() {return 8;}
}
class ICICI extends Bank {
	int getRateOfInterest() {return 7;}
}
class AXIS extends Bank {
	int getRateOfInterest() {return 9;}
}
public class tryProgs2 {
    public static void main(String[] args) {
    	SBI s = new SBI();
    	ICICI i = new ICICI();
    	AXIS a = new AXIS();
        System.out.println("SBI Rate of Interest: "+ s.getRateOfInterest());
        System.out.println("ICICI Rate of Interest: "+ i.getRateOfInterest());
        System.out.println("AXIS Rate of Interest: "+ a.getRateOfInterest());
    }
}
SBI Rate of Interest: 8
ICICI Rate of Interest: 7
AXIS Rate of Interest: 9
************************************************************************************
package WebHandling;
import java.util.Hashtable;
import java.util.Map;
public class tryProgs2 {
    public static void main(String[] args) {
        Hashtable<Integer, String> ht = new Hashtable<Integer, String>();
        ht.put(100, "Rajendra");
        ht.put(102, "Praveen");
        ht.put(101, "Bipin");
        ht.put(103, "Pankaj");
        for (Map.Entry<Integer, String> entry : ht.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
103 Pankaj
102 Praveen
101 Bipin
100 Rajendra
************************************************************************************
package WebHandling;
import java.util.TreeMap;
import java.util.Map;
public class tryProgs2 {
    public static void main(String[] args) {
        TreeMap<Integer, String> ht = new TreeMap<Integer, String>();
        ht.put(100, "Rajendra");
        ht.put(102, "Praveen");
        ht.put(101, "Bipin");
        ht.put(103, "Pankaj");
        for (Map.Entry<Integer, String> entry : ht.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
100 Rajendra
101 Bipin
102 Praveen
103 Pankaj
************************************************************************************
package WebHandling;
import java.util.LinkedHashMap;
import java.util.Map;
public class tryProgs2 {
    public static void main(String[] args) {
        LinkedHashMap<Integer, String> ht = new LinkedHashMap<Integer, String>();
        ht.put(100, "Rajendra");
        ht.put(102, "Praveen");
        ht.put(101, "Bipin");
        ht.put(103, "Pankaj");
        for (Map.Entry<Integer, String> entry : ht.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
100 Rajendra
102 Praveen
101 Bipin
103 Pankaj
************************************************************************************
package WebHandling;
import java.util.HashMap;
import java.util.Map;
public class tryProgs2 {
    public static void main(String[] args) {
        HashMap<Integer, String> ht = new HashMap<Integer, String>();
        ht.put(100, "Rajendra");
        ht.put(102, "Praveen");
        ht.put(101, "Bipin");
        ht.put(103, "Pankaj");
        for (Map.Entry<Integer, String> entry : ht.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
100 Rajendra
101 Bipin
102 Praveen
103 Pankaj
************************************************************************************
package WebHandling;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class tryProgs2 {
    public static void main(String[] args) {
    	int[] array = {1, 1, 2, 2, 3, 4, 5, 5, 6, 6};
		List<Integer> result = findNonRepeatedElements(array);
		System.out.print("Non-repeated elements : "+result);
	}
	public static List<Integer> findNonRepeatedElements(int[] array) {
		HashMap<Integer, Integer> countMap = new HashMap<Integer, Integer>();
		for (int num : array) {
			countMap.put(num, countMap.getOrDefault(num, 0) + 1);
		}
		List<Integer> nonRepeatedElements = new ArrayList<>();
		for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
			if (entry.getValue() == 1) {
				nonRepeatedElements.add(entry.getKey());
			}
		}
		return nonRepeatedElements;
    }
}
OUTPUT - Non-repeated elements : [3, 4]
************************************************************************************
package com.tryPrograms;

import java.util.Objects;

public class Student {
	private int id;
	private String name;
	// constructor
	public Student(int id, String name) {
		this.id = id;
		this.name = name;
	}
	@Override
	public int hashCode() {
		return Objects.hash(id, name);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null || getClass() != obj.getClass())
			return false;
		Student student = (Student) obj;
		return id == student.id && Objects.equals(name, student.name);
	}
		public static void main(String[] args) {
			Student student1 = new Student(1, "Alice");
			Student student2 = new Student(2, "Bob");
			Student student3 = new Student(1, "Alice");
			System.out.println("student1.equals(student2) : " + student1.equals(student2));
			System.out.println("student1.equals(student3) : " + student1.equals(student3));
			// Testing hashCode method 
			System.out.println("Hashcode of student1: " + student1.hashCode()); 
			System.out.println("Hashcode of student2: " + student2.hashCode()); 
			System.out.println("Hashcode of student3: " + student3.hashCode());
	}
}
student1.equals(student2) : false
student1.equals(student3) : true
Hashcode of student1: 63351360
Hashcode of student2: 67988
Hashcode of student3: 63351360
************************************************************************************
package com.tryPrograms;
import java.util.Objects;
public class Student {
	public static void main(String[] args) {
		int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9}; 
		int[] count = countOddAndEven(array);
		System.out.println("Even numbers count: " + count[1]);
		System.out.println("Odd numbers count: " + count[0]);
	}
	public static int[] countOddAndEven(int[] array) {
		int[] count = new int[2];
		for (int num : array) {
			if (num % 2 == 0)
				count[1]++;
			else {
				count[0]++;
			}
		}
		return count;
	}
}
Even numbers count: 4
Odd numbers count: 5
************************************************************************************
package com.tryPrograms;
import java.util.Objects;
public class Student {
	public static void main(String[] args) {
		int[] array = {5, 2, 9, 1, 6, 3}; 
		int max = findMaximum(array); 
		int min = findMinimum(array);
		System.out.println("Minimum value in the array: " + min); 
		System.out.println("Maximum value in the array: " + max);
	}
	public static int findMaximum(int[] array) {
		if (array.length == 0) {
			throw new IllegalArgumentException("Array must not be empty!");
		}
		int max = array[0];
		for (int i=0; i<array.length; i++) {
			if (array[i] > max) 
				max = array[i];
		}
		return max;
	}
	public static int findMinimum(int[] array) {
		if (array.length == 0) {
			throw new IllegalArgumentException("Array must not be empty");
			}
			int min = array[0];
			for (int i=0; i<array.length; i++) {
				if (array[i] < min)
					min = array[i];
		}
		return min;
	}
}
Minimum value in the array: 1
Maximum value in the array: 9
************************************************************************************
package com.tryPrograms;
public class Student {
	public static void main(String[] args) {
		int[] array = {1, 2, 4, 5, 6}; // Missing number is 3 
		int missingNumber = findMissingNumber(array); 
		System.out.println("The missing number is: " + missingNumber); 
	}
	public static int findMissingNumber(int[] array) {
		int n = array.length+1;
		int totalSum = n * (n + 1)/2;
		int arraySum = 0;
		for (int num : array)
			arraySum += num;
		return totalSum - arraySum;
	} 
}
The missing number is: 3
************************************************************************************
package com.tryPrograms;
import java.util.ArrayList;
import java.util.HashSet;
public class Student {
	public static void main(String[] args) {
		ArrayList<Integer> alist = new ArrayList<>();
		alist.add(5);
		alist.add(2);
		alist.add(9);
		alist.add(1);
		alist.add(6);
		alist.add(2);
		alist.add(5);
		ArrayList<Integer> uniqueList = removeDuplicates(alist);
		System.out.print("ArrayList with duplicates removed:");
		for (int num : uniqueList)
			System.out.print(num + " ");
	}
	public static ArrayList<Integer> removeDuplicates(ArrayList<Integer> list) {
		HashSet<Integer> set = new HashSet<>(list);
	return new ArrayList<>(set);
	} 
}
ArrayList with duplicates removed:1 2 5 6 9 
************************************************************************************
package com.tryPrograms;
import java.util.ArrayList;
import java.util.HashSet;
public class Student {
	public static void main(String[] args) {
		int[] array = {5, 2, 9, 1, 6, 2, 5}; 
		int[] uniqueList = removeDuplicates(array);
		System.out.print("ArrayList with duplicates removed:");
		for (int num : uniqueList)
			System.out.print(num + " ");
	}
	public static int[] removeDuplicates(int[] list) {
		HashSet<Integer> set = new HashSet<>(); 
		for (int num : list) { 
			set.add(num); 
			} 
			int[] result = new int[set.size()]; 
			int i = 0; 
			for (int num : set) { 
			result[i++] = num; 
			} 
			return result; 
	} 
}
ArrayList with duplicates removed:1 2 5 6 9 
************************************************************************************
package com.tryPrograms;
public class Student {
	public static void main(String[] args) {
		int[] array = {5, 2, 9, 1, 6}; 
		selectionSort(array); 
		System.out.println("Sorted array:");
		for (int num : array)
			System.out.print(num + " ");
	}
	public static void selectionSort(int[] array) {
		int n = array.length;
		for (int i=0; i<n-1; i++) {
			int midIndex = i;
			for (int j=i+1; j<n; j++) {
				if (array[j] < array[midIndex])
					midIndex = j;
			}
			int temp = array[i];
			array[i] = array[midIndex];
			array[midIndex] = temp;
		}		
	} 
}
Sorted array:
1 2 5 6 9 
************************************************************************************
package com.tryPrograms;
import java.util.ArrayList;
public class Student {
	public static void main(String[] args) {
		ArrayList<String> arrayList = new ArrayList<>();
		arrayList.add("Apple");
		arrayList.add("Banana"); 
		arrayList.add("Cherry"); 
		arrayList.add("Date"); 
		arrayList.add("Elderberry"); 
		if (!arrayList.isEmpty()) {
			String firstElement = arrayList.get(0);
			String lastElement = arrayList.get(arrayList.size()-1);
			System.out.println("First element: " + firstElement); 
			System.out.println("Last element: " + lastElement); 
		} else
			System.out.println("The ArrayList is empty."); 
	} 
}
First element: Apple
Last element: Elderberry
************************************************************************************
package com.tryPrograms;
import java.util.HashSet;
public class Student {
	public static void main(String[] args) {
		int[] array1 = {1, 2, 3, 4, 5}; 
		int[] array2 = {4, 5, 6, 7, 8};
		HashSet<Integer> commonEle = findCommonElements(array1, array2);
		System.out.print("Common elements : " + commonEle);
	} 
	public static HashSet<Integer> findCommonElements(int[] array1, int[] array2) {
		HashSet<Integer> set1 = new HashSet<>();
		HashSet<Integer> commonSet = new HashSet<>();
		for (int num : array1)
			set1.add(num);
		for (int num : array2) {
			if (set1.contains(num))
				commonSet.add(num);
		}
		return commonSet;
	}
}
Common elements : [4, 5]
************************************************************************************
package com.tryPrograms;
import java.util.HashSet;
public class Student {
	public static void main(String[] args) {
		String s1 = "abcabcbb"; // Expected: "abc", length 3 
		String s2 = "bbbbb"; // Expected: "b", length 1 
		String s3 = "pwwkew"; // Expected: "wke", length 3 
		String s4 = ""; // Expected: "", length 0 
		System.out.println("Longest substring without repeating characters in s1: " + lengthOfLongestSubstring(s1)); // Output: 3 
		System.out.println("Longest substring without repeating characters in s2: " + lengthOfLongestSubstring(s2)); // Output: 1 
		System.out.println("Longest substring without repeating characters in s3: " + lengthOfLongestSubstring(s3)); // Output: 3 
		System.out.println("Longest substring without repeating characters in s4: " + lengthOfLongestSubstring(s4)); // Output: 0 
	} 
	public static int lengthOfLongestSubstring(String s) {
		HashSet<Character> set = new HashSet<>();
		int maxLength = 0;
		int start = 0;
		int end = 0;
		while (end < s.length()) {
			char currentChar = s.charAt(end);
			if (!set.contains(currentChar)) {
				set.add(currentChar);
				maxLength = Math.max(maxLength, end-start+1);
				end ++;
			} else {
				set.remove(s.charAt(start));
				start ++;
			}
		}
		return maxLength;
	}
}
Longest substring without repeating characters in s1: 3
Longest substring without repeating characters in s2: 1
Longest substring without repeating characters in s3: 3
Longest substring without repeating characters in s4: 0
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter String : ");
		String input = sc.nextLine();
		System.out.println("Original String is : " + input);
		separateAplhaAndNumeric(input);
	}
	public static void separateAplhaAndNumeric(String input) {
		StringBuilder alphaPart = new StringBuilder();
		StringBuilder numericPart = new StringBuilder();
		for (char ch : input.toCharArray()) {
			if (Character.isLetter(ch))
				alphaPart.append(ch);
			else if (Character.isDigit(ch))
				numericPart.append(ch);
		}
		System.out.println("Output in Alpha : " + alphaPart.toString());
		System.out.println("Output in Numeric : "+ numericPart.toString());
 	}
}
Enter String :  Subbu123raj 
Original String is :  Subbu123raj 
Output in Alpha : Subburaj
Output in Numeric : 123
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter a string : ");
		String input = sc.nextLine();
		System.out.println("Original String is : " +input);
		separateCharacters(input);
 	}
	public static void separateCharacters(String input) {
		StringBuilder lowerCase = new StringBuilder();
		StringBuilder upperCase = new StringBuilder();
		for (char ch : input.toCharArray()) {
			if (Character.isLowerCase(ch))
				lowerCase.append(ch);
			else
				upperCase.append(ch);
		}
		System.out.println("Output in lowercase: "+lowerCase); 
		System.out.println("Output in uppercase "+upperCase);
	} 
}
Enter a string : aBACbcEDed
Original String is : aBACbcEDed
Output in lowercase: abced
Output in uppercase BACED
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter string :  ");
		String input = sc.nextLine();
		String output = getCharacterCount(input);
		System.out.println("Output : " + output);
	} 
	public static String getCharacterCount(String str) {
		StringBuilder result = new StringBuilder();
		int count = 1;
		for (int i=0; i<str.length(); i++) {
			if (i+1<str.length() && str.charAt(i) == str.charAt(i+1))
				count ++;
			else {
				result.append(str.charAt(i)).append(count);
				count = 1;
			}
		}
		return result.toString();
	}
}
Enter string :  aabbcccdd
Output : a2b2c3d2
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter first string: "); 
		String str1 = sc.nextLine();
		System.out.print("Enter second string: "); 
		String str2 = sc.nextLine();
		System.out.println("Before swapping the str1 = : "+str1+" and str2 = "+str2); 
		str1 = str1 + str2;
		str2 = str1.substring(0, str1.length() - str2.length());
		str1 = str1.substring(str2.length());
		System.out.println("After swapping : str1 = " +str1+", str2 = "+str2);
	}
}
Enter first string: Hello
Enter second string: World
Before swapping the str1 = : Hello and str2 = World
After swapping : str1 = World, str2 = Hello
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter string : ");
		String input = sc.nextLine();
		String doubleString = doubleCharacters(input);
		System.out.print("Double characters : " + doubleString);
	}
	public static String doubleCharacters(String str) {
		StringBuilder doubled = new StringBuilder();
		for (int i=0; i<str.length(); i++) {
			char ch = str.charAt(i);
			doubled.append(ch).append(ch);
		}
		return doubled.toString();
	}
}
Enter string : hello
Double characters : hheelllloo
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter String : ");
		String input = sc.nextLine();
		String stringWithoutSpaces = removeSpaces(input);
		System.out.print("String without spaces : " +stringWithoutSpaces);
	}
	public static String removeSpaces(String str) {
		StringBuilder result = new StringBuilder();
		for (int i=0; i<str.length(); i++) {
			if (str.charAt(i) != ' ')
				result.append(str.charAt(i));
		}
		return result.toString();
	}
}
Enter String :  Welcome    to  Java   World 
String without spaces : WelcometoJavaWorld
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter String : ");
		String input = sc.nextLine();
		System.out.print("Even indexed characters in \"" + input + "\" : ");
		printEvenIndexedCharacters(input);
	}
	public static void printEvenIndexedCharacters(String str) {
		for (int i=0; i<str.length(); i++) {
			if (i % 2 == 0)
				System.out.print(str.charAt(i));
		}
	}
}
Enter String : Automation
Even indexed characters in "Automation" : Atmto
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); 
		System.out.print("Enter a string: "); 
		String input = scanner.nextLine(); 
		System.out.println("Unique characters in \"" + input + "\":"); 
		printUniqueCharacters(input); 
	}
	public static void printUniqueCharacters(String str) {
		boolean[] unique = new boolean[128]; 
		for (int i = 0; i < str.length(); i++) { 
			char ch = str.charAt(i); 
			if (!unique[ch]) { 
			unique[ch] = true; 
			System.out.print(ch + " "); 
			} 
		}
	}
}
Enter a string: Java Automation
Unique characters in "Java Automation":
J a v   A u t o m i n 
************************************************************************************
package com.tryPrograms;
public class Student {
	public static void main(String[] args) {
		String str = "Hello World";
		VowelConsonantCount(str);
	}
	static void VowelConsonantCount(String str) {
		int vowels=0, consonants=0;
		str = str.toLowerCase();
		for (char c : str.toCharArray()) {
			if (c >= 'a' && c <= 'z') {
				if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
					vowels++;
				else
					consonants++;
			}
		}
		System.out.println("Vowels : " + vowels);
		System.out.println("consonants : " + consonants);
		
	}
}
Vowels : 3
consonants : 7
************************************************************************************
package com.tryPrograms;
public class Student {
	public static void main(String[] args) {
		String str1 = "listen"; 
		String str2 = "silent"; 
		System.out.println("Strings are Anagrams : " + areAnagrams(str1,str2)); 
	}
	static boolean areAnagrams(String str1, String str2) {
		if (str1.length() != str2.length())
			return false;
		int[] charCount = new int[256];
		for (int i=0; i<str1.length(); i++) {
			charCount[str1.charAt(i)]++;
			charCount[str2.charAt(i)]--;
		}
		for (int count : charCount) {
			if (count != 0)
				return false;
		}
		return true;
	}
}
Strings are Anagrams : true
************************************************************************************
package com.tryPrograms;
public class Student {
	public static void main(String[] args) {
		String str = "madam"; 
		System.out.println("String is palindrome : " +isPalindrome(str));  
	}
	static boolean isPalindrome(String str) {
		int start = 0;
		int end = str.length()-1;
		while (start < end) {
			if (str.charAt(start) != str.charAt(end)) {
				return false;
			}
			start++;
			end--;
		}
		return true;
	}
}
String is palindrome : true
************************************************************************************
package com.tryPrograms;
public class Student {
	public static void main(String[] args) {
		String str = "abc"; 
		permute(str, "");   
	}
	static void permute(String str, String prefix) {
		if (str.length() == 0) { 
			System.out.println(prefix); 
			} else { 
			for (int i = 0; i < str.length(); i++) { 
			String rem = str.substring(0,i) + str.substring(i+1); 
			//System.out.println(rem); 
			permute(rem,prefix + str.charAt(i)); 
			} 
		} 
	}
}
abc
acb
bac
bca
cab
cba
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) {
		System.out.print("Enter the String : ");
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		int count = 1;
		for (int i=0; i<s.length()-1; i++) {
			if ((s.charAt(i) == ' ') && (s.charAt(i + 1) != ' ')) {
				count ++;
			}
		}
		System.out.println("Number of words in string : " +count);
  }
}
Enter the String : Welcome to Java World 
Number of words in string : 4
************************************************************************************
package com.tryPrograms;
import java.util.HashMap;
public class Student {
	public static void main(String[] args) {
		CharacterCount("Test Automation Java Automation"); 
		}
	static void CharacterCount(String inputString) {
		HashMap<String, Integer> CharCountMap = new HashMap<>();
		for (String s : inputString.split(" ")) {
			if (CharCountMap.containsKey(s)) {
				CharCountMap.put(s, CharCountMap.get(s)+1);
			} else
				CharCountMap.put(s, 1);
		}
		System.out.println("Count of Characters in a given string : " + CharCountMap);
  }
}
Count of Characters in a given string : {Java=1, Automation=2, Test=1}
************************************************************************************
package com.tryPrograms;
import java.util.HashMap;
public class Student {
	public static void main(String[] args) { 
		duplicateCharacterCount("Learn Java Programming"); 
		} 
	static void duplicateCharacterCount(String inputString) {
	    inputString = inputString.toLowerCase();  // normalize case
	    HashMap<Character, Integer> charCountMap = new HashMap<>();
	    char[] strArray = inputString.toCharArray();

	    for (char c : strArray) {
	        if (c == ' ') continue; // ignore spaces
	        charCountMap.put(c, charCountMap.getOrDefault(c, 0) + 1);
	    }

	    System.out.println("Duplicate Characters in : " + inputString);
	    for (char ch : charCountMap.keySet()) {
	        if (charCountMap.get(ch) > 1) {
	            System.out.println(ch + " : " + charCountMap.get(ch));
	        }
	    }
	} 
}
Duplicate Characters in : learn java programming
a : 4
r : 3
g : 2
m : 2
n : 2
************************************************************************************
package com.tryPrograms;
public class Student {
	public static void main(String[] args) { 
		reverseEachWordOfString("Java is good programming langauges"); 
	} 
	static void reverseEachWordOfString(String inputString) {
	    String[] words = inputString.split(" ");
	    String reverseString = "";
	    for (int i=0; i<words.length; i++) {
	    	String word = words[i];
	    	String nstr = "";
	    	char ch;
	    	for (int j=0; j<word.length(); j++) {
	    		ch = word.charAt(j);
	    		nstr = ch + nstr;
	    	}
	    	reverseString = reverseString + nstr + " ";
	    }
	    System.out.println(inputString);
	    System.out.println(reverseString);
	} 
}
Java is good programming langauges
avaJ si doog gnimmargorp seguagnal 
************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Student {
	public static void main(String[] args) { 
		Scanner scanner = new Scanner(System.in); 
		System.out.print("Enter a string: "); 
		String input = scanner.nextLine(); 
		char ch; 
		String nstr = ""; 
		for (int i = 0; i < input.length(); i++) { 
		ch = input.charAt(i); 
		nstr = ch + nstr; 
		} 
		System.out.println("Reversed String is : " + nstr); 
	}
}
Enter a string: Java is programming language
Reversed String is : egaugnal gnimmargorp si avaJ
************************************************************************************
************************************************************************************
************************************************************************************
************************************************************************************
************************************************************************************
