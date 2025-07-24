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
************************************************************************************
************************************************************************************
************************************************************************************
************************************************************************************
