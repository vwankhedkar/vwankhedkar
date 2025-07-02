package com.tryPrograms;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
public class Try1 {
    public static void main(String[] args) {
        BufferedReader reader = null;
        int charCount = 0, wordCount = 0, lineCount = 0;
        try {
            reader = new BufferedReader(new FileReader("C:\\Java-Selenium-Train\\eclipse-workspace"
            		+ "\\JavaProject\\src\\com\\tryPrograms\\Sample.txt")); 
            String currentLine = reader.readLine();

            while (currentLine != null) {
                lineCount++;
                String[] words = currentLine.split("\\s+"); 
                wordCount += words.length;
                for (String word : words) {
                    charCount += word.length();
                }
                currentLine = reader.readLine();
            }
            System.out.println("Number of characters: " + charCount);
            System.out.println("Number of words: " + wordCount);
            System.out.println("Number of lines: " + lineCount);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (reader != null)
                    reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
Number of characters: 417
Number of words: 57
Number of lines: 12
**********************************************************************************
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int a[][] = new int[3][2];
        a[0][0] = 100;
        a[0][1] = 200;
        a[1][0] = 300;
        a[1][1] = 400;
        a[2][0] = 500;
        a[2][1] = 600;
        System.out.println(a.length);
        System.out.println(a[0].length);
        for (int r[] : a) {
        	for (int c : r) {
        		System.out.println(c);
        	}
        }
    }
}
3
2
100
200
300
400
500
600
**********************************************************************************
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
    	 String a = "Hello"; 
    	 String b = "World"; 
    	 System.out.println("before swapping: "); 
    	 System.out.println("the value of a is:" + a); 
    	 System.out.println("the value of b is:" + b); 
    	 // 1. append a and b: 
    	 a = a + b; // HelloWorld     	 
    	 // 2. Store initial string a in String b: 
    	 b = a.substring(0, a.length() - b.length());     	 
    	 // 3. Store initial string b in String a: 
    	 a = a.substring(b.length()); 
    	 System.out.println("the value of a and b after swapping"); 
    	 System.out.println("the value of a is:" + a); 
    	 System.out.println("the value of b is:" + b); 
    }
}
before swapping: 
the value of a is:Hello
the value of b is:World
the value of a and b 
after swapping
the value of a is:World
the value of b is:Hello
**********************************************************************************

**********************************************************************************

**********************************************************************************

**********************************************************************************
**********************************************************************************
  
