import java.util.Objects;
public class Main{
    public int id;
    private String name;
    public Main(int id, String name) {
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
        if (obj==null||getClass()!=obj.getClass())
            return false;
        Main student = (Main) obj;
        return id == student.id && Objects.equals(name, student.name);
    }
    public static void main(String[] args) {
        Main student1 = new Main(1,"Alice");
        Main student2 = new Main(2,"Bob");
        Main student3 = new Main(1,"Alice");
        System.out.println("student1.equals(student2): "+ student1.equals(student2));
        System.out.println("student1.equals(student3): "+ student1.equals(student3));
        System.out.println("Hashcode of student1:"+student1.hashCode());
        System.out.println("Hashcode of student2:"+student2.hashCode());
        System.out.println("Hashcode of student3:"+student3.hashCode());
    }
}
student1.equals(student2): false
student1.equals(student3): true
Hashcode of student1:63351360
Hashcode of student2:67988
Hashcode of student3:63351360
*************************************************************************************************
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;
public class Main {
    public static void main(String[] args) {
        int[] array = {1, 1, 2, 2, 3, 4, 5, 5, 6, 6};
        List<Integer> result = findNonRepeatedElements(array);
        System.out.println("Non-repeated elements : "+result);
    }
    public static List<Integer> findNonRepeatedElements(int[] array) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : array) {
            countMap.put(num, countMap.getOrDefault(num, 0)+1);
        }
        List<Integer> nonRepeatedElements = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == 1) {
                nonRepeatedElements.add(entry.getKey());
            }
        }
        return nonRepeatedElements;
    }
}  ==>  Non-repeated elements : [3, 4]
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	    int[] count = countOddAndEven(array);
		System.out.println("Even numbers count : "+count[1]);
		System.out.println("Odd numbers count : "+count[0]);
	}
	public static int[] countOddAndEven(int[] array) {
	    int[] count = new int[2];
	    for (int num : array) {
	        if (num % 2 == 0) {
	            count[1]++;
	        } else
	        count[0]++;
	    }
	    return count;
	}
}
Even numbers count : 4
Odd numbers count : 5
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {5, 2, 9, 1, 6, 3,0};
        int max = findMaximum(array);
        int min = findMinimum(array);
        System.out.println("Maximum value in the array : "+ max);
        System.out.println("Minimum value in the array : "+ min);
	}
	public static int findMaximum(int[] array) {
	    if (array.length == 0) {
	        throw new IllegalArgumentException("Array must not be empty");
	    }
	    int max = array[0];
	    for (int i=1; i<array.length-1; i++) {
	        if (array[i] > max)
	            max = array[i];
	    }
	    return max;
	}
	public static int findMinimum(int[] array) {
	    if (array.length == 0) {
	        throw new IllegalArgumentException("Array must not be empty");
	    }
	    int min = array[0];
	    for (int i=1; i<= array.length-1; i++) {
	        if (array[i] < min) 
	            min = array[i];
	    }
	    return min;
	} 
}
Maximum value in the array : 9
Minimum value in the array : 0
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    String[] array = {"5", "2", "9", "a", "1", "6", "#", "3"};
        int sum = sumIntegers(array);
        System.out.println("Sum of the integers in array : "+ sum);
	} 
	public static int sumIntegers(String[] array) {
	    int sum = 0;
	    for (String element : array) {
	        try {
	            int num = Integer.parseInt(element);
	            sum += num;
	        } catch (NumberFormatException e) {
	            // Ignore elements
	        }
	    }
	    return sum;
	}
}	==>	Sum of the integers in array : 26
*************************************************************************************************
public class Main
{
	public static void main(String[] args) {
	    int[] array = {5, 2, 9, 1, 6, 3};
	    int target = 6;
        int index= linearSearch(array, target);
        if (index != -1) {
            System.out.println("Element " + target + " found at index : " + index);
        } else {
            System.out.println("Element " + target + " not found in the array");
        }
	}
	public static int linearSearch(int[] array, int target) {
	    for (int i=0; i<array.length; i++) {
	        if (array[i] == target) {
	            return i;
	        }
	    }
	    return -1;
	}
} ==>	Element 6 found at index : 4
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************

*************************************************************************************************
