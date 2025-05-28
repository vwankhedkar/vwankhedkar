
package com.tryPrograms;
public class Try1 {
    // Method to calculate max area
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1, max = 0;
        while (left < right) {
            int area = Math.min(height[left], height[right]) * (right - left);
            max = Math.max(max, area);
            if (height[left] < height[right]) left++;
            else right--;
        }
        return max;
    }
    public static void main(String[] args) {
        Try1 obj = new Try1();
        int[] heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        int result = obj.maxArea(heights);
        System.out.println("Maximum area is: " + result);
    }
}
OUTPUT -----  Maximum area is: 49
**********************************************************************
 3Sum
package WebHandling;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
public class tryProgs2 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = obj.threeSum(nums);
        System.out.println("Triplets with sum zero: " + result);
    }
}
OUTPUT -----  Triplets with sum zero: [[-1, -1, 2], [-1, 0, 1]]
**********************************************************************
10. Remove Nth Node From End of List
package WebHandling;
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
public class tryProgs2 {   
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy, fast = dummy;
        // Move fast n+1 steps ahead
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }
        // Move both pointers until fast reaches the end
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        // Delete the nth node
        slow.next = slow.next.next;
        return dummy.next;
    }
    // Utility method to create a linked list from array
    public ListNode createList(int[] nums) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (int num : nums) {
            current.next = new ListNode(num);
            current = current.next;
        }
        return dummy.next;
    }
    // Utility method to print a linked list
    public void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] nums = {1, 2, 3, 4, 5};
        ListNode head = obj.createList(nums);

        System.out.print("Original List: ");
        obj.printList(head);

        ListNode updated = obj.removeNthFromEnd(head, 2);

        System.out.print("After Removing 2nd from End: ");
        obj.printList(updated);
    }
}
Original List: 1 2 3 4 5 
After Removing 2nd from End: 1 2 3 5 
**********************************************************************
package WebHandling;
public class tryProgs2 {   
    public int maxSubArray(int[] nums) {
    	int max = nums[0], currentSum = nums[0];
    	for (int i=0; i<nums.length; i++)  {
    		currentSum = Math.max(nums[i], currentSum+nums[i]);
    		max = Math.max(max, currentSum);
    	}
    	return max;
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] nums = {1, 2, 3, 4, 5};
        int sum = obj.maxSubArray(nums);

        System.out.println("Sum is : "+ sum);
    }
}
OUTPUT ---- Sum is : 16
**********************************************************************

**********************************************************************

**********************************************************************
  
**********************************************************************

**********************************************************************

**********************************************************************
  
**********************************************************************

**********************************************************************

**********************************************************************
  
**********************************************************************
