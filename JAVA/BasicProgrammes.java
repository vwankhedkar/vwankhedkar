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

*************************************************************************
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
