import java.util.*;
class Test {
    public static void main(String[] args) {
        String orig, rev = ""; // Objects of String class 
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a string/number to check if it is a palindrome");  
        orig = in.nextLine();
        int length = orig.length();
        for (int i=length-1; i>=0; i--)
        {
            rev = rev + orig.charAt(i);
            System.out.println(rev);
        }
        if (orig.equals(rev))
            System.out.println("String is Palingrome");
        else
            System.out.println("String is not Palingrome");
    }
}
PS C:\Users\VWankhedkar\PycharmProjects\Robot>  c:; cd 'c:\Users\VWankhedkar\PycharmProjects\Robot'; & 'C:\Program Files\Java\jre1.8.0_421\bin\java.exe' '-cp' 'C:\Users\VWankhedkar\AppData\Roaming\Code\User\workspaceStorage\538f90e2a7e8ceeb2cfc0d33f075b13d\redhat.java\jdt_ws\Robot_9e862827\bin' 'Test' 
Enter a string/number to check if it is a palindrome
aba
a
ab
aba
String is Palingrome
PS C:\Users\VWankhedkar\PycharmProjects\Robot>  c:; cd 'c:\Users\VWankhedkar\PycharmProjects\Robot'; & 'C:\Program Files\Java\jre1.8.0_421\bin\java.exe' '-cp' 'C:\Users\VWankhedkar\AppData\Roaming\Code\User\workspaceStorage\538f90e2a7e8ceeb2cfc0d33f075b13d\redhat.java\jdt_ws\Robot_9e862827\bin' 'Test'
Enter a string/number to check if it is a palindrome
abcda
a
ad
adc
adcb
adcba
String is not Palingrome
************************************************************************
1. Two Sum
package WebHandling;
import java.util.Map;
import java.util.HashMap;
public class tryProgs2 {

    public int[] twoSum(int[] nums, int target) {
    	Map<Integer, Integer> map = new HashMap<>(); // Now Map is recognized
    	for (int i = 0; i < nums.length; i++) {
    		int complement = target - nums[i];
    		if (map.containsKey(complement)) {
    			return new int[] {map.get(complement), i};
    		}
    		map.put(nums[i], i);
    	}
        return new int[]{};
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] nums = {2, 7, 11, 15};
        int target = 18;
        int[] result = obj.twoSum(nums, target);
        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}
OUTPUT ---- Indices: 1, 2
********************************************************
2. Reverse a String
package WebHandling;
public class tryProgs2 {

    public String reverseString(String str) {
    	return new StringBuilder(str).reverse().toString();
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        String rev = obj.reverseString("Java Programming");
        System.out.println("Reversed string is: "+rev);
    }
}
OUTPUT ---- Reversed string is: gnimmargorP avaJ
********************************************************
 3. Palindrome Check
package WebHandling;
public class tryProgs2 {
    public boolean isPalindrome(String str) {
    	int left = 0, right = str.length()-1;
    	while (left < right) {
    		if (str.charAt(left++) != str.charAt(right--))
    			return false;
    	}
    	return true;
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        Boolean palindrome = obj.isPalindrome("malayalam");
        System.out.println("Is string palindrome : "+palindrome);
    }
}
OUTPUT ---- Is string palindrome : true
********************************************************
4. Merge Two Sorted Lists
package WebHandling;
// Define ListNode class
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }

    // Helper method to print list
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        ListNode curr = this;
        while (curr != null) {
            sb.append(curr.val);
            if (curr.next != null) sb.append(" -> ");
            curr = curr.next;
        }
        return sb.toString();
    }
}
public class tryProgs2 {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2)  {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
    // Helper method to convert array to ListNode
    public static ListNode arrayToList(int[] arr) {
        if (arr.length == 0) return null;
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();

        // Create two sorted linked lists
        ListNode l1 = arrayToList(new int[]{1, 3, 5});
        ListNode l2 = arrayToList(new int[]{2, 4, 6});

        // Merge and print result
        ListNode mergedList = obj.mergeTwoLists(l1, l2);
        System.out.println("Merged List is: " + mergedList);
    }
}
OUTPUT ---- Merged List is: 1 -> 2 -> 3 -> 4 -> 5 -> 6
********************************************************
5. Longest Substring Without Repeating Characters
package WebHandling;
import java.util.HashSet;
import java.util.Set;
public class tryProgs2 {
    public int lenOfLongestString(String str) {
    	Set<Character> set = new HashSet<>();
    	int left=0, maxlen=0;
    	for (int right=0; right<str.length(); right++) {
    		while (set.contains(str.charAt(right))) {
    			set.remove(str.charAt(left++));
    		}
    		set.add(str.charAt(right));
    		maxlen = Math.max(maxlen, right-left+1);
    	}
    	return maxlen;
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int lenOfLongString = obj.lenOfLongestString("pythonprogramming");
        System.out.println("Length of longest string is : "+lenOfLongString);
    }
}
OUTPUT ---- Length of longest string is : 7
********************************************************
6. Valid Parentheses
package WebHandling;
import java.util.Stack;
public class tryProgs2 {

    public boolean isValidParanthesis(String s) {
    	Stack<Character> stack = new Stack<>();
    	for (char c : s.toCharArray()) {
    		if (c == '(' || c == '{' || c == '[') {
    			stack.push(c);
    		} else if (!stack.isEmpty() && 
    				((c == ')' && stack.peek() == '(') ||
    				 (c == '}' && stack.peek() == '{') ||
    				 (c == ']' && stack.peek() == '['))) {
    			stack.pop();
    		}  else {
    			return false;
    		}
    	}
    	return stack.isEmpty();
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        boolean isParanthesValid = obj.isValidParanthesis("[(({}))]");
        System.out.println("Is Paranthes Valid : "+isParanthesValid);
    }
}
OUTPUT ---- Is Paranthes Valid : true
********************************************************
7. Search in Rotated Sorted Array
package WebHandling;
import java.util.Stack;
public class tryProgs2 {

    public int search(int[] nums, int target) {
    	int left=0, right=nums.length-1;
    	while (left <= right) {
    		int mid = (left + right) / 2;
    		if (nums[mid] == target)  return mid;
    		if (nums[left] <= nums[mid])  {
    			if (nums[left] <= target && target<nums[mid]) right = mid - 1;
    			else left = mid + 1;
    		} else {
    			if (nums[mid] < target && target <= nums[right]) left = mid + 1;
    			else right = mid - 1;
    		}
    	}
    	return -1;
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] nums = {2,3,4,5,6,7,8,8,9};
        int target = 8;
        int eleLocation = obj.search(nums, target);
        System.out.println("Element location is : "+eleLocation);
    }
}
OUTPUT ---- Element location is : 6
********************************************************
package com.tryPrograms;
public class LambdaProgs {
    public static void main(String[] args) {
        int num=17;
        boolean isPrime = true;
        if (num <= 1) {
        	isPrime = false;
        } else {
        	for (int i=2; i<Math.sqrt(num); i++) {
        		if (num % 2 == 0) {
        			isPrime = false;
        			break;
        		}
        	}
        }
        System.out.print(num + " is prime number - " + isPrime);
    }
}        ----->    17 is prime number - true
*************************************************************************
package com.tryPrograms;
public class SumOfDigits {
	public static void main(String[] args) {
		int number = 12345;
		int sum = 0;
		while (number > 0) {
			sum += number % 10;
			number /= 10;
		}
		System.out.println("Sum of digits: " + sum);
	}
}
Sum of digits: 15
*************************************************************************
package com.tryPrograms;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
public class RemoveDuplicates {
	public static void main(String[] args) {
		Integer[] numbers = {1,2,3,2,5,1,6,3,7};
		Set<Integer> uniqueSet = new HashSet<>(Arrays.asList(numbers));
		Integer[] uniqueNumbers = uniqueSet.toArray(new Integer[0]);
		System.out.println("Original: " + Arrays.toString(numbers));
		System.out.println("Without duplicates: " +Arrays.toString(uniqueNumbers));
	}
}
Original: [1, 2, 3, 2, 5, 1, 6, 3, 7]
Without duplicates: [1, 2, 3, 5, 6, 7]
*************************************************************************
package com.tryPrograms;
public class RemoveDuplicates {
	public static void main(String[] args) {
		String sentence = "Java Coding Interview";
		String[] words = sentence.split(" ");
		StringBuilder result = new StringBuilder();
		for (String word:words) {
			StringBuilder revervedWord = new StringBuilder(word).reverse();
			result.append(revervedWord).append(" ");
		}
		System.out.println("Original: " +sentence);
		System.out.println("Reserved words : " + result.toString().trim());
	}
}
Original: Java Coding Interview
Reserved words : avaJ gnidoC weivretnI
*************************************************************************
package com.tryPrograms;
public class RemoveDuplicates {
	public static void main(String[] args) {
		String input = "Java Programming";
		StringBuilder result = new StringBuilder();
		for (char c:input.toCharArray()) {
			if (Character.isUpperCase(c)) {
				result.append(Character.toLowerCase(c));
			} else if (Character.isLowerCase(c)) {
				result.append(Character.toUpperCase(c));
			} else result.append(c);
		}
		System.out.println("Original : "+input);
		System.out.println("Case Converted : "+result.toString());
	}
}
Original : Java Programming
Case Converted : jAVA pROGRAMMING
*************************************************************************
package com.tryPrograms;
public class RemoveDuplicates {
	public static int findSecondLargest(int[] arr) {
		int largest = Integer.MIN_VALUE;
		int secondLargest = Integer.MIN_VALUE;
		for (int num:arr) {
			if (num > largest) {
				secondLargest = largest;
				largest = num;
			} else if (num > secondLargest && num != largest) {
				secondLargest = num;
			}
		}
		return secondLargest;
	}
	public static void main(String[] args) {
		int[] numbers = {12, 35, 35, 1, 10, 34, 1};
		System.out.println("SecondLargestNumber is : " + findSecondLargest(numbers));
	}
}
SecondLargestNumber is : 34
*************************************************************************
package com.tryPrograms;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
public class RemoveDuplicates {
	public static List<Integer> findDuplicates(int[] arr) {
		Set<Integer> seen = new HashSet<>();
		List<Integer> duplicates = new ArrayList<>();
		for (int num : arr) {
			if (!seen.add(num)) {
				duplicates.add(num);
			}
		}
		return duplicates;
	}
	public static void main(String[] args) {
		 int[] numbers = {1, 2, 3, 4, 2, 7, 8, 8, 3};
		System.out.println("Duplicate elements : " + findDuplicates(numbers));
	}
}
Duplicate elements : [2, 8, 3]
*************************************************************************
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
}
"Listen" and "Silent" are anagrams:true
*************************************************************************
package com.tryPrograms;
public class RemoveDuplicates {
	public static void bubbleSort(int[] arr) {
		int n = arr.length;
		boolean swapped;
		for (int i=0; i<n-1; i++) {
			swapped = false;
			for (int j=0; j<n-i-1; j++) {
				if (arr[j] > arr[j+1]) {
					int temp = arr[j];
					arr[j] = arr[j+1];
					arr[j+1] = temp;
					swapped = true;
				}
			}
			if (!swapped)   break;
		}
	}
	public static void main(String[] args) {
		int[] arr = {64, 34, 25, 12, 22, 11, 90};
		System.out.println("Original array : " + java.util.Arrays.toString(arr));
		bubbleSort(arr);
		System.out.println("Sorted array : " + java.util.Arrays.toString(arr));
	}
}
Original array : [64, 34, 25, 12, 22, 11, 90]
Sorted array : [11, 12, 22, 25, 34, 64, 90]
*************************************************************************
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
*************************************************************************
package com.tryPrograms;
import java.util.HashMap;
import java.util.Map;
public class RemoveDuplicates {
	public static char FirstNonRepeatedChar(String str) {
		Map<Character, Integer> charCounts = new HashMap<>();
		for (char c : str.toCharArray()) {
			charCounts.put(c, charCounts.getOrDefault(c, 0)+1);
		}
		for (char c:str.toCharArray()) {
			if (charCounts.get(c) == 1) {
				return c;
			}
		}
		return '\0';
	}
	public static void main(String[] args) {
		String str = "programming";
		char result = FirstNonRepeatedChar(str);
		if (result != '\0') {
			System.out.println("First non-repeated character : " + result);
		} else {
			System.out.println("No non repeated character found.");
		} 		
	}
}	===>		First non-repeated character : p
*************************************************************************
POJO
package com.tryPrograms;
public class Main {
	private int id;
	private String name;
	private String department;
	// Constructor
	public Main (int id, String name, String department) {
		this.id = id;
		this.name = name;
		this.department = department;
	}
	// Getter and setters
	public int getId() { return id; }
	public void setId(int id) { this.id = id; }
	public String getName() {return name;}
	public void setName(String name) {this.name = name; }
	public String getDepartment() {return department;}
	public void setDepartment(String department) {this.department = department; }
	public static void main(String[] args) {
	System.out.print("Hello");
  } 
}	
************************************************************************************************
package com.tryPrograms;

import java.util.LinkedHashMap;
import java.util.Map;

public class Main {
	public static void main(String[] args) {
		int a[] = {1,2,1,3,3,2,1};  
		Map<Integer,Integer> map = new LinkedHashMap<Integer,Integer>(); 
		for(Integer i : a){ 
		if(map.containsKey(i)){ 
		map.put(i,map.get(i)+1); 
		}else{ 
		map.put(i,1); 
		} 
		} 
		for(Integer i : map.keySet()){ 
		System.out.println(i+":"+map.get(i)); 
		} 
	}
}	
1:3
2:2
3:2
************************************************************************************************
package com.tryPrograms;
import java.util.LinkedHashMap;
import java.util.Map;
public class Main {
	public static void main(String[] args) {
		String  s = "Vaishali";  
		Map<Character,Integer> map = new LinkedHashMap<Character,Integer>();
		for (Character ch : s.toCharArray()) {
			if (map.containsKey(ch)) {
				map.put(ch,map.get(ch)+1);
			} else {
				map.put(ch, 1);
			}
		}
		for (Character ch : map.keySet()) {
			if (map.get(ch) == 1) {
				System.out.print(ch+" : "+map.get(ch));
				break;
			}
		}
	}
}	===> V : 1
************************************************************************************************
package com.tryPrograms;
import java.util.LinkedHashMap;
import java.util.Map;
public class Main {
	public static void main(String[] args) {
		String s = "Vaishali";
		Map<Character,Integer> map = new LinkedHashMap<Character, Integer>();
		for (Character ch : s.toCharArray()) {
			if (map.containsKey(ch)) {
				map.put(ch, map.get(ch)+1);
			} else 
				map.put(ch, 1);
		}
		for (Character ch : map.keySet()) {
			System.out.println(ch + " : " + map.get(ch));
		}
	}
}	
V : 1
a : 2
i : 2
s : 1
h : 1
l : 1
************************************************************************************************
package com.tryPrograms;
import java.util.LinkedHashMap;
import java.util.Map;
public class Main {
	public static void main(String[] args) {
		String a = "Kundan Kumar Pandey Kundan Kumar"; 
		String s[] = a.split(" ");
		Map<String,Integer> map = new LinkedHashMap<String,Integer>();
		for (String ch : s) {
			if (map.containsKey(ch)) {
				map.put(ch, map.get(ch)+1);
			} else 
				map.put(ch, 1);
		}
	for (String ch : map.keySet())
		System.out.println(ch + " : " + map.get(ch));
	}
}	
Kundan : 2
Kumar : 2
Pandey : 1
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

************************************************************************************************
