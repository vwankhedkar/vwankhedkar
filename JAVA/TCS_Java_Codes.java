// Time Complexity: O(n) — We scan the entire array once.
// Space Complexity: O(1) — We use only a few extra variable
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,0,3,4,5,6,7,8,2};
        int min = arr[0];
        int max = arr[0];
        for (int i=1; i<arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max)
               max = arr[i];
        }
        System.out.println("Minimum is : "+min+", Maximum is : "+max);
    }
}    
-------------------------------------------------------------
// Time Complexity: O(n log n) — Due to sorting.
// Space Complexity: O(1) — Only two variables are used
import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,0,3,4,5,6,7,8,2};
        Arrays.sort(arr);
        System.out.println("Minimum is : "+arr[0]+", Maximum is : "+arr[arr.length-2]);
    }
}
OUTPUT ==>    Minimum is : 0, Maximum is : 8

*********************************************************************************
//Time Complexity: O(n) — Each element is swapped once.
//Space Complexity: O(1) — We are swapping elements in plac
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,3};
        int start=0, end=arr.length-1;
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
        for (int num : arr)
            System.out.print(num+" ");
    }
}    =====>        3 2 8 2 7 1 1 
*********************************************************************************
// Time Complexity: O(n) — We traverse the array once.
// Space Complexity: O(n) — Space is required for the frequency 
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,1};
        System.out.print("Count of each num : "+countFreq(arr));
    }
    public static Map<Integer,Integer> countFreq(int[] arr) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num,0)+1);
        }
        return freqMap;
    }
}    ==>    Count of each num : {1=3, 2=2, 7=1, 8=1}
*********************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {7, 3, 2, 9, 0, 6, 7, 3, 1, 2, 9, 0, 6, 4, 8, 5, 1};
        rearrangeArray(arr);  // call the method
    }
    public static void rearrangeArray(int[] arr) {
        Arrays.sort(arr);  // sort first
        int[] result = new int[arr.length];
        int left = 0, right = arr.length - 1;
        for (int i = 0; i < arr.length; i++) {
            if (i % 2 == 0) {
                result[i] = arr[right--];  // pick largest remaining
            } else {
                result[i] = arr[left++];   // pick smallest remaining
            }
        }
        System.arraycopy(result, 0, arr, 0, arr.length);
        System.out.println(Arrays.toString(result));
    }
}    --->    [9, 0, 9, 0, 8, 1, 7, 1, 7, 2, 6, 2, 6, 3, 5, 3, 4]
// Time Complexity: O(n log n) — Due to sorting.
// Space Complexity: O(n) — We use an extra array for rearrangin
*********************************************************************************
// Time Complexity: O(n) — We traverse the array once.
// Space Complexity: O(1) — No extra space required.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        int sum=0;
        for (int num : arr) {
            sum += num;
        }
        System.out.print("Sum of numbers : "+sum);
    }
}   Sum of numbers : 27
*********************************************************************************
// Time Complexity: O(n) — Each element is reversed a constant number of times.
// Space Complexity: O(1) — In-place modification
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        int[] result;
        result = rotateArray(arr, 5);
        System.out.print("Rotated array : "+Arrays.toString(result));
    }
    public static int[] rotateArray(int[] arr, int k) {
        int n = arr.length;
        k = k % n;
        reverse(arr, 0 , k-1);
        reverse(arr, k , n-1);
        reverse(arr, 0 , n-1);
        return arr;
    }
    public static void reverse(int[] arr, int start, int end) {
        while(start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}    ==>    Rotated array : [0, 1, 0, 7, 0, 8, 4, 0, 2, 5]
*********************************************************************************
// Time Complexity: O(n) — We reuse the sum calculation.
// Space Complexity: O(1) — Only constant space used
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        double result;
        result = (double)sumOfArray(arr)/arr.length; ;
        System.out.print("Sum of array : "+result);
    }
    public static int sumOfArray(int[] arr) {
        int sum = 0;
        for (int num : arr) {
        sum += num;
        }
        return sum;
    }
}    ==>        Sum of array : 2.7
*********************************************************************************
// Time Complexity: O(n log n) — Sorting the array.
// Space Complexity: O(1) — Sorting is done in place
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        double result;
        result = findMedian(arr) ;
        System.out.print("Sum of array : "+result);
    }
    public static double findMedian(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        if (n % 2 == 0) {
            return (arr[n/2-1] + arr[n/2])/2.0;
        } else {
            return arr[n / 2];
          }
    }  
}    ===>        Sum of array : 1.5
*********************************************************************************
// Time Complexity: O(n) — Copying the entire array.
// Space Complexity: O(n) — Extra space for the new arra
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 1, 7, 0};
        int[] result = addElement(arr, 6);
        System.out.println("Array after adding element: " + Arrays.toString(result));
    }
    public static int[] addElement(int[] arr, int ele) {
        int[] newArr = new int[arr.length + 1];
        System.arraycopy(arr, 0, newArr, 0, arr.length);
        newArr[arr.length] = ele;  
        return newArr;
    }
}  ==>   Array after adding element: [8, 4, 0, 2, 5, 0, 1, 0, 1, 7, 0, 6]
*********************************************************************************
// Time Complexity: O(n) — We traverse the array and use a set.
// Space Complexity: O(n) — Set and list both take linear space
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        List<Integer> result = findRepeating(arr);
        System.out.println("Array after adding element: " + result);
    }
    public static List<Integer> findRepeating(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        List<Integer> repeating = new ArrayList<>();
        for (int num : arr) {
            if (!seen.add(num)) {
                repeating.add(num);
            }
        }
        return repeating;
    }
}    ==>    Array after adding element: [0, 1, 7, 0]
*********************************************************************************
// Time Complexity: O(n) — Two passes: one to count, another to filter.
// Space Complexity: O(n) — HashMap to store counts.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        List<Integer> result = findNonRepeating(arr);
        System.out.println("Array after adding element: " + result);
    }
    public static List<Integer> findNonRepeating(int[] arr) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num,0)+1);
        }
        List<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer>entry : countMap.entrySet()) {
            if (entry.getValue() == 1) {
                result.add(entry.getKey());
            }
        }
        return result;
    }
}    ==>        Array after adding element: [2, 4, 5, 8]
*********************************************************************************
// Time Complexity: O(n) — Traverse the array once.
// Space Complexity: O(n) — Map takes linear space.
import java.util.*;
class Main {
    public static void main(String[] args) {
        // Each element is a pair {a, b}
        int[][] arr = {
            {1, 2},
            {3, 4},
            {5, 9},
            {2, 1},
            {4, 3},
            {6, 7}
        };

        List<int[]> result = findSymmetricPairs(arr);
        System.out.println("Symmetric pairs: ");
        for (int[] pair : result) {
            System.out.println(Arrays.toString(pair));
        }
    }
    public static List<int[]> findSymmetricPairs(int[][] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        List<int[]> result = new ArrayList<>();

        for (int[] pair : arr) {
            int first = pair[0], second = pair[1];

            // If we already have the reverse pair (b, a)
            if (map.containsKey(second) && map.get(second) == first) {
                result.add(new int[]{second, first});
            } else {
                map.put(first, second);
            }
        }
        return result;
    }
}    ==>        Symmetric pairs: 
[1, 2]
[3, 4]
*********************************************************************************
// Time Complexity: O(n) — One pass through the array.
// Space Complexity: O(1) — Constant extra space.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        int result = maxProdSubArray(arr);
        System.out.println("Maximum Product Subarray: " + result);
    }
    public static int maxProdSubArray(int[] arr) {
        if (arr == null || arr.length == 0) return 0;
        int max = arr[0];
        int min = arr[0];
        int result = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < 0) {
                // swap max and min when negative number appears
                int temp = max;
                max = min;
                min = temp;
            }
            max = Math.max(arr[i], max * arr[i]);
            min = Math.min(arr[i], min * arr[i]);
            result = Math.max(result, max);
        }
        return result;
    }
}    ==>    Maximum Product Subarray: 2240
*********************************************************************************
// Time Complexity: O(n log n) — Sorting the array.
// Space Complexity: O(n) — Space for the rank map.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        int[] result = rankArray(arr);
        System.out.println("Ranks of each element in an Array: " + Arrays.toString(result));
    }
    public static int[] rankArray(int[] arr) {
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;
        for (int i = 0; i < sorted.length; i++) {
            if (!rankMap.containsKey(sorted[i])) {
                rankMap.put(sorted[i], rank++);
            }
        }
        for (int i=0; i<arr.length; i++) {
            arr[i] = rankMap.get(arr[i]);
        }
        return arr;
    }
}     ==>     Ranks of each element in an Array: [7, 4, 6, 3, 5, 1, 2, 1, 2, 6, 1]   
*********************************************************************************
// Time Complexity: O(n log n) — Sorting the array by frequency.
// Space Complexity: O(n) — Map and result array.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        int[] result = sortByFreq(arr);
        System.out.println("Sorted array as per frequency : " + Arrays.toString(result));
    }
    public static int[] sortByFreq(int[] arr) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num,0)+1);
        } 
        return Arrays.stream(arr)
        .boxed()
        .sorted((a,b) -> {
            int freqCompare = freqMap.get(b).compareTo(freqMap.get(a));
            return freqCompare != 0 ? freqCompare : Integer.compare(a,b);
        })
        .mapToInt(i -> i)
        .toArray();
    }
}  ==>    Sorted array as per frequency : [0, 0, 0, 1, 1, 7, 7, 2, 4, 5, 8]
*********************************************************************************
// Time Complexity: O(n) — Reversing the elements.
// Space Complexity: O(1) — No extra space used
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        int k = 3;  // number of positions to rotate
        rotateLeft(arr, k);
        System.out.println("Array after left rotation by " + k + " : " + Arrays.toString(arr));
        rotateRight(arr, k);
        System.out.println("Array after right rotation by " + k + " : " + Arrays.toString(arr));
    }
    public static void rotateLeft(int[] arr, int k) {
        k = k % arr.length;
        reverse(arr, 0, k - 1);
        reverse(arr, k, arr.length - 1);
        reverse(arr, 0, arr.length - 1);
    }
    public static void rotateRight(int[] arr, int k) {
        k = k % arr.length;
        reverse(arr, 0, arr.length - 1);
        reverse(arr, 0, k - 1);
        reverse(arr, k, arr.length - 1);
    }
    public static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}
Array after left rotation by 3 : [2, 5, 0, 1, 0, 1, 7, 0, 8, 4, 7]
Array after right rotation by 3 : [8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0]
*********************************************************************************
// Time Complexity: O(n) — Single pass through the array.
// Space Complexity: O(1) — Only a few extra variables.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 1, 1, 6, 1, 7, 8};
        int result = findEquilibriumIndex(arr);
        System.out.println("Equilibrium Index: " + result);
    }
    public static int findEquilibriumIndex(int[] arr) {
        int totalSum = 0, leftSum = 0;
        for (int num : arr)
            totalSum += num;
        for (int i = 0; i < arr.length; i++) {
            totalSum -= arr[i]; 
            if (leftSum == totalSum)
                return i;
            leftSum += arr[i];
        }
        return -1; 
    }
}        ==>    Equilibrium Index: -1
int[] arr = {1, 3, 5, 2, 2};    ==>    Equilibrium Index: 2
*********************************************************************************
// Time Complexity: O(n) — Reversing elements.
// Space Complexity: O(1) — In-place reversal.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 2, 2};
        int k = 2; // rotate by 2 steps
        circularRotate(arr, k);
        System.out.println("Circularly Rotated Array: " + Arrays.toString(arr));
    }
    public static void circularRotate(int[] arr, int k) {
        k = k % arr.length;
        reverse(arr, 0, arr.length - 1);
        reverse(arr, 0, k - 1);
        reverse(arr, k, arr.length - 1);
    }
    public static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}    ==>    Circularly Rotated Array: [2, 2, 1, 3, 5]
*********************************************************************************
// Time Complexity: O(n + m) — n is the size of the array, m is the size of the order array.
// Space Complexity: O(n) — Extra space for the frequency map
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 2, 2, 3, 1};
        int[] order = {3, 1, 2}; // sort by this order
        int[] result = sortByOrder(arr, order);
        System.out.println("Array sorted by order: " + Arrays.toString(result));
    }
    public static int[] sortByOrder(int[] arr, int[] order) {
        Map<Integer, Integer> freqMap = new HashMap<>();

        // Count frequency of each number
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        int index = 0;
        for (int num : order) {
            if (freqMap.containsKey(num)) {
                int count = freqMap.get(num);
                while (count-- > 0)
                    arr[index++] = num;
                freqMap.remove(num);
            }
        }
        for (int num : freqMap.keySet()) {
            int count = freqMap.get(num);
            while (count-- > 0)
                arr[index++] = num;
        }

        return arr;
    }
}    ==>    Array sorted by order: [3, 3, 1, 1, 2, 2, 5]
*********************************************************************************
// Time Complexity: O(n) — Scan through the array.
// Space Complexity: O(1) — No extra space.
class Main {
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 2, 2, 3, 1};
        int ele = 5;
        int result = searchElement(arr, ele);
        if (result != -1)
            System.out.println("Element " + ele + " found at index: " + result);
        else
            System.out.println("Element " + ele + " not found");
    }
    public static int searchElement(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key) return i;
        }
        return -1;
    }
}
*********************************************************************************
// Time Complexity: O(n + m) — n is the size of the first array, m is the size of the second array.
// Space Complexity: O(n) — Extra space for the set
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 5, 2, 2, 3, 1, 7, 8, 9};
        int[] arr2 = {1, 7, 8, 9};
        boolean result = isSubSet(arr1, arr2);
        if (result)
            System.out.println("arr2 is a subset of arr1");
        else
            System.out.println("arr2 is NOT a subset of arr1");
    }
    public static boolean isSubSet(int[] arr1, int[] arr2) {
        Set<Integer> set = new HashSet<>();
        for (int num : arr1) {
            set.add(num);
        }
        for (int num : arr2) {
            if (!set.contains(num)) {
                return false;
            }
        }
        return true;
    }
}    =====>    arr2 is a subset of arr1
*********************************************************************************
// Time Complexity: O(n)
// Space Complexity: O(1)
import java.util.*;
class Main {
    public static void main(String[] args) {
        String str = "malayalam";
        System.out.println("isPalindrome : " + palindromeCheck(str));
    }
    public static boolean palindromeCheck(String str) {
        int left=0, right=str.length()-1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left ++;
            right --;
        }
        return true;
    }
}      =====>   isPalindrome : true
*********************************************************************************
// Time Complexity: O(n)
// Space Complexity: O(1)
import java.util.*;
class Main {
    public static void main(String[] args) {
        String str = "Hello World";
        countVowelConsonent(str);
    }
    public static void countVowelConsonent(String str) {
        int vowels=0, consonents=0, spaces=0;
        str = str.toLowerCase();
        for (char ch : str.toCharArray()) {
            if (ch == ' ') {
                spaces++;
            } else if (ch >= 'a' && ch <= 'z') {
                if ("aeiou".indexOf(ch) != -1)
                    vowels++;
                else
                    consonents++;
            }
        }
        System.out.println("Vowels : " + vowels);
        System.out.println("Consonents : " + consonents);
        System.out.println("Spaces : " + spaces);
    }
}    ===>    
Vowels : 3
Consonents : 7
Spaces : 1
*********************************************************************************
// Time Complexity: O(1)
// Space Complexity: O(1)
import java.util.*;
class Main {
    public static void main(String[] args) {
        String str = "AHello World";
        for (char ch : str.toCharArray()) {
            System.out.print((int)ch + " ");
        }
        countVowelConsonent(str);
    }
    public static void countVowelConsonent(String str) {
        int vowels=0, consonents=0, spaces=0;
        str = str.toLowerCase();
        for (char ch : str.toCharArray()) {
            if (ch == ' ') {
                spaces++;
            } else if (ch >= 'a' && ch <= 'z') {
                if ("aeiou".indexOf(ch) != -1)
                    vowels++;
                else
                    consonents++;
            }
        }
        System.out.println("\nVowels : " + vowels);
        System.out.println("Consonents : " + consonents);
        System.out.println("Spaces : " + spaces);
    }
}
65 72 101 108 108 111 32 87 111 114 108 100 
Vowels : 4
Consonents : 7
Spaces : 1
*********************************************************************************
// Time Complexity: O(n)
// Space Complexity: O(n)
import java.util.*;
class Main {
    public static void main(String[] args) {
        String str = "Hello World123";
        String revstr;
        String str1 = "3 + (2 * [4 + 5])";
        System.out.print("Ascii values of each char are : ");
        for (char ch : str.toCharArray()) {
            System.out.print((int)ch + " "); //TC, SC -> O(1)
        }
        System.out.println("\nAfter removing vowels : "+str.replaceAll("[AEIOUaeiou]",""));  //TC, SC -> O(n)
        System.out.println("After removing spaces : "+str.replaceAll("\\s",""));  //TC, SC -> O(n)
        System.out.println("After removing nonAlphabets : "+str.replaceAll("[^a-zA-Z]",""));  //TC, SC -> O(n)
        revstr = new StringBuilder(str).reverse().toString();
        System.out.println("After string reversing : " +revstr);
        System.out.println("After removing brackets : " +str1.replaceAll("[\\[\\]{}()]",""));
    }
}
Ascii values of each char are : 72 101 108 108 111 32 87 111 114 108 100 49 50 51 
After removing vowels : Hll Wrld123
After removing spaces : HelloWorld123
After removing nonAlphabets : HelloWorld
After string reversing : 321dlroW olleH
After removing brackets : 3 + 2 * 4 + 5
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************

    
