package com.tryPrograms;
public class StringProgs {
	public static void main(String[] args) {
		System.out.println(revStr("apple"));
		System.out.println(revStr("vaishali1234"));
		System.out.println(revStr("9835732848"));
		System.out.println(revStr("12345vaishali"));
	}
	public static String revStr(String str) {
		StringBuilder res = new StringBuilder();
		for (int i=str.length()-1; i>=0; i--) {
			res.append(str.charAt(i));
		}
		return res.toString();
	}
}
elppa
4321ilahsiav
8482375389
ilahsiav54321
*************************************************************************************
package com.tryPrograms;
import java.util.Arrays;
public class StringProgs {
	public static void main(String[] args) {
		int[] inputArr = new int[] {1,2,3,4,5};
		System.out.println(Arrays.toString(inputArr));
		revArr(inputArr);
		System.out.println(Arrays.toString(inputArr));
	}
	public static void revArr(int[] arr) {
		int start=0;
		int end = arr.length-1;
		while (start < end) {
			int tmp = arr[start];
			arr[start] = arr[end];
			arr[end] = tmp;
			start ++;
			end --;
		}
	}
}
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
*************************************************************************************
package com.tryPrograms;
public class StringProgs {
	public static void main(String[] args) {
		System.out.println(revWords("apple banana kiwi"));
		System.out.println(revWords("rice wheat"));
		System.out.println(revWords("cooking cleaning"));
	}
	public static String revWords(String str) {
		StringBuilder res = new StringBuilder();
		String[] words = str.split(" ");
		for (int i=words.length-1; i>=0; i--) {
			res.append(words[i]).append(" ");
		}
		return res.toString().trim();
	}
}
kiwi banana apple
wheat rice
cleaning cooking
*************************************************************************************
package com.tryPrograms;
public class StringProgs {
	public static void main(String[] args) {
		System.out.println(isPal("anna")); // true
		System.out.println(isPal("civic")); // true
		System.out.println(isPal("apple")); // false
		System.out.println(isPal("level")); // true
	}
	public static boolean isPal(String str) {
		int start =0 ;
		int end = str.length()-1;
		while (start < end) {
			if (str.charAt(start) != str.charAt(end)) {
				return false;
			}
			start ++;
			end --;
		}
    return true;
   }
}
true
true
false
true
*************************************************************************************
package com.tryPrograms;

import java.util.HashMap;
import java.util.Map;

public class StringProgs {
	public static void main(String[] args) {
		System.out.println(MinMax(new int[]{4, 781, 8, 99, 103})); 
		System.out.println(MinMax(new int[] {1, 2, 3, 4, 5})); 
	}
	public static Map<String, Integer> MinMax(int[] arrNum) {
	    int min = arrNum[0];
	    int max = arrNum[0];
	    for (int num : arrNum) {
	        if (min > num) {
	            min = num;
	        } else if (max < num) {
	            max = num;
	        }
	    }
	    Map<String, Integer> result = new HashMap<>();
	    result.put("min", min);
	    result.put("max", max);
	    return result;
	}
}
{min=4, max=781}
{min=1, max=5}
*************************************************************************************
package com.tryPrograms;
public class StringProgs {
	public static void main(String[] args) {
		System.out.println(removeDup("hello")); // helo
		System.out.println(removeDup("apple")); // aple
		System.out.println(removeDup("aaaaaa")); // a
		System.out.println(removeDup("abc")); // abc
	}
	public static String removeDup(String str) {
	    StringBuilder strNoDup = new StringBuilder();
	    for (char ch : str.toCharArray()) {
	    	if (!strNoDup.toString().contains(String.valueOf(ch))) {
	    		strNoDup.append(ch);
	    	}
	    }
	    return strNoDup.toString();
	}
}
helo
aple
a
abc
*************************************************************************************
package com.tryPrograms;
import java.util.LinkedHashSet;
import java.util.Set;
public class StringProgs {
	public static void main(String[] args) {
		System.out.println(removeDup("hello")); // helo
		System.out.println(removeDup("apple")); // aple
		System.out.println(removeDup("aaaaaa")); // a
		System.out.println(removeDup("abc")); // abc
	}
	public static String removeDup(String str) {
	    StringBuilder strNoDup = new StringBuilder();
	    char[] letters = str.toCharArray();
	    Set<Character> set = new LinkedHashSet<>();
	    for (char ch : letters)  set.add(ch);
	    for (Character ch : set) strNoDup.append(ch);
	    return strNoDup.toString();
  }
}
helo
aple
a
abc
*************************************************************************************
package com.tryPrograms;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
public class WordCountFile {
	public static void main(String[] args) {
		System.out.println("Enter string to reverse : ");
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		int len = s.length();
		String rev = "";
		for (int i=len-1; i>=0; i--) {
			rev = rev + s.charAt(i);
		}
		System.out.println("Reverse string without inbuilt method: " +rev);
		StringBuffer sf = new StringBuffer(s);
		System.out.println("Reverse string with inbuilt method: " +sf.reverse());
	}

}
Enter string to reverse : 
This is Java Program
Reverse string without inbuilt method: margorP avaJ si sihT
Reverse string with inbuilt method: margorP avaJ si sihT
*************************************************************************************

*************************************************************************************
