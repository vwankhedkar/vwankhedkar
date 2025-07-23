package com.basic;
import java.util.*;
public class nameArrayList {

	public static void main(String[] args) {
		ArrayList<String> namedList = new ArrayList<String>();   // List<String> namedList = new LinkedList<String>();
		String[] names = {"Ann", "Bob", "Carol"};
		for (int k=0; k<names.length; k++)
			namedList.add(names[k]);
		for (int k=0; k<names.length; k++)
			System.out.println(namedList.get(k));
	}

}
-----------------
package com.basic;
import java.util.*;
public class nameArrayList {

	public static void main(String[] args) {
		List<String> namedList = new ArrayList<>();
		String[] names = {"Ann", "Bob", "Carol"};
		for (int k=0; k<names.length; k++)
			namedList.add(names[k]);
		Iterator<String> it = namedList.iterator();
		while (it.hasNext())
			System.out.println(it.next());
	}
}
------------------
package com.basic;
import java.util.*;
public class nameArrayList {

	public static void main(String[] args) {
		List<String> namedList = new ArrayList<>();
		String[] names = {"Ann", "Bob", "Carol"};
		ListIterator<String> it = namedList.listIterator();
		for (int k=0; k<names.length; k++)
			namedList.add(names[k]);
		it = namedList.listIterator();
		while (it.hasNext())
			System.out.println(it.next());
	}
}

Ann
Bob
Carol
***************************************************************
package com.basic;
import java.util.HashSet;
import java.util.Set;
public class HashSetDemo {

	public static void main(String[] args) {
		Set<String> fruitSet = new HashSet<String>();
		fruitSet.add("Apple");
		fruitSet.add("Banana");
		fruitSet.add("Pear");
		fruitSet.add("Strawberry");
		System.out.println("Here are the elements: ");
		for (String element:fruitSet)
			System.out.println(element);
		System.out.println("Trying to add Banana to " + "the set again");
		if (!fruitSet.add("Banana"))
			System.out.println("Banana was not added again");
		System.out.println("\nHere are the elements once again");
		for (String element:fruitSet)
			System.out.println(element);
	}
}
Here are the elements: 
Apple
Pear
Strawberry
Banana
Trying to add Banana to the set again
Banana was not added again

Here are the elements once again
Apple
Pear
Strawberry
Banana
************************************************
package com.basic;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
public class subStrNonRepeated {
	public static void main(String[] args) {
		Map<String,Integer> mp = new HashMap();
		mp.put("a", 1);
		mp.put("b", 2);
		mp.put("c", 3);
		mp.put("d", 4);
		mp.put("e", 5);
		mp.put("f", 6);
		ArrayList<Integer> sorted = new ArrayList<>(mp.values());
		sorted.sort(Comparator.reverseOrder());
		int highest_value = sorted.get(0);
		mp.entrySet().removeIf(a->a.getValue()==highest_value);
		System.out.println(mp);
	}
}
{a=1, b=2, c=3, d=4, e=5}
***************************************************
package com.basic;

import java.util.HashSet;
import java.util.Set;

public class subStrNonRepeated {

    public static void main(String[] args) {
        String name = "pjdkaljdsfllalaf";
        String longestSubstring = "";

        for (int i = 0; i < name.length(); i++) {
            StringBuilder s = new StringBuilder();
            Set<Character> seenChars = new HashSet<>();

            for (int j = i; j < name.length(); j++) {
                char currentChar = name.charAt(j);

                if (seenChars.contains(currentChar)) {
                    break;
                }

                s.append(currentChar);
                seenChars.add(currentChar);
            }

            if (s.length() > 0) {
                System.out.println(s.toString());
                if (s.length() > longestSubstring.length()) {
                    longestSubstring = s.toString();
                }
            }
        }

        System.out.println("\nLongest substring without repeating characters: " + longestSubstring);
    }
}
pjdkal
jdkal
dkalj
kaljdsf
aljdsf
ljdsf
jdsfl
dsfl
sfl
fl
l
la
al
laf
af
f
******************************************************************************
package WebHandling;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;

public class tryProgs2 {
    public static void main(String[] args) {
    	HashMap<Integer, String> hm = new HashMap<>();
    	hm.put(100, "John");
    	hm.put(102, "Scott"); 
        hm.put(103, "Mary"); 
        hm.put(104, "Scott"); 
        hm.put(102, "David"); 
        System.out.println("Hashmap is: "+hm+" Size of Hashmap is: "+hm.size());
        System.out.println("Keys are : "+hm.keySet() + " and Values are : "+hm.values());
        // Read all the elements  → using for-each loop
        for (int k : hm.keySet())
        	System.out.println(k+" : "+hm.get(k));
        // using Iterator 
        System.out.println("\nUsing Iterator:"); 
        Iterator<Entry<Integer,String>> it = hm.entrySet().iterator();
        while (it.hasNext()) {
        	Entry<Integer, String>entry = it.next();
        	System.out.println(entry.getKey()+" "+entry.getValue());
        }
        hm.clear();
        System.out.println("Is hashkey empty : " + hm.isEmpty());
    }
}
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
*************************************************************************************
	
