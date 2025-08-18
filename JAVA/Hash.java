package com.tryPrograms;
import java.util.Objects;
public class Main {
		private int id;
		private String name;
		public Main(int id, String name) {
			this.id = id;
			this.name = name;
		}
		// Getters and setters (omitted for brevity)
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
			Main student = (Main) obj; 
			return id == student.id && Objects.equals(name, student.name); 
		} 
		public static void main(String[] args) {
			Main student1 = new Main(1, "Alice"); 
			Main student2 = new Main(2, "Bob"); 
			Main student3 = new Main(1, "Alice");
			System.out.println("student1.equals(student2): " + student1.equals(student2));
			System.out.println("student1.equals(student3): " + student1.equals(student3));
			System.out.println("HashCode of student1 : " + student1.hashCode());
			System.out.println("HashCode of student2 : " + student2.hashCode());
			System.out.println("HashCode of student3 : " + student3.hashCode());
	}
}	
student1.equals(student2): false
student1.equals(student3): true
HashCode of student1 : 63351360
HashCode of student2 : 67988
HashCode of student3 : 63351360
*************************************************************************
package com.tryPrograms;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class Main {
	public static void main(String[] args) {
		int[] array =  {1, 1, 2, 2, 3, 4, 5, 5, 6, 6};
		List<Integer> result = findNonRepeatedElements(array);
		System.out.print("Non-repeated elements : "+result);
	}
	public static List<Integer> findNonRepeatedElements(int[] array) {
		Map<Integer, Integer> countMap = new HashMap<>();
		for (int num : array) {
			countMap.put(num, countMap.getOrDefault(num, 0) +1);
		}
		List<Integer> nonRepeatedElements = new ArrayList<>();
		for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
			if (entry.getValue() == 1) {
				nonRepeatedElements.add(entry.getKey());
			}
		}
		return nonRepeatedElements;
	}
}	    ==> Non-repeated elements : [3, 4]
*************************************************************************
package com.tryPrograms;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
public class Main {
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
		System.out.print("ArrayList with duplicates removed:");
		for (int num : uniqueList) 
			System.out.print(num + " ");
	}
	public static ArrayList<Integer> removeDuplicates(ArrayList<Integer> list) {
		Set<Integer> set = new HashSet<Integer>(list);
		return new ArrayList<>(set);
	}
}	
ArrayList with duplicates removed:1 2 5 6 9 
*************************************************************************
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 6, 2, 5}; 
        int[] uniquearr = removeDuplicates(arr);

        System.out.println("Array with duplicates removed:");
        for (int num : uniquearr)
            System.out.print(num + " ");
    }

    public static int[] removeDuplicates(int[] array) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : array)
            set.add(num);

        int[] result = new int[set.size()];
        int i = 0;
        for (int num : set)
            result[i++] = num;

        return result;
    }
}
Array with duplicates removed:
1 2 5 6 9 
*************************************************************************
// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
        int[] array =  {5, 2, 9, 1, 6}; 
        selectionSort(array);
        System.out.println("Sorted Array");
        for (int num : array)
            System.out.print(num + " ");
    }
   public static void selectionSort(int[] array) {
       int n = array.length;
       for (int i=0; i<n-1; i++) {
           int minindex = i;
           for (int j=i+1; j<n; j++) {
               if (array[j] < array[minindex])
                  minindex = j;
           }
       int temp = array[i];
       array[i] = array[minindex];
       array[minindex] = temp;
       }
   }	Sorted Array
}		1 2 5 6 9 
*************************************************************************
import java.util.HashSet;
import java.util.Set; 
public class CommonElements { 
    public static void main(String[] args) { 
        int[] array1 = {1, 2, 3, 4, 5}; 
        int[] array2 = {4, 5, 6, 7, 8}; 
        Set<Integer> commonElements = findCommonElements(array1, 
        array2); 
        System.out.println("Common elements: " + commonElements); 
} 
public static Set<Integer> findCommonElements(int[] array1, 
    int[] array2) { 
    Set<Integer> set1 = new HashSet<>(); 
    Set<Integer> commonSet = new HashSet<>(); 
    // Add elements of the first array to the set 
    for (int num : array1) { 
        set1.add(num); 
    } 
    for (int num : array2) { 
        if (set1.contains(num)) { 
            commonSet.add(num); 
        } 
    } 
    return commonSet; 
   } 
}		Common elements: [4, 5]
*************************************************************************
import java.util.HashSet;
class Main {
    public static void main(String[] args) {
        String s1 = "abcabcbb"; // Expected: "abc", length 3 
        String s2 = "bbbbb"; // Expected: "b", length 1
        String s3 = "pwwkew"; // Expected: "wke", length 3
        String s4 = ""; // Expected: "", length 0
        System.out.println("Longest substring without repeating characters in s1: " + lengthOfLongestSubstring(s1));
        System.out.println("Longest substring without repeating characters in s2: " + lengthOfLongestSubstring(s2));
        System.out.println("Longest substring without repeating characters in s3: " + lengthOfLongestSubstring(s3));
        System.out.println("Longest substring without repeating characters in s4: " + lengthOfLongestSubstring(s4)); // Output: 0 
    }
    public static int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxLength=0;
        int start=0;
        int end=0;
        while (end < s.length()) {
            char currentChar = s.charAt(end);
            if (!set.contains(currentChar)) {
                set.add(currentChar);
                maxLength = Math.max(maxLength,end-start+1);
                end++;
            } else {
                set.remove(s.charAt(start));
                start++;
            }
        }
        return maxLength;
    }
}
Longest substring without repeating characters in s1: 3
Longest substring without repeating characters in s2: 1
Longest substring without repeating characters in s3: 3
Longest substring without repeating characters in s4: 0
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

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
