import java.util.Objects;
public class Main{
    public int id;
    private String name;
    public Main(int id, String name) {
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
        if (obj==null||getClass()!=obj.getClass())
            return false;
        Main student = (Main) obj;
        return id == student.id && Objects.equals(name, student.name);
    }
    public static void main(String[] args) {
        Main student1 = new Main(1,"Alice");
        Main student2 = new Main(2,"Bob");
        Main student3 = new Main(1,"Alice");
        System.out.println("student1.equals(student2): "+ student1.equals(student2));
        System.out.println("student1.equals(student3): "+ student1.equals(student3));
        System.out.println("Hashcode of student1:"+student1.hashCode());
        System.out.println("Hashcode of student2:"+student2.hashCode());
        System.out.println("Hashcode of student3:"+student3.hashCode());
    }
}
student1.equals(student2): false
student1.equals(student3): true
Hashcode of student1:63351360
Hashcode of student2:67988
Hashcode of student3:63351360
*************************************************************************************************
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
public class Main {
    public static void main(String[] args) {
        int[] array = {1, 1, 2, 2, 3, 4, 5, 5, 6, 6};
        List<Integer> result = findNonRepeatedElements(array);
        System.out.println("Non-repeated elements : "+result);
    }
    public static List<Integer> findNonRepeatedElements(int[] array) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : array) {
            countMap.put(num, countMap.getOrDefault(num, 0)+1);
        }
        List<Integer> nonRepeatedElements = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == 1) {
                nonRepeatedElements.add(entry.getKey());
            }
        }
        return nonRepeatedElements;
    }
}  ==>  Non-repeated elements : [3, 4]
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	    int[] count = countOddAndEven(array);
		System.out.println("Even numbers count : "+count[1]);
		System.out.println("Odd numbers count : "+count[0]);
	}
	public static int[] countOddAndEven(int[] array) {
	    int[] count = new int[2];
	    for (int num : array) {
	        if (num % 2 == 0) {
	            count[1]++;
	        } else
	        count[0]++;
	    }
	    return count;
	}
}
Even numbers count : 4
Odd numbers count : 5
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {5, 2, 9, 1, 6, 3,0};
        int max = findMaximum(array);
        int min = findMinimum(array);
        System.out.println("Maximum value in the array : "+ max);
        System.out.println("Minimum value in the array : "+ min);
	}
	public static int findMaximum(int[] array) {
	    if (array.length == 0) {
	        throw new IllegalArgumentException("Array must not be empty");
	    }
	    int max = array[0];
	    for (int i=1; i<array.length-1; i++) {
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
	    for (int i=1; i<= array.length-1; i++) {
	        if (array[i] < min) 
	            min = array[i];
	    }
	    return min;
	} 
}
Maximum value in the array : 9
Minimum value in the array : 0
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    String[] array = {"5", "2", "9", "a", "1", "6", "#", "3"};
        int sum = sumIntegers(array);
        System.out.println("Sum of the integers in array : "+ sum);
	} 
	public static int sumIntegers(String[] array) {
	    int sum = 0;
	    for (String element : array) {
	        try {
	            int num = Integer.parseInt(element);
	            sum += num;
	        } catch (NumberFormatException e) {
	            // Ignore elements
	        }
	    }
	    return sum;
	}
}	==>	Sum of the integers in array : 26
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {5, 2, 9, 1, 6, 3};
	    int target = 6;
        int index= linearSearch(array, target);
        if (index != -1) {
            System.out.println("Element " + target + " found at index : " + index);
        } else {
            System.out.println("Element " + target + " not found in the array");
        }
	}
	public static int linearSearch(int[] array, int target) {
	    for (int i=0; i<array.length; i++) {
	        if (array[i] == target) {
	            return i;
	        }
	    }
	    return -1;
	}
} ==>	Element 6 found at index : 4
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {5, 2, 9, 1, 6, 3};
        int[] result = findLargestAndSmallest(array);
        System.out.println("Smallest element: " + result[0]);
        System.out.println("Largest element: " + result[1]);
	}
	public static int[] findLargestAndSmallest(int[] array) {
		if (array == null || array.length == 0) {
		    throw new IllegalArgumentException("Array must not be null or empty");
		}
		int smallest = array[0];
		int largest = array[0];
		for (int num : array) {
		    if (num < smallest)
		        smallest = num;
		    if (num > largest)
		        largest = num;
		}
		return new int[]{smallest, largest};
	}
}
Smallest element: 1
Largest element: 9
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {1, 2, 4, 5, 6}; // Missing number is 3
	    int missingNumber = findMissingNumber(array);
        System.out.println("The missing number is : " + missingNumber);
	}
	public static int findMissingNumber(int[] array) {
		int n = array.length+1;
		int totalSum = n*(n+1)/2;
		int arraySum = 0;
		for (int num : array) {
		    arraySum += num;
		}
		return totalSum - arraySum;
	}
}	===>	The missing number is : 3
*************************************************************************************************
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
public class Main
{
	public static void main(String[] args) {
	    ArrayList<Integer> arrayList = new ArrayList<>();
	    arrayList.add(5);
	    arrayList.add(2);
	    arrayList.add(9);
	    arrayList.add(1);
	    arrayList.add(6);
	    arrayList.add(2);
	    arrayList.add(5);
	    ArrayList<Integer> uniqueList = removeDuplicates(arrayList);
        System.out.println("Arraylist with duplicates removed");
        for (int num : uniqueList) {
            System.out.print(num + " ");
        }
	}
	public static ArrayList<Integer> removeDuplicates(ArrayList<Integer> list) {
		Set<Integer> lstSet = new HashSet<>(list);
		return new ArrayList<>(lstSet);
	}
}	
Arraylist with duplicates removed
1 2 5 6 9 
*************************************************************************************************
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
public class Main
{
	public static void main(String[] args) {
	    int[] array = {5, 2, 9, 1, 6, 2, 5};
	    int[] uniqueArray = removeDuplicates(array);
        System.out.println("Array with duplicates removed : ");
        for (int num : uniqueArray) {
            System.out.print(num + " ");
        }
	}
	public static int[] removeDuplicates(int[] array) {
		Set<Integer> set = new HashSet<>();
		for (int num : array) {
		    set.add(num);
		}
		int[] result = new int[set.size()];
		int i = 0;
		for (int num : set) 
		    result[i++] = num;
		return result;
	}
}	==>		Array with duplicates removed : 
1 2 5 6 9 
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {5, 2, 9, 1, 6};
        selectionSort(array);
        System.out.print("Sorted Array : ");
        for (int num : array) {
            System.out.print(num + " ");
        }
	}
	public static void selectionSort(int[] array) {
	    int n = array.length;
	    for (int i=0; i<n-1; i++) {
	        int minIndex = i;
	        for (int j=i+1; j<n; j++) {
	            if (array[j] < array[minIndex]) {
	                minIndex = j;
	            }
	        }
	        int temp = array[i];
	        array[i] = array[minIndex];
	        array[minIndex] = temp;
	    }
	}
}	==>		Sorted Array : 1 2 5 6 9 
*************************************************************************************************
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
public class Main
{
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
        }  else {
            System.out.println("The arrayList is empty");
        }
    }
}
First element: Apple
Last element: Elderberry
*************************************************************************************************
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
public class Main
{
	public static void main(String[] args) {
	    int[] array1 = {1, 2, 3, 4, 5};
	    int[] array2 = {4, 5, 6, 7, 8};
	    Set<Integer> commonElements = findCommonElements(array1, array2);
	    System.out.println("Common Elements : " +commonElements);
    }
    public static Set<Integer> findCommonElements(int[] array1, int[] array2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> commonSet = new HashSet<>();
        for (int num : array1)
            set1.add(num);
        for (int num : array2)  {
            if (set1.contains(num)) {
                commonSet.add(num);
            }
        }
        return commonSet;
    }
} ===>	Common Elements : [4, 5]
*************************************************************************************************
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
public class Main
{
	public static void main(String[] args) {
	    String s1 = "abcabcbb"; // Expected: "abc", length 3
        String s2 = "bbbbb";    // Expected: "b", length 1
        String s3 = "pwwkew";   // Expected: "wke", length 3
        String s4 = "";         // Expected: "", length 0
        System.out.println("Longest substring without repeatingcharacters in s1: "
        +lenOfLongestSubstring(s1));
        System.out.println("Longest substring without repeatingcharacters in s2: "
        +lenOfLongestSubstring(s2));
        System.out.println("Longest substring without repeatingcharacters in s3: "
        +lenOfLongestSubstring(s3));
        System.out.println("Longest substring without repeatingcharacters in s4: "
        +lenOfLongestSubstring(s4));
    }
    public static int lenOfLongestSubstring(String s) {
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
Longest substring without repeatingcharacters in s1: 3
Longest substring without repeatingcharacters in s2: 1
Longest substring without repeatingcharacters in s3: 3
Longest substring without repeatingcharacters in s4: 0
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    String input = "32400121200";
        String formattedOutput = String.format("%011d", Long.parseLong(input));
        System.out.println("Formatted output: " + formattedOutput);
        String output = rearrangeDigits(input);
        System.out.println("Output : " + output);
	}
	public static String rearrangeDigits(String input) {
	    StringBuilder digits = new StringBuilder();
	    StringBuilder nonDigits = new StringBuilder();
	    for (char c : input.toCharArray()) {
	        if (Character.isDigit(c)) {
	            digits.append(c);
	        } else {
	            nonDigits.append(c);
	        }
	    }
	    return digits.toString() + nonDigits.toString();
	}
}
Formatted output: 32400121200
Output : 32400121200
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
