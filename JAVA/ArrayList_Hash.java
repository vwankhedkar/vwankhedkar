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
import java.util.ArrayList;
import java.util.List;
class Main {
    public List<List<String>> findIntersection() {
        List<String> list1 = new ArrayList<>();
        List<String> list2 = new ArrayList<>();
        list1.add("A");
        list1.add("B");
        list1.add("C");
        list1.add("D");
        list1.add("E");
        System.out.println("List names : "+list1);
        list2.add("P");
        list2.add("Q");
        list2.add("R");
        list2.add("D");
        list2.add("E");
        System.out.println("List names : "+list2);
        ArrayList<String> common = new ArrayList<>();
        for (String name : list1) 
            if (list2.contains(name))
                common.add(name);
        System.out.println("Common List names : "+common);
        List<List<String>> bothLists = new ArrayList<>();
        bothLists.add(list1);
        bothLists.add(list2);
        return bothLists;
        }
    public static void main(String[] args) {
        Main example = new Main();
        example.findIntersection();
    }
}
List names : [A, B, C, D, E]
List names : [P, Q, R, D, E]
Common List names : [D, E]
******************************************************************************
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
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String input = scanner.nextLine();
        System.out.println("Original string is : " + input);
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
    System.out.println("Output in Alpha: " + alphaPart.toString());
    System.out.println("Output in Numeric: "+numericPart.toString()); 
    }
}
Enter a string : Subbu123raj
Original string is : Subbu123raj
Output in Alpha: Subburaj
Output in Numeric: 123
*************************************************************************
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String input = scanner.nextLine();
        System.out.println("Original string is : " + input);
        separateCharacters(input);
    }
    public static void separateCharacters(String input) {
        StringBuilder lowerCase = new StringBuilder();
        StringBuilder upperCase = new StringBuilder();
        for (char ch : input.toCharArray()) {
            if (Character.isLowerCase(ch))
                lowerCase.append(ch);
            else if (Character.isUpperCase(ch))
                 upperCase.append(ch);
        }
    System.out.println("Output in lowercase: "+lowerCase);
    System.out.println("Output in uppercase: "+upperCase); 
    }
}
Enter a string : aBACbcEDed
Original string is : aBACbcEDed
Output in lowercase: abced
Output in uppercase: BACED
*************************************************************************
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String input = scanner.nextLine();
        String output = getCharacterCount(input); 
        System.out.println("Output: " + output); 
    }
    public static String getCharacterCount(String str) {
        StringBuilder result = new StringBuilder();
        int count = 1;
        for (int i=0; i<str.length();i++) {
             if (i+1<str.length() && str.charAt(i)==str.charAt(i+1))
                 count++;
             else {
                 result.append(str.charAt(i)).append(count);
                 count = 1;
             }
           } 
           return result.toString(); 
    }
}
Enter a string : aabbcccdd
Output: a2b2c3d2
*************************************************************************
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
class Main {
    public void mergeListRemoveDuplicates(List<String> list1, List<String> list2) {
        System.out.println("List1 is :: "+list1);
        System.out.println("List2 is :: "+list2);
        list1.addAll(list2);
        System.out.println("After merging 2 lists: "+list1);
        List<String> uniqueList = new ArrayList<>();
        for (String name : list1)
            if (!uniqueList.contains(name))
               uniqueList.add(name);
        System.out.println("UniqueList names : "+uniqueList);
    }
    public static void main(String[] args) {
        List<String> list1 = new ArrayList<>(Arrays.asList("A","B","C","D"));
        List<String> list2 = new ArrayList<>(Arrays.asList("P","Q","C","D"));
        Main example = new Main();
        example.mergeListRemoveDuplicates(list1, list2);
    }
}
List1 is :: [A, B, C, D]
List2 is :: [P, Q, C, D]
After merging 2 lists: [A, B, C, D, P, Q, C, D]
UniqueList names : [A, B, C, D, P, Q]
*************************************************************************
import java.util.ArrayList;
import java.util.List;
class Main {
    public List<String> arrayFirstLastSameEle() {
        List<String> nameList = new ArrayList<>();
        nameList.add("A");
        nameList.add("B");
        nameList.add("C");
        nameList.add("D");
        nameList.add("E");
        nameList.add("level");
        nameList.add("radar");
        nameList.add("hello");
        System.out.println("Original List : " + nameList);
        List<String> newList = new ArrayList<>();
        for (String name : nameList) {
            if (name == null || name.isEmpty())
                continue;
            char first = name.charAt(0);
            char last = name.charAt(name.length() - 1);
            if (first == last) {
                newList.add(name);
            }
        }
        System.out.println("Filtered List (first == last): " + newList);
        return newList;
    }
    public static void main(String[] args) {
        Main example = new Main();
        example.arrayFirstLastSameEle();
    }
}
Original List : [A, B, C, D, E, level, radar, hello]
Filtered List (first == last): [A, B, C, D, E, level, radar]
*************************************************************************
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
class Main {
    public String ArrayLongestName(List<String> nameList) {
        String longestName = null;
        int max = 0;
        for (String name : nameList) {
            int curr = name.length();
            if (curr > max) {
                max = curr;
                longestName = name;
            }
    }
        System.out.println("longestName is : " + longestName);
        return longestName;
    }
    public static void main(String[] args) {
        List<String> sampleNames = new ArrayList<>(Arrays.asList("Vaish","Sandip","Sumit","Hetarth","Abhyant","Swaraj"));
        Main example = new Main();
        example.ArrayLongestName(sampleNames);
    }
}
longestName is : Hetarth
*************************************************************************
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
class Main {
    public List<Integer> reverseArrayList(List<Integer> list) {
        System.out.println("Original list : "+list);
        int size = list.size();
        for (int i=0; i<size/2; i++) {
            Integer temp = list.get(i);
            list.set(i, list.get(size-1-i));
            list.set(size-1-i, temp);
        }
        System.out.println("ReversedList : "+list);
        return list;
    }
    public static void main(String[] args) {
        Main example = new Main();
        List<Integer> numbers = new ArrayList<Integer>();
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(40);
        numbers.add(50);
        example.reverseArrayList(numbers);
    }
}
Original list : [10, 20, 30, 40, 50]
ReversedList : [50, 40, 30, 20, 10]
*************************************************************************
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
class Main {
    public List<String> findDuplicateWOSet(List<String> inputList) {
        inputList.add("Vaishali");
        inputList.add("Sandeep");
        inputList.add("Sumit");
        inputList.add("Shiv");
        inputList.add("Shambhu");
        inputList.add("Chiku");
        inputList.add("Vaishali");
        inputList.add("Shiv");
        System.out.println("Originaal List : "+inputList);
        String[] arrayL = inputList.toArray(new String[0]);
        System.out.println("To ArrayList : "+Arrays.toString(arrayL));
        List<String> uniqueList = new ArrayList<String>();
        List<String> duplicateList = new ArrayList<String>();
        for (String name : inputList) {
            if (uniqueList.contains(name)) {
                if (!duplicateList.contains(name))
                   duplicateList.add(name);
            }
            else
                uniqueList.add(name);
        }
        System.out.println("Duplicate list is : "+duplicateList);
        return duplicateList;
    }
    public static void main(String[] args) {
        Main example = new Main();
        example.findDuplicateWOSet(new ArrayList<String>());
    }
}
Originaal List : [Vaishali, Sandeep, Sumit, Shiv, Shambhu, Chiku, Vaishali, Shiv]
To ArrayList : [Vaishali, Sandeep, Sumit, Shiv, Shambhu, Chiku, Vaishali, Shiv]
Duplicate list is : [Vaishali, Shiv]
*************************************************************************
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
class Main {
    public List<String> filteringList() {
        List<String> inputList = new ArrayList<String>();
        inputList.add("Vaishali");
        inputList.add("Sandeep");
        inputList.add("Sumit");
        inputList.add("Hetarth");
        inputList.add("Shambhu");
        inputList.add("Chiku");
        inputList.add("Vaishali");
        List<String> inputList1 = new ArrayList<String>();
        for (String name : inputList) {
            if (name != null && !name.isEmpty()) {
                String firstLetter = name.substring(0,1).toUpperCase();
                if (firstLetter.equals("S") || firstLetter.equals("V"))
                    inputList1.add(name);
            }
        }
        System.out.println("Names starting with S and V are : "+inputList1);
        return inputList1;
    }
    public static void main(String[] args) {
        Main example = new Main();
        example.filteringList();
    }
}
Names starting with S and V are : [Vaishali, Sandeep, Sumit, Shambhu, Vaishali]
*************************************************************************
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
class Main {
    public void frequencyWords() {
        List<String> nameList = new ArrayList<String>();
        nameList.add("Vaishali");
        nameList.add("Sandeep");
        nameList.add("Sumit");
        nameList.add("Hetarth");
        nameList.add("Shambhu");
        nameList.add("Chiku");
        nameList.add("Vaishali");
        Map<String, Integer> freqMap = new HashMap<String, Integer>();
        for (String name : nameList) {
            if (freqMap.containsKey(name))
               freqMap.put(name, freqMap.get(name)+1);
            else
               freqMap.put(name, 1);
        }
        for (Map.Entry<String, Integer> entry : freqMap.entrySet())
            System.out.println(entry.getKey() + " Occurs : "+ entry.getValue()+" times");
    }
    public static void main(String[] args) {
        Main example = new Main();
        example.frequencyWords();
    }
}
Sandeep Occurs : 1 times
Hetarth Occurs : 1 times
Vaishali Occurs : 2 times
Shambhu Occurs : 1 times
Sumit Occurs : 1 times
Chiku Occurs : 1 times
*************************************************************************
import java.util.*;
class Student {
    int id; String name; Student(int id, String n) {
        this.id = id; this.name = n; }}
class SMS {
    Map<Integer,Student> map = new HashMap<>();
    void add(Student s) {map.put(s.id,s);}
    Student get(int id) { return map.get(id); }
}
class Main {
    public static void main(String[] args) {
        SMS s = new SMS();
        s.add(new Student(1, "Max"));
        System.out.println(s.get(1).id);
        System.out.println(s.get(1).name);
    }
}	1
Max
*************************************************************************
import java.util.*;
 class Employee { int id; String name; Employee(int id,String n){this.id=id;this.name=n;} }
class EMS {
    Map<Integer, Employee> map = new HashMap<>(); 
    void add(Employee e) {map.put(e.id,e); } 
    Employee get(int id) {return map.get(id);}
}
class Main {
    public static void main(String[] args) {
        EMS s = new EMS();
        s.add(new Employee(1,"Ana"));
        System.out.println(s.get(1).name);
}  }		===>		Ana
*************************************************************************
import java.util.*;
class Account {
    private int balance;
    Account(int bal) {this.balance=bal; }
    synchronized void deposit(int amt) { balance+=amt; }
    synchronized boolean withdraw(int amt) 
    { if (amt<=balance) {
        balance-=amt; return true; } return false; } 
        synchronized int balance() { return balance; }} 
class Main {
    public static void main(String[] args) {
        Account acc=new Account(1000);
        acc.deposit(500); acc.withdraw(200);
        System.out.println(acc.balance());
    }
}		===>		1300
*************************************************************************
 import java.util.*;
 class Book { String id,title; boolean issued; Book(String id,String t){this.id=id;this.title=t;} }
 class Library {
    Map<String,Book> books=new HashMap<>();
    void add(Book b){ books.put(b.id,b); }
    boolean issue(String id){ Book b=books.get(id); if(b!=null && !b.issued){ b.issued=true; return true; } 
    return false; }
    void list(){ books.values().forEach(b->System.out.println(b.id+":"+b.title+":"+b.issued)); }
 }
 public class Main {
    public static void main(String[] args) {
        Library lib=new Library(); lib.add(new Book("1","Java Basics")); lib.add(new Book("2","DSA"));
        lib.issue("1"); lib.list();
    }
 }			==> 1:Java Basics:true
2:DSA:false
*************************************************************************
import java.util.*;
class Main {
    static void print(Integer x) { System.out.println(x); }
    public static void main(String[] args) { 
        List<Integer> list = Arrays.asList(1,2,3);
        list.forEach(Main::print); }  }		==>		1 2 3 
*************************************************************************
import java.util.*;
 import java.util.stream.*;
 public class Main {
    public static void main(String[] args) {
        List<Integer> nums=Arrays.asList(1,2,3,4,5);
        int sumSquaresOfEven = nums.stream().filter(x->x%2==0).map(x->x*x).reduce(0,Integer::sum);
        List<Integer> doubled = nums.stream().map(x->x*2).collect(Collectors.toList());
        System.out.println(sumSquaresOfEven + " " + doubled);
    }
 }		===>		20 [2, 4, 6, 8, 10]
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
