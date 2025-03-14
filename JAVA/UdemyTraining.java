public class Exercise {
  
    public static void main(String[] args) {
        System.out.println(printResult());
    }
    
    public static String printResult(){
        // Write your logic here
        return "Row, row, row your boat\nGently down the stream!!!";
 
    }
}
*****************************************************
public class Exercise {
  
    public static void main(String[] args) {
        System.out.println(printResult());
    }
    
    public static String printResult(){
        // Write your logic here
        return "Row, row, row your boat\nGently down the stream!!!";
 
    }
}
*******************************************************************
public class Exercise {
 
    public static void main(String[] args) {
       System.out.println(printResult());
    }
    
    public static int printResult(){
        float x = 5.2f;
        int y = (int)x;
        return y;
    }
}
*********************************************************8
public class Exercise {
     public static void main(String[] args) {
        System.out.print(printResult());
    }
    public static String printResult() {
         int a = -11 + 5 * 2;
         int b = (87 + 4) % 7;
         int c = (33 + -2 * 9) / 1;
         int d = 6 % 5 / 3 * 6 - 8 ;
 
         return "a value : "+a + " | b value : " + b + " | c value : " + c + " | d value : " + d;
    }
}
*********************************************************************************
public class Exercise {
 
    public static void main(String[] args) {
        System.out.println(calAvg(7,9,11));
    }
    
    public static double calAvg(int a, int b, int c){
       return (a+b+c)/3;
    }
}
***************************************************************************
public class Exercise {
 
    public static void main(String[] args) {
        System.out.println(isLeapYear(2048) );
    }
 
    public static boolean isLeapYear(int year)
    {
        boolean step_1 = (year % 4) == 0;
        boolean step_2 = (year % 100) != 0;
        boolean step_3 = ((year % 100 == 0) && (year % 400 == 0));
 
        return step_1 && (step_2 || step_3);
    }
}
**********************************************************************
public class Exercise {
 
   public static void main(String[] args) {
        System.out.println(printResult());
    }
 
    public static String printResult(){
        String finalStr = "";
        for (int i=1;i<=4;i++){
            String s="";
            for(int j=1;j<=i;j++){
                s=s+"*";
            }
            finalStr = finalStr+s+"\n";
        }
        return finalStr;
    }
}
*********************************************************************
public class Exercise {
 
    public static void main(String[] args) {
        System.out.println(printResult());
    }
 
    public static String printResult(){
        String finalStr = "";
        for(int i=1;i<=10;i++){
            finalStr = finalStr + "2 * "+i+" = "+2*i +"\n";
        }
        return finalStr;
    }
}
*************************************************************************
