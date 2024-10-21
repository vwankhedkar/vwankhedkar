import java.util.*;
class Test {
    public static void main(String[] args) {
        String orig, rev = ""; // Objects of String class 
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a string/number to check if it is a palindrome");  
        orig = in.nextLine();
        int length = orig.length();
        for (int i=length-1; i>=0; i--)
        {
            rev = rev + orig.charAt(i);
            System.out.println(rev);
        }
        if (orig.equals(rev))
            System.out.println("String is Palingrome");
        else
            System.out.println("String is not Palingrome");
    }
}
PS C:\Users\VWankhedkar\PycharmProjects\Robot>  c:; cd 'c:\Users\VWankhedkar\PycharmProjects\Robot'; & 'C:\Program Files\Java\jre1.8.0_421\bin\java.exe' '-cp' 'C:\Users\VWankhedkar\AppData\Roaming\Code\User\workspaceStorage\538f90e2a7e8ceeb2cfc0d33f075b13d\redhat.java\jdt_ws\Robot_9e862827\bin' 'Test' 
Enter a string/number to check if it is a palindrome
aba
a
ab
aba
String is Palingrome
PS C:\Users\VWankhedkar\PycharmProjects\Robot>  c:; cd 'c:\Users\VWankhedkar\PycharmProjects\Robot'; & 'C:\Program Files\Java\jre1.8.0_421\bin\java.exe' '-cp' 'C:\Users\VWankhedkar\AppData\Roaming\Code\User\workspaceStorage\538f90e2a7e8ceeb2cfc0d33f075b13d\redhat.java\jdt_ws\Robot_9e862827\bin' 'Test'
Enter a string/number to check if it is a palindrome
abcda
a
ad
adc
adcb
adcba
String is not Palingrome
