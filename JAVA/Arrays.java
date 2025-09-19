import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3};
        int[] arr2 = {4, 5, 6};
        combinedTwoArrays(arr1, arr2);
    }
    public static void combinedTwoArrays(int[] arr1, int[] arr2) {
        int length = arr1.length+arr2.length;
        int[] newArr = new int[length];
        for (int i=0; i<arr1.length; i++) {
            newArr[i] = arr1[i];
        }
        for (int i=0; i<arr1.length; i++) {
            newArr[arr1.length+i] = arr2[i];
        }
        System.out.println("Combined Arrays are : "+Arrays.toString(newArr));
    }
}	====>	Combined Arrays are : [1, 2, 3, 4, 5, 6]
*****************************************************************************************

*****************************************************************************************
*****************************************************************************************
*****************************************************************************************
// corresponding class names for array types
class Test {
    public static void main(String[] args)
    {
        int[] x = new int[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT -    [I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [[I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [B

class Test {
    public static void main(String[] args)
    {
        boolean[] x = new boolean[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [Z

// corresponding class names for array types
class Test {
    public static void main(String[] args)
    {
        int[] x = new int[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT -    [I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [[I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [B

// corresponding class names for array types
class Test {
    public static void main(String[] args)
    {
        int[] x = new int[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT -    [I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [[I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [B

class Test {
    public static void main(String[] args)
    {
        short[] x = new short[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [S

class Test {
    public static void main(String[] args)
    {
        double[] x = new double[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [D

class Test {
    public static void main(String[] args)
    {
        int[] x = new int[-3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - ERROR!
Exception in thread "main" java.lang.NegativeArraySizeException: -3
	at Test.main(Test.java:7)

class Test {
    public static void main(String[] args)
    {
        int[] x = new int[2147483648];
    }
}
OUTPUT - /tmp/532ypyp8YG/Test.java:7: error: integer number too large
        int[] x = new int[2147483648];

class Test {
    public static void main(String[] args)
    {
        int[] x = new int[2147483647];
       // System.out.println(x.getClass().getName());
    }
}
OUTPUT - Exception in thread "main" ERROR!
java.lang.OutOfMemoryError: Requested array size exceeds VM limit
	at Test.main(Test.java:7)

class Test {
    public static void main(String[] args)
    {
        int[][] a = new int[2][];
        System.out.println(a);
        System.out.println(a[0]);
        System.out.println(a[0][0]);
    }
}
OUTPUT - [[I@379619aa
null
ERROR!
Exception in thread "main" java.lang.NullPointerException: Cannot load from int array because "<local1>[0]" is null
	at Test.main(Test.java:10)

class Test {
    public static void main(String[] args)
    {
        int[] a = {10, 20, 30, 40, 50};
        int[] b = {70, 80};
        a = b;
        System.out.println(a);
        b = a;
        System.out.println(b);
    }
}
OUTPUT -[I@379619aa
[I@379619aa
****************************************************************************************************************
package com.tryPrograms;
public class SingleDimArray {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};
        System.out.println("Elements of array: ");
        for (int i=0; i<numbers.length; i++) {
        	System.out.println("Element at index : "+i+": "+numbers[i]);
        }
    }
}
Elements of array: 
Element at index : 0: 10
Element at index : 1: 20
Element at index : 2: 30
Element at index : 3: 40
Element at index : 4: 50
****************************************************************************************************************
package com.tryPrograms;
public class DoubleDiaArray {
    public static void main(String[] args) {
        int[][] arr = {
        		{1, 2},
        		{3, 4}
        };
        System.out.println(arr[0][0]);
        System.out.println(arr[1][1]);
    }
}
1
4
****************************************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class InputArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter size of array: ");
        int size = sc.nextInt();
        int[] arr = new int[size];
        System.out.println("Enter "+ size + " elements: ");
        for (int i=0; i<size; i++) {
        	arr[i] = sc.nextInt();
        }
        System.out.println("You entered: ");
        for (int i=0; i<size; i++) {
        	System.out.println(arr[i]);
        }
        sc.close();
    }
}
Enter size of array: 3
Enter 3 elements: 
87
45
32
You entered: 
87
45
32
****************************************************************************************************************
package com.tryPrograms;
public class sortDescending {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 7};
        for (int i=0; i<arr.length; i++) {
        	for (int j=i+1; j<arr.length; j++) {
        		if (arr[j] > arr[i]) {
        			int temp = arr[i];
        			arr[i] = arr[j];
        			arr[j] = temp;
        		}
        	}
        }
    	System.out.println("Array in Descending order is: ");
    	for (int num:arr) {
        	System.out.print(num+" ");
    	}
    }
}
Array in Descending order is: 
9 7 5 2 1 
****************************************************************************************************************
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int[] number = {5, 2, 7, 8, 4, 3, 9};
        int evenSum = 0;
        int oddSum = 0;
        for (int i=0; i<number.length; i++) {
        	if (number[i] % 2 == 0) {
        		evenSum += number[i];
        	} else {
        		oddSum += number[i];
        	}
        }
        System.out.println("Sum of Even numbers: "+evenSum);
        System.out.println("Sum of Odd numbers: "+oddSum);
    }
}
Sum of Even numbers: 14
Sum of Odd numbers: 24
****************************************************************************************************************
package com.tryPrograms;
public class sumDigits {
    public static void main(String[] args) {
        int[] number = {123, 45, 9, 100, 78};
        for (int i=0; i<number.length; i++) {
        	int num = number[i];
        	int sum = 0;
        	while (num > 0) {
        		sum += num % 10;
        		num = num / 10;
        }
        	System.out.println("Numbers: "+ number[i] + "-> Sum of digits: " + sum);
    } 
  }
}
Numbers: 123-> Sum of digits: 6
Numbers: 45-> Sum of digits: 9
Numbers: 9-> Sum of digits: 9
Numbers: 100-> Sum of digits: 1
Numbers: 78-> Sum of digits: 15
****************************************************************************************************************
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        boolean isUnique = true;
        for (int i=0; i<arr.length; i++) {
        	for (int j=i+1; j<arr.length; j++) {
        		if (arr[i] == arr[j]) {
        			isUnique = false;
        			break;
        		}
        }
        	if (!isUnique)  break;
      } 
    if (isUnique) {
    	System.out.println("Array contains only unique values");
    }  else  {
    	System.out.println("Array contains duplicate values");
    }
  }
}
Array contains only unique values
****************************************************************************************************************
package com.tryPrograms;
public class copyArray {
    public static void main(String[] args) {
        int[] orig = {10, 20, 30, 40, 50};
        int[] copy = new int[orig.length];
        for (int i=0; i<orig.length; i++) {
        		copy[i] = orig[i];
        }
    	System.out.print("Copied array: ");
    	for (int i=0; i<copy.length; i++) {
    		System.out.print(copy[i] + " ");
    	}
  }
}
Copied array: 10 20 30 40 50 
****************************************************************************************************************
package com.tryPrograms;
public class findIndex {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int target = 30;
        int index = -1;
        for (int i=0; i<arr.length; i++) {
        	if (arr[i] == target) {
        		index = i;
        		break;
        	}
        }
      if (index != -1) {
    	  System.out.print("Element: " +target+ " found at index: "+index);
      } else {
    	  System.out.print("Element: " +target+ " not found in the array");
    }
  }
}
Element: 30 found at index: 2
****************************************************************************************************************
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int[] orig = {10, 20, 30, 40, 50, 60, 70};
        int newSize = (orig.length + 1) / 2;
        int[] result = new int[newSize];
        int index = 0;
        for (int i=0; i<orig.length; i+=2) {
        	result[index] = orig[i];
        	index++;
        }
    System.out.print("Array after removing every second element:");
    for (int i=0; i<result.length; i++) {
    	System.out.print(result[i] + " ");
    }
  }
}
Array after removing every second element:10 30 50 70 
****************************************************************************************************************
package com.tryPrograms;
public class insertEleArray {
    public static void main(String[] args) {
        int[] orig = {10, 20, 30, 40, 50};
        int element = 25;
        int position = 2;
        if (position < 0 || position > orig.length) {
        	System.out.print("Invalid position! ");
        	return;
        }
        int[] newArray = new int[orig.length+1];
        for (int i=0; i<position; i++) {
        	newArray[i] = orig[i];
        }
        newArray[position] = element;
        for (int i=position; i<orig.length; i++) {
        	newArray[i+1] = orig[i];
        }
        System.out.println("Array after insertion: ");
        for (int i=0; i<newArray.length; i++) {
        	System.out.print(newArray[i] + " ");
        }
    }
}
Array after insertion: 
10 20 25 30 40 50 
****************************************************************************************************************
package com.tryPrograms;
public class minmaxArray {
    public static void main(String[] args) {
        int[] arr = {15, 22, 8, 19, 31, 4};
        int max = arr[0];
        int min = arr[0];
        for (int i=0; i<arr.length; i++) {
        	if (arr[i] > max) {
        		max = arr[i];
        	} 
        	if (arr[i] < min) {
        		min = arr[i];
        	}
        }
    	System.out.println("Maximum value: "+max);
    	System.out.println("Minimum value: "+min);
    }
}
Maximum value: 31
Minimum value: 4
****************************************************************************************************************
package com.tryPrograms;
public class secondHighestNum {
    public static void main(String[] args) {
        int[] arr = {15, 22, 8, 19, 31, 4};
        int highest = Integer.MIN_VALUE;
        int secondHighest = Integer.MIN_VALUE;
        for (int num : arr) {
        	if (num > highest) {
        		secondHighest = highest;
        		highest = num;
        	} else if (num > secondHighest && num < highest) {
        		secondHighest = num;
        	}
        }
        if (secondHighest == Integer.MIN_VALUE) {
        	System.out.println("No second highest value found(array may have all equal elements): ");        	
        } else {
    	System.out.println("Second highest value is: "+ secondHighest);
        }
    }
}
Second highest value is: 22
****************************************************************************************************************
package com.tryPrograms;
public class reverseArray {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50, 60};
        int start = 0;
        int end = arr.length-1;
        while (start < end) {
        	int temp = arr[start];
        	arr[start] = arr[end];
        	arr[end] = temp;
        	start ++;
        	end --;
        }
    	System.out.print("Reversed array : ");
    	for (int i : arr) {
        	System.out.print(i + " ");
    	}
    }
}
Reversed array : 60 50 40 30 20 10 
****************************************************************************************************************
package com.tryPrograms;
public class dupFound {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 20, 40, 10, 50, 30};
        System.out.println("Duplicate values in array: ");
        boolean foundDuplicate = false;
        for (int i=0; i<arr.length; i++) {
        	boolean isDuplicate = false;
        	for (int j=0; j<i; j++) {
        		if (arr[i] == arr[j]) {
        			isDuplicate = true;
        			break;
        		}
        	}
        	for (int k=i+1; k<arr.length; k++) {
        		if (!isDuplicate) {
        			if (arr[i] == arr[k]) {
        				System.out.println(arr[i]);
        				foundDuplicate =true;
        				break;
        			}
        		}
        	}
    	}
        if (!foundDuplicate) {
        	System.out.println("No duplicates found!");
        }
    }
}
Duplicate values in array: 
10
20
30
****************************************************************************************************************
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 20, 10, 40, 10, 50, 30};
        int n = arr.length;
        int[] temp = new int[n];
        int newIndex = 0;
        for (int i=0; i<n; i++) {
        	boolean isDuplicate = false;
        	for (int j=0; j<newIndex; j++) {
        		if (arr[i] == temp[j]) {
        			isDuplicate = true;
        			break;
        		}
        	}
        	if (!isDuplicate) {
        		temp[newIndex] = arr[i];
        		newIndex++;
        	}
        }
    	System.out.println("Array after removing duplicates: ");
    	for (int i=0; i<newIndex; i++) {
    		System.out.print(temp[i] + " ");
    	}
    }
}
Array after removing duplicates: 
10 20 30 40 50 
****************************************************************************************************************
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int[] arr = {1, 3, 2, 3, 4, 3, 5, 1, 2};
        int maxCount = 0;
        int mostFrequest = arr[0];
        for (int i=0; i<arr.length; i++) {
        	int count = 0;
        	for (int j=0; j<arr.length; j++) {
        		if (arr[i] == arr[j]) {
        			count++;
        		}
        	}
        	if (count > maxCount) {
        		maxCount = count;
        		mostFrequest = arr[i];
        	}
    	}
		System.out.println("Most frequest number is: " + mostFrequest);
		System.out.println("It appears " + maxCount + " times.");
    }
}
Most frequest number is: 3
It appears 3 times.
****************************************************************************************************************
package WebHandling;
import java.util.LinkedHashMap;
import java.util.Map;
public class tryProgs2 {
    public static Character firstNonRepeated(String str) {
    	Map<Character, Integer> countMap = new LinkedHashMap<>();
    	for (char c : str.toCharArray()) {
    		countMap.put(c, countMap.getOrDefault(c, 0) + 1);
    	}
    	System.out.println("Count map is: "+countMap);
    	for (Map.Entry<Character, Integer> entry : countMap.entrySet()) {
    		if (entry.getValue() == 1) return entry.getKey();
    	}
    	return null;    	
    }
    public static void main(String[] args) {
        System.out.println("The nonrepeated 1st Char is: "+firstNonRepeated("swiss"));
    }
}
Count map is: {s=3, w=1, i=1}
The nonrepeated 1st Char is: w
****************************************************************************************************************
package WebHandling;
import java.util.HashSet;
import java.util.Set;
public class tryProgs2 {
    public static int lengthOfLongestSubstring(String str) {
    	Set<Character> set = new HashSet<>();  
    	int left=0, max=0;
    	for (int right=0; right<str.length(); right++) {
    		while(set.contains(str.charAt(right))) {
    			set.remove(str.charAt(left++));
    		}
    		set.add(str.charAt(right));
    		max = Math.max(max, right-left+1);
    	}
    	return max;
    }
    public static void main(String[] args) {
        System.out.println("The lengthOfLongestSubstring is: "+lengthOfLongestSubstring("abcabcbb"));
    }
}
The lengthOfLongestSubstring is: 3
****************************************************************************************************************
package WebHandling;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class tryProgs2 {
    public static boolean isValidParentheses(String str) {
    	Stack<Character> stack = new Stack<>();
        for (char c : str.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char open = stack.pop();
    			if ((c == ')' && open != '(') || (c == '}' && open != '{') || (c == ']' && open != '['))  {
    				return false;
    			}
    		}
    	}
    	return stack.isEmpty();
    }
    public static void main(String[] args) {
        System.out.println("The isValidParentheses is: "+isValidParentheses("()[]{}[]"));
    }
}
The isValidParentheses is: true
****************************************************************************************************************
package WebHandling;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class tryProgs2 {
    public static String reverseWords(String str) {
        String[] words = str.trim().split("\\s+");  // use double backslash for regex
        List<String> wordList = Arrays.asList(words);
        Collections.reverse(wordList);
        return String.join(" ", wordList);
    }
    public static void main(String[] args) {
        System.out.println("The reverseWords string is: " + reverseWords("  the sky is blue  "));
    }
}
The reverseWords string is: blue is sky the
****************************************************************************************************************
package WebHandling;
public class tryProgs2 {
    public static boolean  isAnagram(String s, String t) {
        if (s.length() != t.length())  return false;
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        for (char c : t.toCharArray()) {
        	if (--count[c - 'a'] < 0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println("Is string isAnagram : " + isAnagram("listen", "silent"));
    }
}
Is string isAnagram : true
****************************************************************************************************************
package WebHandling;
public class tryProgs2 {
    public static int missingNumber(int[] nums) {
        int n = nums.length;
        int total = n * (n + 1) / 2;
        for (int num : nums) total -= num;
        return total;
    }
    public static void main(String[] args) {
        System.out.println("Missing number in list is: "+missingNumber(new int[]{3, 0, 1}));
    }
}
Missing number in list is: 2
****************************************************************************************************************
package WebHandling;
import java.util.Arrays;

public class tryProgs2 {
    public static void moveZeroes(int[] nums) {
        int index = 0;
        for (int i=0; i < nums.length; i++) {
        	if (nums[i] != 0) {
        		nums[index++] = nums[i];
        }
      }
        while (index < nums.length) {
        	nums[index++] = 0;
        }
    }
    public static void main(String[] args) {
    	int[] arr = {0, 1, 0, 3, 12};
    	moveZeroes(arr);
        System.out.println("Array after moving zeros are: "+Arrays.toString(arr));
    }
}
Array after moving zeros are: [1, 3, 12, 0, 0]
****************************************************************************************************************
package WebHandling;

import java.util.Stack;

public class tryProgs2 {  // OR rename class to MyQueue
    Stack<Integer> input = new Stack<>();
    Stack<Integer> output = new Stack<>();
    public void push(int x) {
        input.push(x);
    }
    public int pop() {
        peek();  // Ensure elements are transferred if output is empty
        return output.pop();
    }
    public int peek() {
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                output.push(input.pop());
            }
        }
        return output.peek();
    }
    public boolean empty()  {
        return input.isEmpty() && output.isEmpty();
    }
    public static void main(String[] args) {
        tryProgs2 q = new tryProgs2();  // Use current class name
        q.push(1);
        q.push(2);
        System.out.println(q.peek());  // Output: 1
        System.out.println(q.pop());   // Output: 1
        System.out.println(q.empty()); // Output: false
    }
}
1
1
false
****************************************************************************************************************
package WebHandling;

public class tryProgs2 {
	public static int majorityElement(int[] nums) {
		int count=0, candidate=0;
		for (int num : nums) {
			if (count == 0)  candidate = num;
			count += (num == candidate) ? 1 : -1;
		}
	return candidate;
	}
    public static void main(String[] args) {
        System.out.println("majorityElement is: "+(majorityElement(new int[]{2,2,1,1,1,2,2})));
    }
}
majorityElement is: 2
****************************************************************************************************************
package WebHandling;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class tryProgs2 {
	public static int[] intersection(int[] num1, int[] num2) {
		Set<Integer> set1 = new HashSet<>();
		for (int num : num1) set1.add(num);
		Set<Integer> resultSet = new HashSet<>();
		for (int num : num2)
		{
			if (set1.contains(num))  resultSet.add(num);
		}
	 return resultSet.stream().mapToInt(i -> i).toArray();
	}
    public static void main(String[] args) {
        System.out.println("majorityElement is: "+Arrays.toString(intersection(new int[]{1, 2, 2, 1}, new int[] {2, 2})));
    }
}
majorityElement is: [2]
****************************************************************************************************************
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

class Main {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();
        int[] arr1 = {1, 3, 2, 7, 10};
        int[] arr2 = {7, 2, 5, 9, 12};
        ArrayList<Integer> merged = new ArrayList<>();
        int i = 0, j = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                merged.add(arr1[i++]);
            } else {
                merged.add(arr2[j++]);
            }
        }
        while (i < arr1.length) merged.add(arr1[i++]);
        while (j < arr2.length) merged.add(arr2[j++]);
        set.addAll(merged);
        for (int num : set) {
            System.out.print(num + " ");
        }
    }
}
1 2 3 5 7 9 10 12
****************************************************************************************************************
import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 3, 4, 5, 5, 6 }; 
        int[] uniqueArray = removeDuplicates(arr); 
        System.out.print("Array with duplicates removed: ");
        for (int num : uniqueArray) {
            System.out.print(num + " ");
        }
    }
    public static int[] removeDuplicates(int[] arr) {
        int[] uniqueArray = new int[arr.length];
        int j = 0;
        for (int i=0; i<arr.length-1; i++) {
            if (arr[i] != arr[i+1])
                uniqueArray[j++] = arr[i];
        }
        uniqueArray[j++] = arr[arr.length-1];
        return Arrays.copyOf(uniqueArray, j);
    }
}
Array with duplicates removed: 1 2 3 4 5 6 
****************************************************************************************************************
import java.util.Arrays;
import java.util.Collections;

class Main {
    public static void main(String[] args) {
        int[] arr = { 64, 34, 25, 12, 22, 11, 90 }; 
        
        bubbleSort(arr); 
        
        System.out.println("Sorted array: " + Arrays.toString(arr));
        System.out.println("Max in an array: " + arr[arr.length - 1]);
        System.out.println("Second Max in an array: " + arr[arr.length - 2]);
        // Reverse manually
        System.out.print("Reverse array: [");
        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i]);
            if (i != 0) System.out.print(", ");
        }
        System.out.println("]");
    }

    // Bubble Sort
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}
Sorted array: [11, 12, 22, 25, 34, 64, 90]
Max in an array: 90
Second Max in an array: 64
Reverse array: [90, 64, 34, 25, 22, 12, 11]
****************************************************************************************************************


****************************************************************************************************************


****************************************************************************************************************


****************************************************************************************************************


****************************************************************************************************************


****************************************************************************************************************
