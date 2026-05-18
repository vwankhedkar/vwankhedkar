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
12) Java program to reverse each word of a given string
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
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------------------------------
// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class Main {
    public static void main(String[] args) {
        String str="2a3b1c";
        System.out.println("Given string: "+str);
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<str.length()-1;i+=2){
            char c= str.charAt(i);
            char lett= str.charAt(i+1);
            int count = Character.getNumericValue(c);
            
            for(int j=0;j<count;j++)
            sb.append(lett);
        }
        System.out.println("Expanded string: "+sb.toString());
    }
}
public class AmazonHomePage {
    
    private WebDriver driver;
    public AmazonHomepage(WebDriver driver){
        this.driver=driver;
    }
    public void clickSignIn(){
        driver.findElement(By.id("nav-link-accountList")).click();
    }
}
public class AmazonSignInpage{
        private WebDriver driver;
    public AmazonSignInpage(WebDriver driver){
        this.driver=driver;
    }
    public void enterMobileOrEmail(String input){
        driver.findElement(By.id("ap-email-login")).sendKeys(input);
    }
    public void clickonContinue(){
        driver.findElement(By.xpath("/span[@id='continue']")).click();
    }
    
}
@TestMethodOrder(Methodorderer.OrderAnnotation.class)
public class AmazonSignInTest{
    
    private static WebDriver driver;
    private static final string Amazon_URL="https://www.amazon.com";
    
    @BeforeAll
    public static void setUp(){
        driver = new ChromerDriver();
        driver.manage().window().maximize();
    }
    @AfterAll
    public static void tearDown(){
        if(driver!=null)
        driver.quit();
        
    }
    
    @Test @Order(1)
    public void testNavigateAndSignIn(){
driver.get(Amazon_URL);    
AmazonHomePage homepage = new AmazonHomePage(driver);
homepage.clickSignIn();
AmazonSignInpage signinpage = new AmazonSignInpage(driver);
signinpage.enterMobileOrEmail("9861249381");
signinpage.clickContinue();
Assertions.asserttTrue(driver.getCurrentUrl().contains("Signin"),"should be on signinflow - FAILED");
}
}
---------------------------------------------------
*************************************************************************
EPAM : Java
class Main {
    
    public static void findOccurence(){
        String input[] = {"apple", "apple", "banana", "apple", "orange", "banana", "papaya"};
        
        HashMap<String, Integer> hashmap = new HashMap<>();
        
        for(String s: input){
            if(!hashmap.containsKey(s)){
                hashmap.put(s, 1);
            }else
            {
                hashmap.put(s, hashmap.get(s)+1);
            }
        }
        
        for(String s1 : hashmap.keySet()){
            if(hashmap.get(s1) >1){
                System.out.println(" " +s1+""+ hashmap.get(s1));
            }
        }
    }
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        findOccurence();
    }
}
------------------------------------------------------------
import java.util.HashMap;
class Main {
    public static void main(String[] args) {
        String[] List = {"apple", "apple", "banana", "apple", "orange", "banana", "papaya"};
        HashMap<String, Integer> fruits = new HashMap<String, Integer>();
        for (String word : List) {
            if (fruits.containsKey(word)) {
                int x = fruits.get(word);
                fruits.put(word, x+1);
            }
            else
                fruits.put(word, 1);
        }
        System.out.println(fruits);
        for (String s : fruits.keySet()) {
            if (fruits.get(s) > 1)
               System.out.println(s +": "+ fruits.get(s));
        }
    }
}
{banana=2, orange=1, papaya=1, apple=3}
banana: 2
apple: 3

---------------------------------------------------
************************************************************************************
Java
write a code to print the distinct numbers = {-5, -3, 0, 3, 2, 1, 0, -3, 0, 5}; 
import java.util.HashSet;
import java.util.Set;
 
public class Distinct {
    public static void main(String[] args) {
        int[] numbers = {-5, -3, 0, 3, 2, 1, 0, -3, 0, 5}; 
        Set<Integer> distinctNumbers = new HashSet<>();   
        for (int num : numbers) {
            distinctNumbers.add(num);
        }
 
        for (Integer num : distinctNumbers) {
            System.out.println(num);   
        }
    }
}
************************************************************************************
class Main {
    public static void findBrokenLinks(){
         WebdriverManager().chromedriver().setup();
         Webdriver driver = new ChromeDriver();
         driver.get("https://www.naukri.in");
         
         List<WebElement> list = driver.findElements(By.tagName("a"));
         
         for(WebElement e: list){
             String s = e.getAttribute("href");
             URL url = new URL(s);
             URLHttpConnection urlHttpConnection = (URLHttpConnection) url.openConnection();
                urlHttpConnection.setTimeOut(5000);
                urlHttpConnection.connect();               
                if( urlHttpConnection.getStatusCode() == 500){
                     urlHttpConnection.getResponseMessage();
                     System.out.println("Broken Link "+ urlHttpConnection.getResponseMessage() );
                }
         }
    }
public static void main(String[] args) {
        System.out.println("Try programiz.pro");
      findBrokenLinks
    }
}

Response reponse = Restassured.given()
                        .when()
                        .get("Naukri.in")
                        .then()
                        .statusCode(200);
                        
    int status = response.jsonPath().get(statusCode);
    
    Assert.assertEquals(status, 200);
	
	
	
package com.PractiseProgs;
import org.openqa.selenium.By;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
public class openHTML { 
	public static void main(String[] args) throws InterruptedException 
	{ 
		WebDriver driver=new FirefoxDriver(); 
		driver.get("https://www.amazon.in/"); 
		RemoteWebDriver r= (RemoteWebDriver) driver; 
		WebElement ele = driver.findElement(By.linkText("Your Amazon.in"));
		System.out.println(ele);
		Point p = ele.getLocation();
		int y = p.getY();
		String s = "window.scrollTo(0,"+y+")";
		Thread.sleep(3000);
		//String c="window.scrollTo(0,document.body.scrollHeight)"; 
		r.executeScript(s);  
		driver.quit();
	}
} 

---------------------------------------------------
*************************************************************************
Interview AT&T
https://reqres.in/

package com.api;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.Test;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;

import java.util.HashMap;
import java.util.Map;

public class PostAPITest {

    @Test
    public void testCreateUser() {
        // Set base URI
        RestAssured.baseURI = "https://reqres.in/api";

        // Request payload
        Map<String, String> requestBody = new HashMap<>();
        requestBody.put("name", "morpheus");
        requestBody.put("job", "leader");

        // Send POST request
        Response response = RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(requestBody)
                .when()
                .post("/users")
                .then()
                .statusCode(201)
                .extract().response();

        // Assertions
        String name = response.jsonPath().getString("name");
        String job = response.jsonPath().getString("job");
        String id = response.jsonPath().getString("id");
        String createdAt = response.jsonPath().getString("createdAt");

        assertEquals(name, "morpheus");
        assertEquals(job, "leader");
        assertNotNull(id);
        assertNotNull(createdAt);

        System.out.println("User created with ID: " + id);
    }
}

Mavan pom.xml

<dependencies>
    <dependency>
        <groupId>io.rest-assured</groupId>
        <artifactId>rest-assured</artifactId>
        <version>5.3.1</version>
    </dependency>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.7.1</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>2.15.3</version>
    </dependency>
</dependencies>

*************************************************************************
  write a code to print the distinct numbers = {-5, -3, 0, 3, 2, 1, 0, -3, 0, 5}; 
import java.util.HashSet;
import java.util.Set;
 
public class Distinct {
    public static void main(String[] args) {
        int[] numbers = {-5, -3, 0, 3, 2, 1, 0, -3, 0, 5}; 
        Set<Integer> distinctNumbers = new HashSet<>();   
        for (int num : numbers) {
            distinctNumbers.add(num);
        }
 
        for (Integer num : distinctNumbers) {
            System.out.println(num);   
        }
    }
}
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
		Python
---------------------------------------------------
with open('file.txt','r') as file:
    for line in file:
        print(line.strip())

---------------------------------------------------
with open('file.txt','w') as file:
    file.write("Hello")
with open('file.txt','r') as file:
    print(file.read())
---------------------------------------------------
import re
text = "I love learning Python!"
match = re.search(r"Python", text)
if match:
    print(match.group())
----------------
import re
text = "I love Python learning Python!"
match = re.search(r"Python", text)
if match:
    print(match)
---------------------------------------------------
import re
text = "My favorite number is 42."
match = re.search(r"\d+",text)
if match:
    print("Found Number : ", match.group())
Found Number :  42
---------------------------------------------------
import re
email = "user@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if (re.match(pattern,email)):
    print("Valid mail !")
else:
    print("Invalid mail !")
Valid mail !
---------------------------------------------------
import re
text = "The event is on 15/08/2025."
date = re.search(r"\d{2}/\d{2}/\d{4}", text)
if date:
    print("Found date : ", date.group())
Found date :  15/08/2025
---------------------------------------------------
import re
phone_number = "(123) 456-7890"
pattern = r"\(\d{3}\) \d{3}-\d{4}"
if re.match(pattern, phone_number):
    print("Valid phone number !")
else:
    print("Invalid phone number!")
Valid phone number !
---------------------------------------------------
import re
text = "Hello World!"
modified_text = re.sub(r"\s","_",text)
print(modified_text)
Hello_World!
---------------------------------------------------
import re
text = "Visit our website at https://www.example.com for more info."
url = re.search(r"https?://[a-zA-Z0-9./]+",text)
if url:
    print("Found URL...", url.group())
Found URL... https://www.example.com
---------------------------------------------------
import re
text = "apple, banana, cherry"
fruits = re.split(r",\s*",text)
print(fruits)
['apple', 'banana', 'cherry']
---------------------------------------------------
import re
text = "I have 3 apples, 7 bananas, and 12 cherries."
numbers = re.findall(r"\d+",text)
print("Numbers found !", numbers)
Numbers found ! ['3', '7', '12']
---------------------------------------------------
import re
text = "Alice and Alex are amazing artists."
words = re.findall(r"\b[Aa]\w+",text)
print("Words found - ",words)
Words found -  ['Alice', 'and', 'Alex', 'are', 'amazing', 'artists']
---------------------------------------------------
import re
password = "Secure@123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
if re.match(pattern, password):
    print("Strong password!")
else:
    print("Weak password!Try adding uppercase, lowercase, numbers, and special characters.")
Strong password!
---------------------------------------------------
import re
text = "Python is fun! Let's learn regex together."
words = re.findall(r"\b\w+\b",text)
print("Words : ", words)
Words :  ['Python', 'is', 'fun', 'Let', 's', 'learn', 'regex', 'together']
---------------------------------------------------
import re
tweet = "Learning #Python and #Regex is fun! #Coding"
hashtags = re.findall(r"#\w+",tweet)
print("Hashtags found - ", hashtags)
Hashtags found -  ['#Python', '#Regex', '#Coding']
---------------------------------------------------
import re
text = "Alice and Bob are learning Python in New York."
capitalized_words = re.findall(r"\b[A-Z][a-z]*\b",text)
print("capitalized Words : ", capitalized_words)
capitalized Words :  ['Alice', 'Bob', 'Python', 'New', 'York']
---------------------------------------------------
import re
text = "Python is awesome!"
cleaned_text = re.sub(r"\s+"," ",text)
print(cleaned_text)
Python is awesome!
---------------------------------------------------
import re
text = "I have 3 apples, 10 bananas, and 25 oranges."
numbers = re.findall(r"\d+",text)
print("Numbers found : ",numbers)
Numbers found :  ['3', '10', '25']
---------------------------------------------------
import re
text = "The tiger and the turtle are in the zoo."
words = re.findall(r"\b[Tt]\w+",text)
print("Words found : ", words)
Words found :  ['The', 'tiger', 'the', 'turtle', 'the']
---------------------------------------------------
import re
text = "Python123"
if re.fullmatch(r"[A-Za-z0-9]+",text):
    print("Valid input (letters and numbers only)")
else:
    print("Invalid input")
Valid input (letters and numbers only)
---------------------------------------------------
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof!")
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
Buddy says Woof!
---------------------------------------------------
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
dog = Dog()
dog.speak()
Dog barks
---------------------------------------------------
class Car:
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed
    def accelerate(self,increment):
        if increment > 0:
            self.__speed+=increment
    def brake(self, decrement):
        if decrement > 0 and self.__speed - decrement > 0:
            self.__speed -= decrement
    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return self.__brand
---------------------------------------------------
class Car:
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed
    def accelerate(self,increment):
        if increment > 0:
            self.__speed+=increment
    def brake(self, decrement):
        if decrement > 0 and self.__speed - decrement > 0:
            self.__speed -= decrement
    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return self.__brand
my_car = Car("Toyota",50)
print(my_car.get_speed())
my_car.accelerate(30)
print(my_car.get_speed())
my_car.brake(20)
print(my_car.get_speed())
50
80
60
---------------------------------------------------
class Cat:
    def speak(self):
        print("Meow")
class Dog:
    def speak(self):
        print("Woof")
animals = [Cat(), Dog()]
for animal in animals:
    animal.speak()
Meow
Woof
---------------------------------------------------
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Woof")
dog = Dog()
dog.speak()
Woof
---------------------------------------------------
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@decorator
def say_hello():
    print("Hello")
say_hello()
Before function call
Hello
After function call
---------------------------------------------------
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(3)
for num in counter:
    print(num)
1
2
3
---------------------------------------------------
numbers = [1, 2, 3, 4, 5]
sq = [x**2 for x in numbers]
print(sq)
[1, 4, 9, 16, 25]
---------------------------------------------------
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
age_dict = {name:age for name, age in zip(names, ages)}
print(age_dict)
{'Alice': 25, 'Bob': 30, 'Charlie': 35}
---------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index} : {fruit}")
0 : apple
1 : banana
2 : cherry
---------------------------------------------------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
combine = zip(names,scores)
print(list(combine))
[('Alice', 85), ('Bob', 90), ('Charlie', 95)]
---------------------------------------------------
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))	==>		1
---------------------------------------------------
import threading
def print_num():
    for i in range(5):
        print(i)
thread1 = threading.Thread(target=print_num)
thread2 = threading.Thread(target=print_num)
thread1.start()
thread2.start()
0
1
2
3
4
0
1
2
3
4
---------------------------------------------------
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
Hello, Alice!
Hello, Alice!
Hello, Alice!
---------------------------------------------------
import json
person = {"name":"Alice", "age":25}
json_data = json.dumps(person)
print(json_data)
{"name": "Alice", "age": 25}
---------------------------------------------------
import json
json_string = '{"name":"Alice", "age":25}'
person = json.loads(json_string)
print(person)
{'name': 'Alice', 'age': 25}
---------------------------------------------------
import csv
data = [["name", "age"], ["Alice", 25], ["Bob", 30]]
with open('output.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
with open('output.csv','r') as file:
    header = csv.reader(file)
    for row in header:
        print(row)
['name', 'age']
['Alice', '25']
['Bob', '30']
---------------------------------------------------
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
print()
print(df["name"])
print()
print(df[df["age"]>=30])
      name  age
0    Alice   25
1      Bob   30
2  Charlie   35

0      Alice
1        Bob
2    Charlie
Name: name, dtype: object

      name  age
1      Bob   30
2  Charlie   35
---------------------------------------------------
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
200
---------------------------------------------------
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
data = {"name":"Alice","age":25}
response = requests.post("https://api.example.com", json=data)
print(response.status_code)
200
{'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}', 'notifications_url': 'https://api.github.com/notifications', 'organization_url': 'https://api.github.com/orgs/{org}', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_teams_url': 'https://api.github.com/orgs/{org}/teams', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'topic_search_url': 'https://api.github.com/search/topics?q={query}{&page,per_page}', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}
201
---------------------------------------------------
import requests
from bs4 import BeautifulSoup
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
https://iana.org/domains/example
---------------------------------------------------
from multiprocessing import Process
def print_num():
    for i in range(5):
        print(i)
process = Process(target = print_num)
process.start()
process.join()
0
1
2
3
4
---------------------------------------------------
import asyncio
async def greet():
    await asyncio.sleep(1)
    print("Hello, Async!")
asyncio.run(greet())
Hello, Async!
---------------------------------------------------
class CustomError(Exception):
    pass
try:
    raise CustomError("A Custom error occured")
except CustomError as e:
    print(e)
A Custom error occured
---------------------------------------------------
import yaml
data = {"name":"Alice", "age":25}
yaml_str = yaml.dump(data)
print(yaml_str)
age: 25
name: Alice
---------------------------------------------------
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
print(config["DEFAULT"][Setting])
---------------------------------------------------
import calendar
year = int(input("Enter year : "))
month = int(input("Enter month : "))
cal = calendar.month(year, month)
print(cal)
Enter year : 2026
Enter month : 4
     April 2026
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30
---------------------------------------------------
year = int(input("Enter a year : "))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year")
Enter a year : 2024
2024 is a leap year
---------------------------------------------------
num = int(input("Enter a number : "))
flag = False
if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
    for i in range (2, num):
        if (num % i == 0):
            flag = True
            break
if flag:
    print(f"{num}, is not prime number")
else:
    print(f"{num}, is prime number")
Enter a number : 11
11, is prime number
---------------------------------------------------
lower = int(input("Enter lower number : "))
upper = int(input("Enter upper number : "))
print("Prime numbers between {lower} and {upper} are : ")
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num, end = " ")
Enter lower number : 1
Enter upper number : 10
Prime numbers between {lower} and {upper} are : 
2 3 5 7 
---------------------------------------------------
num = int(input("Enter a number : "))
fact = 1
if num < 0:
    print("Factirial does not exist for negative numbers")
elif num == 0:
    print("Factirial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact * i
    print(f"Factirial of number {num} is {fact}")
Enter a number : 4
Factirial of number 4 is 24
---------------------------------------------------
nterms = int(input("How many terms? : "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Enter positive integer...")
elif nterms == 1:
    print("Fibbonacci series upto ",nterms," : ")
    print(n1, end = " ")
else:
    print("Fibbonacci series : ")
    while count < nterms:
        print(n1, end = " ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
How many terms? : 10
Fibbonacci series : 
0 1 1 2 3 5 8 13 21 34 
---------------------------------------------------
num = int(input("Enter a number : "))
num_str = str(num)
num_digits = len(num_str)
sum_of_power = 0
temp_num = num
while (temp_num > 0):
    digit = temp_num % 10
    sum_of_power += digit ** num_digits
    temp_num //= 10
if sum_of_power == num:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
Enter a number : 153
153 is Armstrong number
---------------------------------------------------
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))
for num in range(lower, upper+1):
    order = len(str(num))
    temp_num = num
    sum = 0
    while (temp_num > 0):
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
    if num == sum:
        print(num)
Enter the lower limit of the interval: 10
Enter the upper limit of the interval: 10000
153
370
371
407
1634
8208
9474
---------------------------------------------------
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The L.C.M. is", compute_lcm(num1, num2))
Enter the number: 54
Enter the number: 24
The L.C.M. is 216
---------------------------------------------------
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The H.C.F. is", compute_hcf(num1, num2))
Enter the number: 54
Enter the number: 24
The H.C.F. is 6
---------------------------------------------------
dec_num = int(input('Enter a decimal number: '))
print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")
Enter a decimal number: 27
The decimal value of 27 is:
0b11011 in binary.
0o33 in octal.
0x1b in hexadecimal.
---------------------------------------------------
char = str(input("Enter the character : "))
print("The ASCII value of {char} is : ", ord(char))
Enter the character : V
The ASCII value of {char} is :  86
---------------------------------------------------
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select opearation : ")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")
while True:
    choice = input("Enter choice(1/2/3/4) : ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, please enter number.")
            continue
        if choice == '1':
            print(num1,"+",num2,'=',add(num1, num2))
        elif choice == '2':
            print(num1,"-",num2,'=',sub(num1, num2))
        if choice == '3':
            print(num1,"*",num2,'=',multiply(num1, num2))
        if choice == '4':
            print(num1,"/",num2,'=',divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/No) : ")    
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
Select opearation : 
1. Add 
2. Subtract 
3. Multiply 
4. Divide 
Enter choice(1/2/3/4) : 1
Enter first number: 3
Enter second number: 4
3.0 + 4.0 = 7.0
Let's do next calculation? (yes/No) : yes
Enter choice(1/2/3/4) : 2
Enter first number: 6
Enter second number: 1
6.0 - 1.0 = 5.0
Let's do next calculation? (yes/No) : yes
Enter choice(1/2/3/4) : 3
Enter first number: 6
Enter second number: 2
6.0 * 2.0 = 12.0
Let's do next calculation? (yes/No) : yes
Enter choice(1/2/3/4) : 90
Enter first number: 90
Enter second number: 3
90.0 / 3.0 = 30.0
Let's do next calculation? (yes/No) : no
---------------------------------------------------
def recur_fibbo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibbo(n-1) + recur_fibbo(n-2))
nterms = int(input("Enter number of the terms greater than 0 : "))
if nterms <= 0:
    print("Please enter positive integer ")
else:
    print("Fibbonacci sequence : ")
    for i in range(nterms):
        print(recur_fibbo(i), end=" ")
Enter number of the terms greater than 0 : 8
Fibbonacci sequence : 
0 1 1 2 3 5 8 13 
---------------------------------------------------
def recur_facto(n):
    if n == 1:
        return n
    else:
        return n * recur_facto(n-1)
num = int(input("Enter the number : "))
if num < 0:
    print("Please enter positive integer factorial is not for negative num")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    print(f"The Factorial is : ", recur_facto(num))
Enter the number : 7
The Factorial is :  5040
---------------------------------------------------
class Solution(object):
    def rotated_arr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        rotated_arr = [0] * n
        for i in range(n):
            rotated_arr[(i + k) % n] = nums[i]
        nums[:] = rotated_arr
        return nums
arr = [1, 2, 3, 4, 5]
d = 2
s = Solution()
print("Original array : ", arr)
result = s.rotated_arr(arr, d)
print("Rotated array : ", result)
----------------------------
n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
Original array :  [1, 2, 3, 4, 5]
Rotated array :  [4, 5, 1, 2, 3]
---------------------------------------------------
def split_and_arr(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    first_part = arr[:k]
    second_part = arr[k:]
    result = second_part + first_part
    return result
arr = [1, 2, 3, 4, 5]
k = 3
result = split_and_arr(arr, k)
print("Original array : ", arr)
print("Array after splitting and adding : ", result)
Original array :  [1, 2, 3, 4, 5]
Array after splitting and adding :  [4, 5, 1, 2, 3]
---------------------------------------------------
A monotonic array is one that is entirely non-increasing or non-decreasing
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if (arr[i] > arr[i-1]):
            decreasing = False
        elif (arr[i] < arr[i-1]):
            increasing = False
    return increasing or decreasing
arr1 = [1, 2, 2, 3]
arr2 = [3, 2, 1]
arr3 = [1, 3, 2, 4]
print("arr1 is monotonic:", is_monotonic(arr1))
print("arr2 is monotonic:", is_monotonic(arr2))
print("arr3 is monotonic:", is_monotonic(arr3))
arr1 is monotonic: True
arr2 is monotonic: True
arr3 is monotonic: False
---------------------------------------------------
def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
matrix1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
matrix2 = [
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]
result_matrix = add_matrices(matrix1, matrix2)
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Sum of matrices:")
    for row in result_matrix:
        print(row)
Sum of matrices:
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
---------------------------------------------------
def multiply_matrices(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
    if cols1 != rows2:
        return "Matrix multiplication is not possible. Number of columns mismatch"
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
matrix1 = [
 [1, 2, 3],
 [4, 5, 6]
]
matrix2 = [
 [7, 8],
 [9, 10],
 [11, 12]
]
result_matrix = multiply_matrices(matrix1, matrix2)
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result of matrics multiplication :")
    for row in result_matrix:
        print(row)
Result of matrics multiplication :
[58, 64]
[139, 154]
---------------------------------------------------
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
matrix = [
 [1, 2, 3],
 [4, 5, 6]
]
transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)
[1, 4]
[2, 5]
[3, 6]
---------------------------------------------------
my_str = input("Enter a string : ")
words = [word.capitalize() for word in my_str.split()]
words.sort()
print("The sorted words are : ")
for word in words:
    print(word)
Enter a string : vaishali mangulal wankhedkar sandip vishal shiv shambhu chiku
The sorted words are : 
Chiku
Mangulal
Sandip
Shambhu
Shiv
Vaishali
Vishal
Wankhedkar
---------------------------------------------------
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string : ")
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)
/home/main.py:1: SyntaxWarning: invalid escape sequence '\,'
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
Enter a string : Hello!!!, he said ---and went
Hello he said and went
---------------------------------------------------
A Disarium number is a number that is equal to the sum of its digits each raised to the
power of its respective position. For example, 89 is a Disarium number because 8 + = 8 + 81 = 89.
def is_disarium(number):
    num_str = str(number)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return digit_sum == number
try:
    num = int(input("Enter a number : "))
    if is_disarium(num):
        print(f"{num} is a Disarium number")
    else:
        print(f"{num} is not a Disarium number")
except ValueError:
    print("Invalid input. Please enter a valid number")
Enter a number : 89
89 is a Disarium number
---------------------------------------------------
def is_disarium(number):
    num_str = str(number)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return digit_sum == number
disarium_num = [num for num in range(1, 101) if is_disarium(num)]
print("Disarium numbers between 1 to 100 : ")
for num in disarium_num:
    print(num, end = " | ")
Disarium numbers between 1 to 100 : 
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 89 | 
---------------------------------------------------
19 is a Happy Number because:
The process reaches 1, so 19 is a Happy Number.
1 + = 82
2 9
2
8 + = 68
2 2
2
6 + = 100
2 8
2
1 + + = 1

def is_happy_num(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    return num == 1
num = int(input("Enter a number : "))
if is_happy_num(num):
    print(f"{num} is a happy number.")
else:
    print(f"{num} is a not a happy number.")
Enter a number : 23
23 is a happy number.
---------------------------------------------------
def is_happy_num(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    return num == 1
happy_num = []
for num in range(1, 101):
    if is_happy_num(num):
        happy_num.append(num)
print("Happy numbers between 1 and 100.")
print(happy_num)
Happy numbers between 1 and 100.
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
---------------------------------------------------
A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
18 is a Harshad number because , and 18 is divisible by 9
42 is not a Harshad number because , and 42 is not divisible by 6.
def is_harshad_num(num):
    digit_sum = sum(int(i) for i in str(num))
    return num % digit_sum == 0
num = int(input("Enter a number : "))
if is_harshad_num(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
Enter a number : 18
18 is a Harshad number.
---------------------------------------------------
A pronic number, also known as an oblong number or rectangular number, is a type of
figurate number that represents a rectangle. It is the product of two consecutive integers, n
and (n + 1). Mathematically, a pronic number can be expressed as:
For example, the first few pronic numbers are:
𝑃 = 𝑛 ∗ (𝑛 + 1) 𝑛
𝑃1 = 1 ∗ (1 + 1) = 2
𝑃2 = 2 ∗ (2 + 1) = 6
𝑃3 = 3 ∗ (3 + 1) = 12
𝑃4 = 4 ∗ (4 + 1) = 20
def is_pronic_num(num):
    for n in range(1, int(num ** 0.5)+1):
        if n * (n + 1) == num:
            return True
    return False
print("Pronic numbers between 1 and 100 are : ")
for i in range(1, 101):
    if is_pronic_num(i):
        print(i, end = " | ")
Pronic numbers between 1 and 100 are : 
2 | 6 | 12 | 20 | 30 | 42 | 56 | 72 | 90 | 
---------------------------------------------------
numbers = [30, 10, 45, 5, 20]
numbers.sort(reverse = True)
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")
The second largest number in the list is: 30
---------------------------------------------------
def find_n_largest_ele(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    largest_ele = sorted_lst[:n]
    return largest_ele
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
N = int(input("N = "))
result = find_n_largest_ele(numbers, N)
print(f"The {N} largest number in the list are :", result)
N = 3
The 3 largest number in the list are : [345, 100, 98]
---------------------------------------------------
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list = [i for i in list_of_lists if i]
print("List after removing empty lists:", filtered_list)
List after removing empty lists: [[1, 2, 3], [4, 5], [6, 7, 8]]
---------------------------------------------------
def count_occurance(l, element):
    count = l.count(element)
    return count
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = 2
occurances = count_occurance(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurances} times in list")
The element 2 appears 3 times in list
---------------------------------------------------
def find_words(words, k):
    result = []
    for i in words:
        if len(i) > k:
            result.append(i)
    return result
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragonfruit"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")
Words longer than 5 characters: ['banana', 'cherry', 'elderberry', 'dragonfruit']
---------------------------------------------------
def remove_char(input_str, i):
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
input_str = "Hello, wWorld!"
i = 7
new_str = remove_char(input_str, i)
print(f"Original String : {input_str}")
print(f"String after removing {i}th character: {new_str}")
Original String : Hello, wWorld!
String after removing 7th character: None
---------------------------------------------------
input_str = "Python program to split and join a string"
word_list = input_str.split()
separator = " "
output_str = separator.join(word_list)
print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)
Original String: Python program to split and join a string
List of split Words: ['Python', 'program', 'to', 'split', 'and', 'join', 'a', 'string']
Joined String: Python program to split and join a string
---------------------------------------------------
def is_binary_str(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True
input_str = "1001110"
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")
'1001110' is a binary string.
---------------------------------------------------
def uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    uncommon_words_set = words1.symmetric_difference(words2)
    uncommon_words_list = list(uncommon_words_set) 
    return uncommon_words_list
string1 = "This is first string"
string2 = "This is second string"
uncommon = uncommon_words(string1, string2)
print("Uncommon words : ", uncommon)
Uncommon words :  ['second', 'first']
---------------------------------------------------
def find_duplicates(input_str):
    char_count = {}
    duplicates = []
    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates
input_string = "piyush sharma"
duplicate_chars = find_duplicates(input_string)
print("Duplicate characters : ", duplicate_chars)
Duplicate characters :  ['s', 'h', 'a']
---------------------------------------------------
import re
def check_special_char(in_str):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'  
    if re.search(pattern, in_str):
        return True
    else:
        return False
input_string = str(input("Enter a string : "))
contains_special = check_special_char(input_string)
if contains_special:
    print("The string contains special characters. ")
else:
    print("The string does not contains special characters. ")
Enter a string : "Hello, World $!"
The string contains special characters. 
---------------------------------------------------
my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}
uni_val = set()
for i in my_dict.values():
    uni_val.add(i)
unique_values_list = list(uni_val)
print("Uniques values in the dictionary : ", unique_values_list)
Uniques values in the dictionary :  [10, 20, 30]
---------------------------------------------------
my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}
total_sum = 0 
for i in my_dict.values():
    total_sum += i
print("sum of all the items dictionary : ", total_sum)
sum of all the items dictionary :  90
---------------------------------------------------
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary (using dictionary unpacking) is : ", merged_dict)
Merged dictionary (using dictionary unpacking) is :  {'a': 1, 'b': 2, 'c': 3, 'd': 4}
---------------------------------------------------
key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict = {}
for key, value in key_values_list:
    flat_dict[key] = value
print("Flat dictionary : ", flat_dict)
Flat dictionary :  {'a': 1, 'b': 2, 'c': 3, 'd': 4}
---------------------------------------------------
from collections import OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
new_item = ('a',1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(ordered_dict)
print("Updated Ordered Dict : ", new_ordered_dict)
Updated Ordered Dict :  OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
---------------------------------------------------
from collections import OrderedDict
def check_order(string, reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)
    return string_dict == reference_dict
input_string = "hello world"
reference_string = "helo wrd"
if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the reference string")
else:
    print("The order of characters in the input string does not matche the reference string")
The order of characters in the input string matches the reference string
---------------------------------------------------
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Sorted by Keys : ")
for key, value in sorted_dict_by_keys.items():
    print(f"{key} : {value}")
Sorted by Keys : 
apple : 3
banana : 1
cherry : 2
date : 4
---------------------------------------------------
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_values = dict(
    sorted(sample_dict.items(), key=lambda item: item[1]))
print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
    print(f"{key}: {value}")
Sorted by values:
banana: 1
cherry: 2
apple: 3
date: 4
---------------------------------------------------
import math
C = 50
H = 30
def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))
input_seq = input("Enter comma seperated values of D: ")
D_values = input_seq.split(',')
result = [calculate_Q(int(D)) for D in D_values]
print(','.join(map(str, result)))
Enter comma seperated values of D: 100,150,180
18,22,24
---------------------------------------------------
X,Y = map(int, input("Enter two digits (X, Y): ").split(','))
array = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j
for row in array:
    print(row)
Enter two digits (X, Y): 3,5
[0, 0, 0, 0, 0]
[0, 1, 2, 3, 4]
[0, 2, 4, 6, 8]
---------------------------------------------------
input_sequence = input("Enter a comma-separated sequence of words: ")
words = input_sequence.split()
sorted_words = sorted(words)
sorted_sequence = ','.join(sorted_words)
print("Sorted words : ", sorted_sequence)
Enter a comma-separated sequence of words: without, hello, bag, world
Sorted words :  bag,,hello,,without,,world
---------------------------------------------------
input_sequence = input("Enter a comma-separated sequence of words: ")
words = input_sequence.split()
sorted_words = sorted(words)
result = ' '.join(sorted_words)
print("Result : ", result)
Enter a comma-separated sequence of words: hello world and practice makes perfect and hello world again
Result :  again and and hello hello makes perfect practice world world
---------------------------------------------------
sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char in sentence:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
print("LETTERS", letter_count)
print("DIGITS", digit_count)
Enter a sentence: hello world! 123
LETTERS 10
DIGITS 3
---------------------------------------------------
import re
def is_valid_password(password):
    if 6 <= len(password) <= 12:
        if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
        return False
password = input("Enter passwords separated by commas: ").split(',')
valid_passwords = []
for psw in password:
    if is_valid_password(psw):
        valid_passwords.append(psw)
print(','.join(valid_passwords))
Enter passwords separated by commas: ABd1234@1,a F1#,2w3E*,2We3345
ABd1234@1
---------------------------------------------------
input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
word_freq = {}
for word in words:
    word = word.strip('.,?')
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
sorted_words = sorted(word_freq.items())
for word, frequency in sorted_words:
    print(f"{word}:{frequency}")
Enter a sentence: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
2:2
3:1
3?read:1
and:1
between:1
choosing:1
new:1
or:2
python:5
to:1
---------------------------------------------------
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
sentences = []
for sub in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{sub} {verb} {obj}"
            sentences.append(sentence)
for sentence in sentences:
    print(sentence)
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
---------------------------------------------------
import zlib
string = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(string.encode())
decompressed_string = zlib.decompress(compressed_string).decode()
print("Original String:", string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)
Original String: hello world!hello world!hello world!hello world!
Compressed String: b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
Decompressed String: hello world!hello world!hello world!hello world!
---------------------------------------------------
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 4
result = binary_search(sorted_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")
Element 4 found at index 3
---------------------------------------------------
def divisible_by_5_and_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num
try:
    n = int(input("Enter a value for n: "))
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
Enter a value for n: 100
0,35,70
---------------------------------------------------
def fibbonacci(n):
    sequence = [0, 1]
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
    return sequence
try:
    n = int(input("Enter a value for n: "))
    result = fibbonacci(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
Enter a value for n: 8
0,1,1,2,3,5,8,13
---------------------------------------------------
def extract_username(email):
    parts = email.split('@')
    if len(parts) == 2:
        return parts[0]
    else:
        return "Invalid email format"
try:
    email = input("Enter an email address: ")
    username = extract_username(email)
    print(username)
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
Enter an email address: john@google.com
john
---------------------------------------------------
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2
shape = Shape()
square = Square(float(input("Enter the shape of the square : ")))
print("Shape's area by default:", shape.area()) 
print("Area of the square:", square.area()) 
Enter the shape of the square : 5
Shape's area by default: 0
Area of the square: 25.0
---------------------------------------------------
def stutter(word):
    if len(word) < 2:
        return "Word must be at least two characters long."
    stutter_word = f"{word[:2]} ... {word[:2]} ... {word}?"
    return stutter_word
print(stutter("incredible")) 
print(stutter("enthusiastic")) 
print(stutter("outstanding")) 
in ... in ... incredible?
en ... en ... enthusiastic?
ou ... ou ... outstanding?
---------------------------------------------------
import math
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)
print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))
57.3
1145.9
2864.8
---------------------------------------------------
def is_curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0
print(is_curzon(5)) 
print(is_curzon(10)) 
print(is_curzon(14))
True
False
True
---------------------------------------------------
import math
def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x**2) / 2
    return round(area, 1)
print(area_of_hexagon(1)) 
print(area_of_hexagon(2)) 
print(area_of_hexagon(3))
2.6
10.4
23.4
---------------------------------------------------
import math
def binary(decimal):
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal = decimal // 2
    return binary_str if binary_str else "0"
print(binary(1)) 
print(binary(5)) 
print(binary(10))
1
101
1010
---------------------------------------------------
def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b+1):
        if num % c == 0:
            total += num
    return total
print(evenly_divisible(1, 10, 20)) 
print(evenly_divisible(1, 10, 2)) 
print(evenly_divisible(1, 10, 3))
0
30
18
---------------------------------------------------
def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return False
print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 < 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))
True
False
True
---------------------------------------------------
def replace_vowels(string, char):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        string = string.replace(vowel, char)
    return string
print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))
th# ##rdv#rk
m?nn?? m??s?
sh*k*sp**r*
---------------------------------------------------
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input string must have same length")
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance
print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
5
0
1
---------------------------------------------------
def filter_list(lst):
    result = []
    for element in lst:
        if isinstance(element, int) and element >= 0:
            result.append(element)
    return result
print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
print(filter_list([1, "a", "b", 0, 15]))
[1, 2]
[1, 2, 123]
[1, 0, 15]
---------------------------------------------------
num = int(input("Enter number : "))
fact = 1
if num in (0, 1):
    fact = 1
else:
    for i in range(1, num+1):
        fact = fact * i
print(f"Factorial of {num} is : {fact}")
Enter number : 5
Factorial of 5 is : 120
---------------------------------------------------
text = input("Enter string to check if it is palindrome or not : ")
rev = ""
tempstr = ""
for i in text:
    if i.isalnum():
        rev = i + rev
        tempstr += i
if tempstr == rev:
    print("Given string is palindrome")
else:
    print(f"Given string is not palindrome")
Enter string to check if it is palindrome or not : madam
Given string is palindrome
---------------------------------------------------
text = input("Enter a string to find palindrome or not: ").lower()
rev = ""
tempstr = ""
for i in text:
    if i.isalnum(): 
        rev = i + rev
        tempstr += i
if tempstr == rev:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
Enter a string to find palindrome or not: Was it a car or a cat I saw?
Given string is palindrome
---------------------------------------------------
text = str(input("Enter string to count vowels and consonents : ")).lower()
vowels = 'aeiou'
vowels_cnt = 0
consonents_cnt = 0
for i in text:
    if i.isalpha():
        if i in vowels:
            vowels_cnt += 1
        else:
            consonents_cnt += 1
print(f"Vowels : {vowels_cnt}, Consonents : {consonents_cnt}")
Enter string to count vowels and consonents : Ashish Sunil Zope
Vowels : 6, Consonents : 9
---------------------------------------------------
num = int(input("Enter num : "))
sum = 0
temp = abs(num)
while temp > 0:
    sum += temp % 10
    temp //= 10
print(f"All digits if {num} : {sum}")
Enter num : 17121996
All digits if 17121996 : 36
---------------------------------------------------
def srt(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
    return array #(return sorted(array))

if __name__ == "__main__":
    array = [1, 5, 2, 6, 7, 9, 2]
    print(srt(array))
[1, 2, 2, 5, 6, 7, 9]
---------------------------------------------------
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
Enter temperature in Celsius: 37
37.0°C is equal to 98.60°F
---------------------------------------------------
num = int(input("Enter a number to check prime or not: "))
if num <= 1:
    print(f"{num} is neither Prime nor Composite number")
else:
    isPrime=True
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print("Given number is a Prime number")
    else:
        print("Given number is a Composite number")
Enter a number to check prime or not: 17
Given number is a Composite number
---------------------------------------------------
nth_term = int(input("Enter number of terms to generate "))
a, b = 0, 1
print("Fibonacci series upto Nth term:")
for i in range(nth_term):
    print(a, end = " ")
    a, b = b, a+b
Enter number of terms to generate 15
Fibonacci series upto Nth term:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
---------------------------------------------------
year = int(input("Enter year in YYYY format to check if a year is a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
Enter year in YYYY format to check if a year is a leap year: 2024
2024 is a leap year
---------------------------------------------------
sentence = str(input("Enter a sentences :"))
wordcount = 1 if len(sentence.strip()) > 0 else 0
for i in sentence:
    if i == " ":
        wordcount += 1
print(f"Total number of words in given sentence is {wordcount}")
Enter a sentences :Ashish Sunil Zope Senior Data engineer
Total number of words in given sentence is 6
---------------------------------------------------
list = list(map(int, input("Enter name seperated by space : ").split()))
if len(list) < 2:
    print("List should have at least 2 numbers.")
else:
    first = second = float('-inf')
    for num in list:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float('-inf'):
        print("No second largest number (all elements might be equal).")
    else:
        print(f"Second largest number is {second}.")
Enter name seperated by space : 8 3 9 3 5 0 3
Second largest number is 8.
---------------------------------------------------
list = list(map(int, input("Enter numbers seperated by space : ").split()))
uniq_list = []
for i in list:
    if i not in uniq_list:
        uniq_list.append(i)
print("List with duplicate elements : ", uniq_list)
Enter numbers seperated by space : 4 2 4 6 2 5 8 0 3 3
List with duplicate elements :  [4, 2, 6, 5, 8, 0, 3]
---------------------------------------------------
num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the second number : "))
def fn_find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
gcd = fn_find_gcd(num_1, num_2)
print(f"GCD of {num_1} and {num_2} is : {gcd}")
Enter the first number : 56
Enter the second number : 98
GCD of 56 and 98 is : 14
---------------------------------------------------
list = list(map(int, input("Enter numbers seperated by space : ").split()))
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print("Sorted list is : ", list)
Enter numbers seperated by space : 34 23 567 23 678 89
Sorted list is :  [23, 23, 34, 89, 567, 678]
---------------------------------------------------
list_1 = list(map(int, input("Enter first list (space seperated) : ").split()))
list_2 = list(map(int, input("Enter second list (space seperated) : ").split()))
common_ele = []
for i in list_1:
    if i in list_2 and i not in common_ele:
        common_ele.append(i)
print("Common elements in list are : ", common_ele)
Enter first list (space seperated) : 7 4 6 3 8 9 1 2 5 7 8 2
Enter second list (space seperated) : 1 2 5 9 5 6 2 3 7 0 1 2
Common elements in list are :  [7, 6, 3, 9, 1, 2, 5]
---------------------------------------------------
(.venv) PS C:\Users\vwank\PycharmProjects\Python_Aug25\Pytest> 
---------------------------------------------------
list_1 = list(map(int, input("Enter first list (space seperated) : ").split()))
list_2 = list(map(int, input("Enter second list (space seperated) : ").split()))
merged_list = []
i, j = 0, 0
while i < len(list_1) and j < len(list_2):
    if list_1[i] < list_2[j]:
        merged_list.append(list_1[i])
        i += 1
    else:
        merged_list.append(list_2[i])
        j += 1
merged_list += list_1[i:]
merged_list += list_2[j:]
print("Merged list is : ", merged_list)
Enter first list (space seperated) : 4 433 344 34 7
Enter second list (space seperated) : 45 23 56 78
Merged list is :  [4, 23, 23, 23, 23, 433, 344, 34, 7]
---------------------------------------------------
list = list(map(str, input("Enter second sorted list : ").split()))
isDigit = True
for i in list:
    if not i.isdigit():
        isDigit = False
        break
print("List contains only digit. "if isDigit else "List contain non-digit elements")
Enter second sorted list : Ashish Sunil Zope 28-10-1996 28 7744046830
List contain non-digit elements
---------------------------------------------------
import string
sentence = input("Enter string : ")
sent_no_punc = ""
for i in sentence:
    if i not in string.punctuation:
        sent_no_punc += i
print("Without punctuation : ", sent_no_punc)
Enter string : Ashish Sunil Zope, Senior Data Engineer: turning messy data into
insights—faster than tea...!!!Without punctuation :  Ashish Sunil Zope Senior Data Engineer turning messy data into
---------------------------------------------------
binary_num = input("Enter a binary number: ")
if not all (bit in "01" for bit in binary_num):
    print("Invalid input!! Please enter only 0s and 1s")
else:
    decimal_num = int(binary_num, 2)
    print(f"The decimal value of binary {binary_num} is {decimal_num}")
Enter a binary number: 1010010101
The decimal value of binary 1010010101 is 661
---------------------------------------------------
num = int(input("Enter decimal number : "))
bin_no = ""
temp = num
if num == 0:
    bin_no = "0"
while num > 0:
    bin_no = str(num % 2) + bin_no
    num //= 2
print(f"The binary value of decimal number {temp} is {bin_no}")
Enter decimal number : 18
The binary value of decimal number 18 is 10010
---------------------------------------------------
sentence = input("Enter string : ")
freq = {}
for char in sentence:
    if char != " ":
        freq[char] = freq.get(char,0)+1
max_char = ""
max_count = 0
for char, count in freq.items():
    if count > max_count:
        max_char = char
        max_count = count
print()
print(f"The maximum occuring character is '{max_char}' with {max_count} occurances.")
Enter string : shish Sunil Zope, Senior Data Engineer: turning messy data into insights—faster than tea...!!!
The maximum occuring character is 'n' with 9 occurances.
---------------------------------------------------
str1 = input("Enter first string : ").replace(" ", "").lower()
str2 = input("Enter second string : ").replace(" ", "").lower()
if len(str1) != len(str2):
    print("No, the strings are not anagrams.")
else:
    freq = {}
    for ch in str1:
        freq[ch] = freq.get(ch, 0)+1
    for ch in str2:
        if ch in freq:
            freq[ch] -= 1
        else:
            freq[ch] = 1
if all(value==0 for value in freq.values()):
    print("Yes, the strings are anagrams.")
else:
    print("No, given strings are not anagrams.")
Enter second string : silent
Yes, the strings are anagrams.
---------------------------------------------------
str = input("Enter a string : ")
upper = lower = 0
for char in str:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(f"upper : {upper}, lower : {lower}")
Enter a string : Ashish Sunil Zope, Senior Data Engineer
upper : 6, lower : 27
---------------------------------------------------
str = input("Enter a string : ")
result = ""
new_word = True
for char in str:
    if new_word and char.isalpha():
        result += char.upper()
        new_word = False
    else:
        result += char
    if char == " ":
        new_word = True
print(f"Capitalized : {result}")
Enter a string : ashish sunil zope senior data engineer
Capitalized : Ashish Sunil Zope Senior Data Engineer
---------------------------------------------------
str = input("Enter a string : ")
result = ""
new_word = True
for char in str:
    if char == " ":
        result += "_"
    else:
        result += char
print(f"Result : {result}")
Enter a string : Ashish Sunil Zope Senior Data Engineer
Result : Ashish_Sunil_Zope_Senior_Data_Engineer
---------------------------------------------------
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = int(input("Enter time in years: "))
n = int(input("Enter number of times interest applied per year: "))
amount = principal * (1 + rate/(100*n))**(n*time)
print(f"Compound Interest Amount: {amount:.2f}")
Enter principal amount: 100000
Enter annual interest rate (%): 13.74
Enter time in years: 10
Enter number of times interest applied per year: 12
Compound Interest Amount: 392039.88
---------------------------------------------------
		43 codes in Java
---------------------------------------------------
public class Main
{
	public static void main(String[] args) {
	    String string = "Big black bug bit a big black dog on his big black nose";
	    int count;
	    string = string.toLowerCase();
	    String words[] = string.split(" ");
		System.out.println("Duplicate words in given string : ");
		for (int i=0; i< words.length; i++) {
		    count = 1;
		    for (int j=i+1; j<words.length; j++) {
		        if (words[i].equals(words[j]))   {
		            count ++;
		            words[j] = "0";
		        }
		    } 
		    if (count > 1 && words[i] != "0")
		       System.out.println(words[i]);
		}
	}
}
Duplicate words in given string : 
big
black
---------------------------------------------------
public class Main
{
	public static void main(String[] args) {
	    int total;
	    int[] numbers = new int[]{1, 2, 3, 4, 6, 7};
	    total = 7;
	    int expected_sum = total * ((total + 1) / 2);
	    int num_sum = 0;
	    for (int i : numbers)
	        num_sum += i;
	    System.out.print(expected_sum - num_sum);
	}
}	==>		5
---------------------------------------------------
import java.util.concurrent.ThreadLocalRandom;
public class Main
{
    public static int getRandomValue(int min, int max) {
        return ThreadLocalRandom
        .current()
        .nextInt(min, max+1);
    }
	public static void main(String[] args) {
	    int min=1, max=100;
	    System.out.print("Random value between " + min +" and "+ max +" : "
	                    +getRandomValue(min, max));
	}
}
Random value between 1 and 100 : 9
---------------------------------------------------
import java.util.concurrent.ThreadLocalRandom;
public class Main
{
	public static void main(String[] args) {
	    String a = "Hello";
        String b = "World";
	    System.out.println("Strings before swap : a= " + a +" and b = " + b);
	    a = a  + b;
	    b = a.substring(0, a.length() - b.length());
	    a = a.substring(b.length());
	    System.out.println("Strings after swap : a= " + a +" and b = " + b);
	}
}
Strings before swap : a= Hello and b = World
Strings after swap : a= World and b = Hello
---------------------------------------------------
public class Main
{
    static void pushZerosToEnd(int arr[], int n) {
        int count=0;
        for (int i=0; i<n; i++)
            if (arr[i] != 0)
               arr[count++] = arr[i];
        while (count < n)
            arr[count++] = 0;
    }
	public static void main(String[] args) {
	    int arr[] = {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9};
	    int n = arr.length;
	    pushZerosToEnd(arr, n);
	    System.out.println("Arrays after pushing back to zeros : ");
	    for (int i=0; i<n; i++)
	       System.out.print(arr[i] + " ");
	}
}
Arrays after pushing back to zeros : 
1 9 8 4 2 7 6 9 0 0 0 0 
---------------------------------------------------
class TaskEvenOdd implements Runnable {
    private int max;
    private Printer print;
    private boolean isEvenNumber;
    TaskEvenOdd(Printer print, int max, boolean isEvenNumber)  {
        this.print = print;
        this.max = max;
        this.isEvenNumber = isEvenNumber;
    }
    @Override
    public void run() {
        int number = isEvenNumber == true ? 2 : 1;
        while (number <= max) {
            if (isEvenNumber)  {
                print.printEven(number);
            } else {
                print.printOdd(number);
            }
            number += 2;
        }
    }
}
class Printer {
    boolean isOdd = false;
    synchronized void printEven(int number)   {
        while (isOdd == false)   {
            try  {
                wait();
            }  catch (InterruptedException e) { e.printStackTrace();  }
        }
        System.out.println("Thread Odd : " +number);
        isOdd = true;
        notifyAll();
    }
    
    synchronized void printOdd(int number)  {
        while (isOdd == true)   {
            try  {
                wait();
            }  catch(InterruptedException e) { e.printStackTrace(); }
        }
        System.out.println("Thread Odd : " + number);
        isOdd = true;
        notifyAll();
    }
}

public class Main
{
    static int MAX=5;
	public static void main(String[] args) {
	    Printer print = new Printer();
	    Thread t1 = new Thread(new TaskEvenOdd(print, MAX, false));
	    Thread t2 = new Thread(new TaskEvenOdd(print, MAX, true));
	    t1.start();
	    t2.start();
	}
}
Thread Odd : 1
Thread Odd : 2
Thread Odd : 4
---------------------------------------------------
public class Main
{
    // Function for swapping the characters
    public static String swapString(String a, int i, int j) {
        char[] b =a.toCharArray();
        char ch;
        ch = b[i];
        b[i] = b[j];
        b[j] = ch;
        return String.valueOf(b);
    }
    // Function for generating different permutations of the string
    public static void generatePermutation(String str, int start, int end) {
        //Prints the permutations
        if (start == end-1)
            System.out.println(str);
        else {
        for (int i = start; i < end; i++) {
        //Swapping the string by fixing a character
        str = swapString(str,start,i);
        //Recursively calling function generatePermutation() for rest of the characters
        generatePermutation(str,start+1,end);
        //Backtracking and swapping the characters again.
        str = swapString(str,start,i);
        }
      }
    }
	public static void main(String[] args) {
	    String str = "ABC";
	    int len = str.length();
		System.out.println("All the permutations of string are : ");
		generatePermutation(str, 0, len);
	}
}
All the permutations of string are : 
ABC
ACB
BAC
BCA
CBA
CAB
---------------------------------------------------
public class Main
{
    static void reverses(String str) {
        char[] inputArray = str.toCharArray();
        char[] result = new char[inputArray.length];
        // Mark spaces in result
        for (int i = 0; i < inputArray.length; i++) {
        if (inputArray[i] == ' ') {
            result[i] = ' ';
            }
        }
        // Traverse input string from beginning
        // and put characters in result from end
        int j = result.length - 1;
        for (int i = 0; i < inputArray.length; i++) {
            // Ignore spaces in input string
                if (inputArray[i] != ' ') {
                // ignore spaces in result.
                    if (result[j] == ' ') {
                        j--;
                    }
                result[j] = inputArray[i];
                j--;
                }
            }
                System.out.println(String.valueOf(result));
            }
	public static void main(String[] args) {
		reverses("India Is my country");
	}
}	====>		yrtnu oc ym sIaidnI
---------------------------------------------------
import java.util.HashMap;
import java.util.Map;
public class Main
{
    public static String getUniqueCharacterSubstring(String input) {
    Map<Character, Integer> visited = new HashMap<>();
    String output = "";
    for (int start = 0, end = 0; end < input.length(); end++) {
        char currChar = input.charAt(end);
        if (visited.containsKey(currChar)) {
            start = Math.max(visited.get(currChar) + 1, start);
        }
        if (output.length() < end - start + 1) {
            output = input.substring(start, end + 1);
        }
            visited.put(currChar, end);
        }
        return output;
    }
    
	public static void main(String[] args) {
	    String input = "LongestSubstringFindOut";
		System.out.println("LongestSubstringFindOut --> "+getUniqueCharacterSubstring(input));
	}
}	====>		LongestSubstringFindOut --> LongestSub
---------------------------------------------------
public class Main
{
    static boolean areRotations(String str1, String str2)  {
        return (str1.length() == str2.length()) && ((str1 + str1).indexOf(str2) != -1);
    }
	public static void main(String[] args) {
	    String str1 = "AACD";
	    String str2 = "ACDA";
	    if (areRotations(str1, str2))
		    System.out.println("Strings are rotations for each other");
		else
		    System.out.println("Strings are not rotations for each other");
	}
}	===>	Strings are rotations for each other
---------------------------------------------------
public class Main
{
	public static void main(String[] args) {
	    String regex = "[0-9]+";
	    String data = "784375378237";
		System.out.println("Is Number : "+data.matches(regex));
	}
} ===>	Is Number : true
---------------------------------------------------
public class Main
{
	public void printTwoMaxNumbers(int[] nums) {
	    int maxOne = 0;
        int maxTwo = 0;
        for(int n:nums) {
        if(maxOne < n) {
        maxTwo = maxOne;
        maxOne = n;
	    } else if(maxTwo < n) {
            maxTwo = n;
	    }
	  }
	    System.out.println("First Max Number: "+maxOne);
        System.out.println("Second Max Number: "+maxTwo);
	}
	public static void main(String[] args) {
	    int num[] = {5,34,78,2,45,1,99,23};
        Main tmn = new Main();
        tmn.printTwoMaxNumbers(num);
	}
}
First Max Number: 99
Second Max Number: 78
---------------------------------------------------
public class Main
{
    void printLeaders(int arr[],  int size) {
        for (int i=0; i<size; i++) {
            int j;
            for (j=i+1; j<size; j++)  {
                if (arr[i] <= arr[j]) 
                   break;
            }
            if (j == size)
                System.out.print(arr[i] + " ");
        }
    }
	public static void main(String[] args) {
	    Main test = new Main();
	    int arr[] = new int[]{25, 10, 2, 4, 1, 3};
	    int n = arr.length;
	    test.printLeaders(arr, n);
	}
}	===>	25 10 4 3 
---------------------------------------------------
		Python - OOPs
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class RoleManager(Employee):

    next_role_id = 101

    def __init__(self, first_name, last_name, role_name):
        super().__init__(first_name, last_name)

        self.role_name = role_name

        # Auto assign role id
        self.role_id = RoleManager.next_role_id
        RoleManager.next_role_id += 1

    def display_employee(self):
        print("Employee Details")
        print(f"Name      : {self.first_name} {self.last_name}")
        print(f"Role Name : {self.role_name}")
        print(f"Role ID   : {self.role_id}")
        print()

# Input outside class
# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# role_name = input("Enter Role Name: ")


# Object creation
# emp = RoleManager(first_name, last_name, role_name)
emp = RoleManager("Vais", "Wank", "QA")
emp1 = RoleManager("Vaishali", "Wankhedkar", "Automation")

# Display
emp.display_employee()
emp1.display_employee()

Employee Details
Name      : Vais Wank
Role Name : QA
Role ID   : 101

Employee Details
Name      : Vaishali Wankhedkar
Role Name : Automation
Role ID   : 102
---------------------------------------------------
text = "python is good programming"
words = text.split()
result = ""
for word in words:
    reverse_wrd = ""
    for i in range(len(word)-1, -1, -1):
        reverse_wrd += word[i]
    result += reverse_wrd + " "
print(result.strip())
nohtyp si doog gnimmargorp
---------------------------------------------------
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1
counter = count_up_to(3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter)) #stopIteration
0
1
2
3
---------------------------------------------------
The Collatz sequence is generated if the number is even, divide it by 2; if the number is odd, multiply it by 3 and add 1.
def collatz_sequence(num):
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        sequence.append(num)
    return sequence
num = int(input("Enter number : "))
print(collatz_sequence(num))
Enter number : 10
[10, 5, 16, 8, 4, 2, 1]
---------------------------------------------------
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def is_rawword(word):
    letter_values = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
        'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
        't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
    }
    word_sum = 0
    for char in word.lower():
        if char.isalpha():
            word_sum += letter_values[char]
    return is_prime(word_sum)
word = "hello"
if is_rawword(word):
    print(f"{word} is a rawword")
else:
    print(f"{word} is not a rawword")
hello is not a rawword
abd is a rawword
---------------------------------------------------
Write a program to calculate the sum of the numbers in the string = "Today is 20th March, 2026."
text = "Today is 20th March, 2026."
total = 0
num = ""
for i in text:
    if i >= '0' and i <= '9':  #i.isdigit()
        num = num + i
    else:
        if num != "":
            total = total + int(num)
            num = ""
if num != "":
    total = total + int(num)
print(total)		===>	2046

OR

text = "Today is 20th March, 2026."
sum = 0
num = ""
for ch in text:
    if ch.isdigit():
        num += ch
    else:
        if num:
            sum = sum + int(num)
            num = ""
if num:
    sum += int(num)
print("sum = ", sum)	==>	2046
---------------------------------------------------
lst = [1, 2, 3, 2, 4, 1, 5, 3]
uniq_lst = []
[uniq_lst.append(i) for i in lst if i not in uniq_lst]
print(uniq_lst)

uniq_lst = []
for i in lst:
    if i not in uniq_lst:
        uniq_lst.append(i)
print(uniq_lst)

uniq_lst = []
uniq_lst = list(dict.fromkeys(lst))
print(uniq_lst)
output - [1, 2, 3, 4, 5]
---------------------------------------------------
str = "Python programming"
uniq_lst = []
[uniq_lst.append(i) for i in str if i not in uniq_lst and i != " "]
print(uniq_lst)

uniq_lst = []
for i in str:
    if i not in uniq_lst and i != " ":
        uniq_lst.append(i)
print(uniq_lst)

uniq_lst = []
uniq_lst = list(dict.fromkeys(i for i in str if i != " "))
print(uniq_lst)
['P', 'y', 't', 'h', 'o', 'n', 'p', 'r', 'g', 'a', 'm', 'i']
---------------------------------------------------
Write a program to print the name of the topper and his/her total marks.
students = {
    "Vaishali": [80, 90, 85],
    "Amit": [70, 75, 80],
    "Sneha": [95, 90, 92]
}
topper = ""
highest_total = 0
for name, marks in students.items():
    total = sum(marks)
    if total > highest_total:
        highest_total = total
        topper = name
print("Topper Name :", topper)
print("Total Marks :", highest_total)
Topper Name : Sneha
Total Marks : 277
---------------------------------------------------
def tic_tac_toe(matrix):
    # Check rows
    for row in matrix:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != ' ':
            return matrix[0][col]
    # Check diagonal
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != ' ':
        return matrix[0][0]
    # Check reverse diagonal
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != ' ':
        return matrix[0][2]
    # Check unfinished game
    for row in matrix:
        if ' ' in row:
            return "Game not over yet"
    # Tie
    return "Tie"
board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]
print(tic_tac_toe(board))		==>		X
---------------------------------------------------
def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        tower_of_hanoi(n-1, source, auxiliary, destination)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n-1, auxiliary, destination, source)
n = 3
source = "A"
destination = "C"
auxiliary = "B"
print(f"Solving Tower of Hanoi with {n} disks")
tower_of_hanoi(n, source, destination, auxiliary)
Solving Tower of Hanoi with 3 disks
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
---------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array : ", arr)
bubble_sort(arr)
print("Sorted array : ", arr)
Original array :  [64, 34, 25, 12, 22, 11, 90]
Sorted array :  [11, 12, 22, 25, 34, 64, 90]
---------------------------------------------------
m = int(input("Enter number of rows : "))
n = int(input("Enter number of columns : "))

minefield = []

# Input matrix
for i in range(m):
    row = []

    for j in range(n):
        element = int(input(f"Element at position ({i},{j}) : "))
        row.append(element)

    minefield.append(row)

# Initialize result matrix
neighbouring_mines = [[0 for _ in range(n)] for _ in range(m)]
# Count neighbouring mines
for i in range(m):
    for j in range(n):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Skip current cell
                if dx == 0 and dy == 0:
                    continue
                new_i = i + dx
                new_j = j + dy
                if 0 <= new_i < m and 0 <= new_j < n:
                    count += minefield[new_i][new_j]
        neighbouring_mines[i][j] = count
# Output
print("\nNeighbour Mine Count Matrix")
for row in neighbouring_mines:
    print(row)
Enter number of rows : 3
Enter number of columns : 3
Element at position (0,0) : 0
Element at position (0,1) : 1
Element at position (0,2) : 0
Element at position (1,0) : 1
Element at position (1,1) : 0
Element at position (1,2) : 1
Element at position (2,0) : 1
Element at position (2,1) : 0
Element at position (2,2) : 1

Neighbour Mine Count Matrix
[2, 2, 2]
[2, 5, 2]
[1, 4, 1]
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
		*** Leetcode ***
---------------------------------------------------
class Solution:
    def separateDigits(self, nums):
        result = []
        for num in nums:
            digits = []
            while num > 0:
                digit = num % 10
                digits.append(digit)
                num = num // 1
            # reverse to maintain original order
            digits.reverse()
            result.extend(digits)
        return result
nums = [30,130,14,754,41]
s = Solution()
print(s.separateDigits(nums))
[3, 1, 5, 2, 3, 8, 7, 7]
---------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        longest = ""
        for ch in strg:
            if ch not in st:
                st.append(ch)
            else:
                if len(st) > len(longest):
                    longest = "".join(st)
                while ch in st:
                    st.pop(0)
                st.append(ch)
        if len(st) > len(longest):
            longest = "".join(ch)
        return longest
b = Solution()
strg = "pwwkeopdfvw"
lng_str = b.lengthOfLongestSubstring(strg)
print(f"Longest substring : {lng_str} with lenth is : {len(lng_str)}")
Longest substring : wkeopdfv with lenth is : 8
---------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        last_idx = {}
        max_len = 0
        start_idx = 0
        for i in range(0, len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]]+1)
            max_len = max(max_len, i-start_idx+1)
            last_idx[s[i]] = i
        print(start_idx)
        print(last_idx)
        return max_len                
b = Solution()
strg = "pwwkeopdfvw"
print(b.lengthOfLongestSubstring(strg))
---------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        strlen = len(s)
        seenChar = {}
        substr = ""
        longest = 0
        finalList = []
        if (strlen <= 0):
            return strlen
        for L in range(strlen):
            if len(substr) > 0:
                finalList.append(substr)
            currLongest = 0
            substr = ""
            seenChar = {}
            for R in range(L, strlen):
                currChar = s[R]
                if currChar not in seenChar:
                    seenChar[currChar] = 1
                    substr += currChar
                    currLongest += 1
                    longest = max(currLongest, longest)
            else:
                break
        return longest
b = Solution()
strg = "pwwkehw"
print(b.lengthOfLongestSubstring(strg))	====>		5
---------------------------------------------------
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            steps += 1
        return steps
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
---------------------------------------------------
Approach 1: Brute Force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
s = Solution()
st = "babadda"
print(s.longestPalindrome(st))		==>	adda
---------------------------------------------------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]: 
            return s
        left = self.longestPalindrome(s[1:])
        right = self.longestPalindrome(s[:-1])

        if len(left)>len(right):
            return left
        else:
            return right
s = Solution()
st = "babadda"
print(s.longestPalindrome(st))	==>	adda
---------------------------------------------------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        Max_Len=1
        Max_Str=s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str
s = Solution()
st = "babadda"
print(s.longestPalindrome(st))	==>	adda
---------------------------------------------------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str
s = Solution()
st = "babadda"
print(s.longestPalindrome(st))	==>	adda
---------------------------------------------------
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxArea = 0
        while left < right:
            distance = right - left
            area = min(height[left], height[right]) * distance
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
height = [1,8,6,2,5,4,8,3,7]
s = Solution
print(Solution.maxArea(s, height))
OUTPUT: 49
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
		***	HackerRank	***
---------------------------------------------------
import collections
numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())
income = 0
for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)
Input (stdin)
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Your Output (stdout)
200
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
Pytest fixtures :
import pytest
class TestFixture:

    @pytest.fixture
    def first_entry(self):
        return "a"
    @pytest.fixture()
    def order(self):
        return []
    @pytest.fixture()
    def append_first(self,order, first_entry):
        return order.append(first_entry)
    def test_string(self, append_first, order, first_entry):
        print("order-----", order)
        print("first_entry-----", first_entry)
        assert order == [first_entry]
(.venv) PS C:\Users\vwank\PycharmProjects\Python_Aug25\Pytest> pytest -v -s .\TestFixture2.py
================================================================================== test session starts ===================================================================================
platform win32 -- Python 3.13.1, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\vwank\PycharmProjects\PytestJuly25\.venv\Scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.13.1', 'Platform': 'Windows-11-10.0.26200-SP0', 'Packages': {'pytest': '8.4.1', 'pluggy': '1.6.0'}, 'Plugins': {'dependency': '0.6.0', 'html': '4.1.1', 'metadata': '3.1.1', 'rerunfailures': '15.1', 'xdist': '3.8.0'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-24.0.2'}
rootdir: C:\Users\vwank\PycharmProjects\Python_Aug25\Pytest
plugins: dependency-0.6.0, html-4.1.1, metadata-3.1.1, rerunfailures-15.1, xdist-3.8.0
collected 1 item

TestFixture2.py::TestFixture::test_string order----- ['a']
first_entry----- a
PASSED
---------------------------------------------------
import pytest
@pytest.mark.parametrize("username, password",[("vais","3005"),("wank","8282")])
def test_sample_one(username, password):
    print(username, password)
========================================================================================= PASSES ========================================================================================= 
_______________________________________________________________________________ test_sample_one[vais-3005] _______________________________________________________________________________ 
---------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------- 
vais 3005
_______________________________________________________________________________ test_sample_one[wank-8282] _______________________________________________________________________________ 
---------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------- 
wank 8282
================================================================================ short test summary info ================================================================================= 
PASSED test_parameterize1.py::test_sample_one[vais-3005]
PASSED test_parameterize1.py::test_sample_one[wank-8282]
============================================================================== 2 passed, 1 warning in 0.04s ============================================================================== 

---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
