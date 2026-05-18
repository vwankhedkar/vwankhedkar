*************************************************************************
			*** Leetcode *****
*************************************************************************
class Solution {
    public int numberOfSteps(int num) {
        int steps = 0;
        while (num != 0) {
            if (num % 2 == 0) {
                num = num / 2;
            }
            else
              num = num - 1;
            steps += 1;
        }
        return steps;
    }
}
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
*************************************************************************
class ListNode {

    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}
class Main {
    public boolean isPalindrome(ListNode head) {
        StringBuilder values = new StringBuilder();
        ListNode temp = head;
        while (temp != null) {
            values.append(temp.val);
            temp = temp.next;
        }
        String original = values.toString();
        String reversed =
                new StringBuilder(original).reverse().toString();
        return original.equals(reversed);
    }
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(2);
        head.next.next.next = new ListNode(1);
        Main s = new Main();
        System.out.println(s.isPalindrome(head));
    }
}
*************************************************************************
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
    }
}
class Main {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        return dummy.next;
    }
    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val);
            if (head.next != null) {
                System.out.print(" -> ");
            }
            head = head.next;
        }
    }
    public static void main(String[] args) {
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);
        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);
        Main s = new Main();
        ListNode result = s.addTwoNumbers(l1, l2);
        printList(result);
    }
}	===>	7 -> 0 -> 8
*************************************************************************
Java program to find the longest without repeating characters
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
*************************************************************************
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int len1 = nums1.length;
        int len2 = nums2.length;
        int left = 0;
        int right = len1;
        while (left <= right) {
            int part1 = (left + right) / 2;
            int part2 = (len1 + len2 + 1) / 2 - part1;
            int maxLeft1 = (part1 == 0)
                    ? Integer.MIN_VALUE
                    : nums1[part1 - 1];
            int minRight1 = (part1 == len1)
                    ? Integer.MAX_VALUE
                    : nums1[part1];
            int maxLeft2 = (part2 == 0)
                    ? Integer.MIN_VALUE
                    : nums2[part2 - 1];
            int minRight2 = (part2 == len2)
                    ? Integer.MAX_VALUE
                    : nums2[part2];
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((len1 + len2) % 2 == 0) {
                    return (Math.max(maxLeft1, maxLeft2)
                            + Math.min(minRight1, minRight2)) / 2.0;
                }
                return Math.max(maxLeft1, maxLeft2);
            }
            else if (maxLeft1 > minRight2) {
                right = part1 - 1;
            }
            else {
                left = part1 + 1;
            }
        }
        throw new IllegalArgumentException("Input arrays are not sorted.");
    }
}
*************************************************************************
class Solution {
    public String longestPalindrome(String s) {
        if (s.length() <= 1) {
            return s;
        }
        int maxLen = 1;
        String maxStr = s.substring(0, 1);

        for (int i = 0; i < s.length(); i++) {
            for (int j = i + maxLen; j <= s.length(); j++) {
                if (j - i > maxLen && isPalindrome(s.substring(i, j))) {
                    maxLen = j - i;
                    maxStr = s.substring(i, j);
                }
            }
        }
        return maxStr;
    }
    private boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
----------------------------------------
public class Solution {
    public String longestPalindrome(String s) {
        if (s.equals(new StringBuilder(s).reverse().toString())) {
            return s;
        }

        String left = longestPalindrome(s.substring(1));
        String right = longestPalindrome(s.substring(0, s.length() - 1));

        if (left.length() > right.length()) {
            return left;
        } else {
            return right;
        }
    }
}
----------------------------------------------------
public class Solution {
    public String longestPalindrome(String s) {
        if (s.length() <= 1) {
            return s;
        }
        int maxLen = 1;
        String maxStr = s.substring(0, 1);
        s = "#" + s.replaceAll("", "#") + "#";
        int[] dp = new int[s.length()];
        int center = 0;
        int right = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i < right) {
                dp[i] = Math.min(right - i, dp[2 * center - i]);
            }
            while (i - dp[i] - 1 >= 0 && i + dp[i] + 1 < s.length() && s.charAt(i - dp[i] - 1) == s.charAt(i + dp[i] + 1)) {
                dp[i]++;
            }
            if (i + dp[i] > right) {
                center = i;
                right = i + dp[i];
            }
            if (dp[i] > maxLen) {
                maxLen = dp[i];
                maxStr = s.substring(i - dp[i], i + dp[i] + 1).replaceAll("#", "");
            }
        }
        return maxStr;
    }
}
---------------------------------------
public class Solution {
    public String longestPalindrome(String s) {
        if (s.length() <= 1) {
            return s;
        }
        int maxLen = 1;
        int start = 0;
        int end = 0;
        boolean[][] dp = new boolean[s.length()][s.length()];
        for (int i = 0; i < s.length(); ++i) {
            dp[i][i] = true;
            for (int j = 0; j < i; ++j) {
                if (s.charAt(j) == s.charAt(i) && (i - j <= 2 || dp[j + 1][i - 1])) {
                    dp[j][i] = true;
                    if (i - j + 1 > maxLen) {
                        maxLen = i - j + 1;
                        start = j;
                        end = i;
                    }
                }
            }
        }
        return s.substring(start, end + 1);
    }
}
*************************************************************************
class Solution {
    public int maxArea(int[] height) {
        int max_area = 0;
        int left = 0;
        int right = height.length - 1;
        while (left < right) {
            max_area = Math.max(max_area, (right-left)* Math.min(height[left], height[right]));
            if (height[left] < height[right])
                left ++;
            else 
                right --;
        }
        return max_area;
    }
}
*************************************************************************
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int reverse = 0;
        int xcopy = x;
        while (x > 0) {
            reverse = (reverse * 10) + (x % 10);
            x /= 10;
        }
        return reverse == xcopy;
    }
}
*************************************************************************
class Solution {
    Result[][] memo;

    public boolean isMatch(String text, String pattern) {
        memo = new Result[text.length() + 1][pattern.length() + 1];
        return dp(0, 0, text, pattern);
    }

    public boolean dp(int i, int j, String text, String pattern) {
        if (memo[i][j] != null) {
            return memo[i][j] == Result.TRUE;
        }
        boolean ans;
        if (j == pattern.length()) {
            ans = i == text.length();
        } else {
            boolean first_match =
                (i < text.length() &&
                    (pattern.charAt(j) == text.charAt(i) ||
                        pattern.charAt(j) == '.'));

            if (j + 1 < pattern.length() && pattern.charAt(j + 1) == '*') {
                ans = (dp(i, j + 2, text, pattern) ||
                    (first_match && dp(i + 1, j, text, pattern)));
            } else {
                ans = first_match && dp(i + 1, j + 1, text, pattern);
            }
        }
        memo[i][j] = ans ? Result.TRUE : Result.FALSE;
        return ans;
    }
}
*************************************************************************
class Solution {
    public String intToRoman(int num) {
        final int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        final String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", 
        "IX", "V", "IV", "I"};
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<values.length; ++i) {
            if (num == 0)
               break;
            while (num >= values[i]) {
                sb.append(symbols[i]);
                num -= values[i];
            }
        }
        return sb.toString();
        }
}
*************************************************************************
class Solution {
    public int romanToInt(String s) {
        int ans = 0;
        Map<Character, Integer> roman = new HashMap<>();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);
        for (int i=0; i<s.length()-1; i++)  {
            if (roman.get(s.charAt(i)) < roman.get(s.charAt(i+1)))  {
                ans -= roman.get(s.charAt(i));
            } else {
                ans += roman.get(s.charAt(i));
            }
        }
        return ans + roman.get(s.charAt(s.length() - 1));
    }
}
*************************************************************************
class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder ans = new StringBuilder();
        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length-1];
        for (int i=0; i<=Math.min(first.length(), last.length()); i++) {
            if (first.charAt(i) != last.charAt(i))  {
                return ans.toString();
            }
            ans.append(first.charAt(i));
        }
        return ans.toString();
    }
}
*************************************************************************
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i=0; i<nums.length; i++)  {
            if (i>0 && nums[i] == nums[i-1])  {
                continue;
            }
            int j = i + 1;
            int k = nums.length -1;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                if (total > 0)  {
                    k--;
                } else if (total < 0) {
                    j++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    while (nums[j] == nums[j-1] && j < k) {
                        j++;
                    }
                }
            }
        }
        return res;
    }
}
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

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
		Javascript
*************************************************************************
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) {
        return false;
    }
    let reverse = 0;
    let xcopy = x;
    while (x > 0) {
        reverse = (reverse * 10) + (x % 10);
        x = Math.floor(x / 10);
    }
    return reverse == xcopy
};		==> True
*************************************************************************
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let res = 0;
    const roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    for (let i = 0; i < s.length - 1; i++) {
        if (roman[s[i]] < roman[s[i + 1]]) {
            res -= roman[s[i]];
        } else {
            res += roman[s[i]];
        }
    }

    return res + roman[s[s.length - 1]];    
};
*************************************************************************
var threeSum = function(nums) {
    let res = [];
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i-1]) {
            continue;
        }
        
        let j = i + 1;
        let k = nums.length - 1;

        while (j < k) {
            let total = nums[i] + nums[j] + nums[k];

            if (total > 0) {
                k--;
            } else if (total < 0) {
                j++;
            } else {
                res.push([nums[i], nums[j], nums[k]]);
                j++;

                while (nums[j] === nums[j-1] && j < k) {
                    j++;
                }
            }
        }
    }
    return res;    
};
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
