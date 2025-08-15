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
