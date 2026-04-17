1.)Java program to Find Odd or Even number
Java program to Find Odd or Even numb
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter any number :");
        int number = scanner.nextInt();
        if (number % 2 == 0) {
            System.out.println(number + " is even");
        } else {
            System.out.println(number + " is odd");
        }
    }
}
Enter any number :11
11 is odd
Enter any number :120
120 is even
---------------------------------------------------
2) Java program to find Prime number
import java.util.Scanner
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number : ");
        int number = scanner.nextInt();
        if (isPrime(number)) {
            System.out.println(number + " is a prime number");
        } else {
            System.out.println(number + " is not a prime number");
        }
        scanner.close();
    }
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
---------------------------------------------------
3.) Java program to find Fibonacci series upto a given number range
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of terms : ");
        int num = 6;
        int first=0, second=1, next;
        System.out.print("Fibbonnacci series is : ");
        for (int i=0; i<=num; i++) {
            System.out.print(first +" ");
            next = second + first;
            first = second;
            second = next;
        }
    }
}
Enter number of terms : 
Fibbonnacci series is : 0 1 1 2 3 5 8 
---------------------------------------------------
4.) Java program to swap two numbers without using third variable
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = 5;
        System.out.println("First number :"+a);
        int b = 10;
        System.out.println("Second number :"+b);
        System.out.println("Before swapping:a = "+ a +" b = " +b);
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("After swapping:a = "+ a +" b = " +b);
    }
}
First number :5
Second number :10
Before swapping:a = 5 b = 10
After swapping:a = 10 b = 5
---------------------------------------------------
5.) Java program to Find Factorial on given Number
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        int fact = 1;
        int num = 5;
        for (int i=1; i<=num; i++) {
            fact = fact * i;
        }
        System.out.println("Factorial number "+num+" is : "+fact);
    }
}
---------------------------------------------------
6.) Java program to Reverse Number
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        int no, rev=0, r, a;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter any number : ");
        no = sc.nextInt();
        a = no;
        while (no > 0) {
            r = no % 10;
            rev = rev*10+r;
            no = no/10;
        }
        System.out.print("Reverse of number is : "+rev);
    }
}
Enter any number : 123456789
Reverse of number is : 987654321
---------------------------------------------------
7.) Java program to find Armstrong Numbe
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        int arm=0, a,b,c,d,no;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter any number : ");
        no = sc.nextInt();
        d = no;
        while (no > 0) {
            a = no % 10; no = no / 10; arm = arm+a*a*a;
        }
        if (arm == d) 
            System.out.println("Armstrong number ");
        else
            System.out.println("Not a Armstrong number ");
    }
}
Enter any number : 153
Armstrong number
---------------------------------------------------
8.) Java program to find number of digits in given number
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        int no=0, a=0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter any number : ");
        no = sc.nextInt();
        if (no < 0)
            no = no * -1;
        else if (no == 0)
            no = 1;
        while (no > 0) {
            no = no / 10;
            a++;
        }
            System.out.println("No of digits in given number is: "+a);
    }
}Enter any number : 123456
No of digits in given number is: 6
---------------------------------------------------
9.) Java program to find Palindrome number
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number : ");
        int no = sc.nextInt();
        if (isPalindrome(no)) 
           System.out.print("Number is palindrome ");
        else
           System.out.print("Number is not palindrome ");
    }
public static boolean isPalindrome(int num) {
    int orig_num = num;
    int rev_num = 0;
    while (num != 0) {
        int digit = num % 10;
        rev_num = rev_num * 10 + digit;
        num = num / 10;
    }
    return orig_num == rev_num;
  }
} Enter number : 12321
Number is palindrome 
---------------------------------------------------
10.) Java program to calculate the sum of digits of a number
class Main {
    public static void main(String[] args) {
        int num = 12345;
        int sum = sumOfDigits(num);
        System.out.print("Sum of digits of "+num+" is: "+sum);
    }
public static int sumOfDigits(int num) {
    int sum = 0;
    while (num > 0) {
        int digit = num % 10;
        sum = sum + digit;
        num = num / 10;
    }
    return sum;
  }
}		Sum of digits of 12345 is: 15
---------------------------------------------------
11.) Java program to reverse a string
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String input = sc.nextLine();
        char ch;
        String nstr = "";
        for (int i=0; i<input.length(); i++) {
            ch = input.charAt(i);
            nstr = ch + nstr;
        }
        System.out.print("Reversed string is : "+nstr);
  }
}	Enter a string : Java programming
Reversed string is : gnimmargorp avaJ
---------------------------------------------------
12.) Java program to reverse each word of a given string
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        reverseEachWord("Java is good programming langauges");
  }
static void reverseEachWord(String inputStr)  {
    String[] words = inputStr.split(" ");
    String reverseStr = "";
    for (int i=0; i<words.length; i++) {
       String word = words[i];
       String nstr = "";
       char ch;
       for (int j=0; j<word.length(); j++) {
           ch = word.charAt(j);
           nstr = ch + nstr;
       }
       reverseStr = reverseStr + nstr + " ";
    }
    System.out.println(inputStr);
    System.out.println(reverseStr);
   }
}		Java is good programming langauges
avaJ si doog gnimmargorp seguagnal 
---------------------------------------------------
13.) Java program to find duplicate characters in a string
import java.util.HashMap;
import java.util.Set;
class Main {
    public static void main(String[] args) {
        duplicateCharacterCount("Learn Java Programming");
    }
static void duplicateCharacterCount(String inputStr) {
    HashMap<Character,Integer> charCountMap = new HashMap<>();
    char[] strArray = inputStr.toCharArray(); 
    for (char c : strArray) {
        if (c == ' ') continue;
        if (charCountMap.containsKey(c)) {
            charCountMap.put(c, charCountMap.get(c) + 1);
        } else {
            charCountMap.put(c, 1);
        }
    }
    Set<Character> charsInString = charCountMap.keySet();
    System.out.println("Duplicate characters in : "+inputStr);
    for (Character ch : charsInString) { 
        if (charCountMap.get(ch) > 1)  {
           System.out.println(ch + " : " + charCountMap.get(ch));
        }
     }
   }
}		
Duplicate characters in : Learn Java Programming
a : 4
r : 3
g : 2
m : 2
n : 2
---------------------------------------------------
14.)Java program to count Occurrences of Each Character in String
import java.util.HashMap;
class Main {
    public static void main(String[] args) {
        CharacterCount("Test Automation Java Automation");
    }
    static void CharacterCount(String inputStr) {
        HashMap<Character, Integer> charCountMap = new HashMap<>();
        for (char c : inputStr.toCharArray()) {
            if (c == ' ') continue;
            if (charCountMap.containsKey(c)) {
                charCountMap.put(c, charCountMap.get(c) + 1);
            } else {
                charCountMap.put(c, 1);
            }
        }
        System.out.println("Character count: " + charCountMap);
    }
}	Character count: {A=2, a=4, e=1, i=2, J=1, m=2, n=2, o=4, s=1, T=1, t=5, u=2, v=1}
---------------------------------------------------
15.) Java program to count the number of words in a string
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        System.out.print("Enter the string : ");
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int count = 1;
        for (int i=0; i<s.length()-1; i++) {
            if ((s.charAt(i) == ' ') && (s.charAt(i+1)!=' '))
                count++;
        }
    System.out.println("Number of words in a string : "+count);
    }
}		Enter the string : Welcome to Java World
Number of words in a string : 4
---------------------------------------------------
16.) Java program to find all permutations of a given string
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        String str = "abc";
        permute(str,"");    
}
static void permute(String str, String prefix) {
    if (str.length() == 0) {
        System.out.print(prefix + " ");
    } else {
        for (int i=0; i<str.length(); i++) {
            String rem = str.substring(0,i)+str.substring(i+1);
            permute(rem, prefix+str.charAt(i));
            }
        }
    }
}	
abc acb bac bca cab cba 
---------------------------------------------------
17.) Java program to find if a string is Palindrome
class Main {
    public static void main(String[] args) {
        String str = "madam";
        System.out.println(isPalindrome(str));
    }
static boolean isPalindrome(String str) {
    int start=0;
    int end = str.length()-1;
    while (start < end) {
        if (str.charAt(start) != str.charAt(end))
           return false;
        start++;
        end--;
    }
    return true;
  }
}		===>	true
---------------------------------------------------
18.) Java program to determine if Two Strings are Anagram
class Main {
    public static void main(String[] args) {
        String str1 = "listen";
        String str2 = "silent";
        System.out.println(areAnagrams(str1,str2));
    }
static boolean areAnagrams(String str1, String str2) {
    if (str1.length() != str2.length())
       return false;
    int[] charCount = new int[256];
    for (int i=0; i<str1.length(); i++) {
        charCount[str1.charAt(i)]++;
        charCount[str2.charAt(i)]--;
    }
    for (int count : charCount) {
        if (count != 0) 
            return false;
    }
    return true;
    }
}		===>	true
---------------------------------------------------
19.) Java program to Count Vowels and Consonants in a given string
class Main {
    public static void main(String[] args) {
        String str = "Hello World";
        VowelConsonantCount(str);
    }
static void VowelConsonantCount(String str) {
    int vowels=0, consonants = 0;
    str = str.toLowerCase();
    for (char c:str.toCharArray()) {
        if (c >= 'a' && c <= 'z') {
            if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
               vowels++;
        else
               consonants++;
        }
    }
    System.out.println("Vowels : "+vowels);
    System.out.println("Consonants : "+consonants);
    }
}
---------------------------------------------------
20.) Java program to print unqiue characters
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String : ");
        String input = sc.nextLine();
        System.out.println("Unique characters in \"" + input + "\":");
        printUniqueCharacters(input);
    }
    public static void printUniqueCharacters(String str) {
        boolean[] unique = new boolean[128];
        for (int i=0; i<str.length(); i++) {
            char ch = str.charAt(i);
            if (!unique[ch])   {
                unique[ch] = true;
                System.out.print(ch + " ");
            }
        }
    }
}
---------------------------------------------------
21.) Java program to print even indexed characters
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string : ");
        String input = sc.nextLine();
        System.out.print("Even indexed characters in \"" + input + "\":");
        printEvenIndexedCharacters(input);
    }
    public static void printEvenIndexedCharacters(String str) {
        for (int i=0; i<str.length(); i++) {
            if (i % 2 == 0)
               System.out.print(str.charAt(i));
        }
    }
}
Enter the string : Automation
Even indexed characters in "Automation":Atmto
---------------------------------------------------
22.)Java program to remove space from a given string
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string with spaces: ");
        String input = sc.nextLine();
        String stringWithoutSpaces = removeSpaces(input);
        System.out.println("String without spaces: " + stringWithoutSpaces);
    }
    public static String removeSpaces(String str) {
        StringBuilder result = new StringBuilder();
        for (int i=0; i < str.length(); i++) {
            if (str.charAt(i) != ' ')
               result.append(str.charAt(i));
        }
        return result.toString();
    }
}
Enter a string with spaces: Welcome to Java World
String without spaces: WelcometoJavaWorld
---------------------------------------------------
23.) Java program to print each letter twice from a given string
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String input = sc.nextLine();
        String doubledString = doubleCharacters(input);
        System.out.println("Doubled chars : " +doubledString);
    }
    public static String doubleCharacters(String str)   {
        StringBuilder doubled = new StringBuilder();
        for (int i=0; i<str.length(); i++) {
            char ch = str.charAt(i);
            doubled.append(ch).append(ch);
        }
        return doubled.toString();
    }
}
Enter a string : hello
Doubled chars : hheelllloo
---------------------------------------------------
24.) Java program to swap two string without using 3rd variable
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first string : ");
        String str1 = sc.nextLine();
        System.out.print("Enter second string : ");
        String str2 = sc.nextLine();
        System.out.println("Before swapping: str1 = " + str1 + ", str2 = " + str2);
        str1 = str1 + str2;
        str2 = str1.substring(0, str1.length()-str2.length());
        str1 = str1.substring(str2.length());
        System.out.println("After swapping: str1 = " + str1 + ", str2 = " + str2);
    }
}
Enter first string : Hello
Enter second string : World
Before swapping: str1 = Hello, str2 = World
After swapping: str1 = World, str2 = Hello
---------------------------------------------------
25.)Java program to gives Output: a2b2c3d2 for the Input String Str = “aabbcccdd”
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String input = sc.nextLine();
        String output = getCharacterCount(input);
        System.out.print("Output : " +output);
    }
    public static String getCharacterCount(String str)   {
        StringBuilder result = new StringBuilder();
        int count = 1;
        for (int i=0; i<str.length(); i++)  {
            if (i+1 <str.length() && str.charAt(i)==str.charAt(i+1))  {
                count ++;
        }  else  {
            result.append(str.charAt(i)).append(count);
            count = 1;
        }
    }
    return result.toString();
    }
}
Enter a string : aabbcccdd
Output : a2b2c3d2
---------------------------------------------------
26.) Java program to gives two Output: “abcde” , “ABCDE” for the Input String Str = “aBACbcEDed”
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String input = sc.nextLine();
        System.out.println("Original string is : "+input);
        separateCharacters(input);
    }
    public static void separateCharacters(String input)  {
        StringBuilder lowerCase = new StringBuilder();
        StringBuilder upperCase = new StringBuilder();
        for (char ch : input.toCharArray())  {
            if (Character.isLowerCase(ch))   { lowerCase.append(ch); }
            else { upperCase.append(ch);}
        }
        System.out.println("Output in lowercase : "+lowerCase);
        System.out.println("Output in uppercase : "+upperCase);
    }
}
Enter a string : aBACbcEDed
Original string is : aBACbcEDed
Output in lowercase : abced
Output in uppercase : BACED
---------------------------------------------------
27.) Java program to gives two Output: “Subburaj” , “123” for the Input String Str = “Subbu123raj”
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a String : ");
        String input = sc.nextLine();
        System.out.println("Original String is : "+input);
        separateAplhaAndNumeric(input);
    }
    public static void separateAplhaAndNumeric(String input)   {
        StringBuilder alphaPart = new StringBuilder();
        StringBuilder numericPart = new StringBuilder();
        for (char ch : input.toCharArray())   {
            if (Character.isLetter(ch)) 
               alphaPart.append(ch);
            else if (Character.isDigit(ch))   
               numericPart.append(ch);
        }
        System.out.println("Output in Alpha: "+alphaPart.toString());
        System.out.println("Output in Numeric: "+numericPart.toString());
    }
}
Enter a String : Subbu123raj
Original String is : Subbu123raj
Output in Alpha: Subburaj
Output in Numeric: 123
---------------------------------------------------
28.)Java program to gives Output: “32412120000” for the Input String Str =“32400121200”
class Main {
    public static void main(String[] args) {
        String input = "32400121200";
        String output = rearrangeDigits(input);
        System.out.println("Output: " + output);
    }
    public static String rearrangeDigits(String input)   {
        StringBuilder digits = new StringBuilder();
        StringBuilder nonDigits = new StringBuilder();
        for (char c : input.toCharArray())  {
            if (Character.isDigit(c)) 
               digits.append(c);
            else
               nonDigits.append(c);
        }
        return digits.toString() + nonDigits.toString();
    }
}
Output: 32400121200
---------------------------------------------------
29.) Java program to gives Output: “32412120000” for the Input String Str = “32400121200”
class Main {
    public static void main(String[] args) {
        String input = "32400121200";
        String formattedOutput = String.format("%011d",Long.parseLong(input));
        System.out.println("Formatted output : "+formattedOutput);
    }
}
Formatted output : 32400121200
---------------------------------------------------
30.) Java program to find the longest without repeating characters
import java.util.HashSet;
class Main {
    public static void main(String[] args) {
        String s1 = "abcabcbb"; // Expected: "abc", length 3
        String s2 = "bbbbb";
        String s3 = "pwwkew";
        String s4 = "";
        System.out.println("Longest substring without repeating characters in s1 :"  +lengthOfLongestSubstring(s1));
        System.out.println("Longest substring without repeating characters in s2 :"  +lengthOfLongestSubstring(s2));
        System.out.println("Longest substring without repeating characters in s3 :"  +lengthOfLongestSubstring(s3));
        System.out.println("Longest substring without repeating characters in s4 :"  +lengthOfLongestSubstring(s4));
    }
    public static int lengthOfLongestSubstring(String s)   {
        HashSet<Character> set = new HashSet<>();
        int maxLength = 0;
        int start = 0;
        int end = 0;
        while (end < s.length())  {
            char currentChar = s.charAt(end);
            if (!set.contains(currentChar))  {
                set.add(currentChar);
                maxLength = Math.max(maxLength, end-start+1);
                end++;
            }
            else {
                set.remove(s.charAt(start));
                start++;
            }
        }
        return maxLength;
    }
}
Longest substring without repeating characters in s1 :3
Longest substring without repeating characters in s2 :1
Longest substring without repeating characters in s3 :3
Longest substring without repeating characters in s4 :0
---------------------------------------------------
			Arrays
---------------------------------------------------
31.) Find common elements between two arrays
import java.util.HashSet;
import java.util.Set;
class Main {
    public static void main(String[] args) {
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {4, 5, 6, 7, 8};
        Set<Integer> commonElements = findCommonElements(array1, array2);
        System.out.println("Common Elements : "+commonElements);
    }
    public static Set<Integer> findCommonElements(int[] array1, int[] array2)  {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> commonSet = new HashSet<>();
        for (int num : array1) 
            set1.add(num);
        for (int num : array2) 
            if (set1.contains(num)) {
                commonSet.add(num);
            }
        return commonSet;
    }
}
Common Elements : [4, 5]
---------------------------------------------------
32.) Find first and last element of Arraylist
import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("Apple");
        arrayList.add("Banana");
        arrayList.add("Cherry");
        arrayList.add("Date");
        arrayList.add("Elderberry");
        if (!arrayList.isEmpty())    {
            String firstElement = arrayList.get(0);
            String lastElement = arrayList.get(arrayList.size()-1);
            System.out.println("First element : "+firstElement);
            System.out.print("Last element : "+lastElement);
        }   else {
            System.out.print("The arraylist is empty");
        }
    }
}
First element : Apple
Last element : Elderberry
---------------------------------------------------
33.) Sort an array without using in-built method
import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
        int[] array = {5, 2, 9, 1, 6};
        selectionSort(array);
        System.out.print("Sorted array : ");
        for (int num : array)  {
            System.out.print(num + " ");
        }
    }
    public static void selectionSort(int[] array)   {
        int n = array.length;
        for (int i=0; i<n-1; i++)  {
            int minIndex = i;
            for (int j=i+1; j<n; j++)  {
                if (array[j] < array[minIndex]) {
                   minIndex = j;
            }
        }
        int temp = array[i];
        array[i] = array[minIndex];
        array[minIndex] = temp;
        }
    }
}
Sorted array : 1 2 5 6 9 
---------------------------------------------------
34.) Remove duplicates from an Array
import java.util.HashSet;
import java.util.Set;
class Main {
    public static void main(String[] args) {
        int[] array = {5, 2, 9, 1, 6, 2, 5};
        int[] uniqueArray = removeDuplicates(array);
        System.out.println("Array with duplicates removed : ");
        for (int num : uniqueArray)  {
            System.out.print(num + " ");
        }
    }
    public static int[] removeDuplicates(int[] array)  {
        Set<Integer> set = new HashSet<>();
        for (int num : array)  {
            set.add(num);
        }
        int[] result = new int[set.size()];
        int i=0;
        for (int num : set) {
            result[i++] = num;
        }
        return result;
    }
}
Array with duplicates removed : 
1 2 5 6 9 
---------------------------------------------------
35.) Remove duplicates from an ArrayList
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Set;
class Main {
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
        System.out.println("ArrayList with duplicates removed");
        for (int num : uniqueList) {
            System.out.print(num + " ");
        }
    }
    public static ArrayList<Integer> removeDuplicates(ArrayList<Integer> list)  {
        Set<Integer> set = new HashSet<>(list);
        return new ArrayList<>(set);
    }
}
ArrayList with duplicates removed
1 2 5 6 9 
---------------------------------------------------
36.) Find the missing number in an Array
class Main {
    public static void main(String[] args) {
        int[] array = {1, 2, 4, 5, 6};
        int missingNumber = findMissingNumber(array);
        System.out.print("The missing number is : "+missingNumber);
    }
    public static int findMissingNumber(int[] array)  {
        int n = array.length+1;
        int totalSum = n * (n + 1) / 2;
        int arraySum = 0;
        for (int num : array)  {
            arraySum += num ;
        }
        return totalSum - arraySum;
    }
}
The missing number is : 3
---------------------------------------------------
37.) Find the largest and smallest element in an Array
class Main {
    public static void main(String[] args) {
        int[] array = {5, 2, 9, 1, 6, 3};
        int[] result = findLargestAndSmallest(array);
        System.out.println("Smallest Element : "+result[0]);
        System.out.println("Largest Element : "+result[1]);
    }
    public static int[] findLargestAndSmallest(int[] array)  {
        if (array == null || array.length==0)  {
            throw new IllegalArgumentException("Array must not be null or empty");
        }
        int smallest = array[0];
        int largest = array[0];
        for (int num : array)  {
            if (num < smallest)  {
                smallest = num;
            }
            if (num > largest)  {
                largest = num;
            }
        }
        return new int[] {smallest, largest};
    }
}
Smallest Element : 1
Largest Element : 9
---------------------------------------------------
38.) Search element in an Array
class Main {
    public static void main(String[] args) {
        int[] array = {5, 2, 9, 1, 6, 3};
        int target = 6;
        int index = linearSearch(array, target);
        if (index >= 1) 
            System.out.println("Element "+target+" found at index: "+index);
        else 
            System.out.println("Element "+target+" not found in the array.");
    }
    public static int linearSearch(int[] array, int target)  {
        for (int i=0; i<array.length; i++)  {
            if (array[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
Element 6 found at index: 4
Element 56 not found in the array.
---------------------------------------------------
39.) Array consists of integers and special characters,sum only integers
class Main {
    public static void main(String[] args) {
        String[] array = {"5", "2", "9", "a", "1", "6", "#", "3"};
        int sum = sumIntegers(array);
        System.out.println("Sum of integers in the array : "+sum);
    }
    public static int sumIntegers(String[] array)  {
        int sum = 0;
        for (String element : array)  {
            try  {
                int num = Integer.parseInt(element);
                sum += num;
            } catch (NumberFormatException e)  { }
        }
        return sum;
    }
}    Sum of integers in the array : 26
---------------------------------------------------
40.) Find Minimum and Maximum from an Array
class Main {
    public static void main(String[] args) {
        int[] array = {5, 2, 9, 1, 6, 3};
        int max =  findMaximum(array);
        int min =  findMinimum(array);
        System.out.println("Minimum value in the array : "+min);
        System.out.println("Maximum value in the array : "+max);
    }
    public static int findMaximum(int[] array)  {
        if (array.length == 0)  {
            throw new IllegalArgumentException("Array must not be empty");
        }
        int max = array[0];
        for (int i=1; i<array.length; i++)  {
            if (array[i] > max) {
               max = array[i];
            }
        }
        return max;
    }
    public static int findMinimum(int[] array)  {
        if (array.length == 0)  {
            throw new IllegalArgumentException("Array must not be empty");
        }
        int min = array[0];
        for (int i=1; i<array.length; i++)  {
            if (array[i] < min) {
                min = array[i];
            }
        }
        return min;
    }
}
Minimum value in the array : 1
Maximum value in the array : 9
---------------------------------------------------
41.) Java program to count Odd and Even number from given array  Input: {1,2,3,4,5,6,7,8,9}
class Main {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] count = countOddandEven(array);
        System.out.println("Even numbers count : "+count[1]);
        System.out.println("Odd numbers count : "+count[0]);
    }
    public static int[] countOddandEven(int[] array)  {
        int[] count = new int[2];
        for (int num : array)  {
            if (num % 2 == 0)
                count[1]++;
            else
                count[0]++;
        }
        return count;
    }
}
Even numbers count : 4
Odd numbers count : 5
---------------------------------------------------
42.) Java program – input array was given [ 1,1,2,2,3,4,5,5,6,6], Output – [3,4]
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
class Main {
    public static void main(String[] args) {
        int[] array = {1, 1, 2, 2, 3, 4, 5, 5, 6, 6};
        List<Integer> result = findNonRepeatedElements(array);
        System.out.println("Non-repeated elements : "+result);
    }
    public static List<Integer> findNonRepeatedElements(int[] array)  {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : array)  {
            countMap.put(num, countMap.getOrDefault(num,0)+1);
        }
        List<Integer> nonRepeatedElements = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet())  {
            if (entry.getValue() == 1)  {
                nonRepeatedElements.add(entry.getKey());
            }
        }
        return nonRepeatedElements;
    }
}
Non-repeated elements : [3, 4]
---------------------------------------------------
43.) Java program to implement hashcode and equals
import java.util.Objects;
public class Student {
    private int id;
    private String name;
    public Student(int id, String name)  {
        this.id = id;
        this.name = name;
    }
    @Override
    public int hashCode()  {
        return Objects.hash(id, name);
    }
    @Override
    public boolean equals(Object obj)  {
        if (this == obj)
           return true;
        if (obj == null || getClass()!=obj.getClass()) 
           return false;
        Student student = (Student) obj;
        return id == student.id && Objects.equals(name,student.name);
    }
    public static void main(String[] args) {
        Student student1 = new Student(1, "Alice");
        Student student2 = new Student(2, "Bob");
        Student student3 = new Student(1, "Alice");
        System.out.println("student1.equals(student2)" +student1.equals(student2));
        System.out.println("student1.equals(student3)" +student1.equals(student3));
        System.out.println("Hashcode of student1 : " +student1.hashCode());
        System.out.println("Hashcode of student2 : " +student2.hashCode());
        System.out.println("Hashcode of student3 : " +student3.hashCode());
    }
}
student1.equals(student2)false
student1.equals(student3)true
Hashcode of student1 : 63351360
Hashcode of student2 : 67988
Hashcode of student3 : 63351360
---------------------------------------------------
