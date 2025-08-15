public class Main {

    public static void main(String[] args) {
        // Print Hello to the console
        
        int x = 0 ;
        if (x){
            System.out.println("Hello");
        }
        else{
            System.out.println("Hi");
        }
    }
}
OUTPUT - Main.java:21: error: incompatible types: int cannot be converted to boolean        if (x){

        int x = 10 ;
        if (x=20){
            System.out.println("Hello");
        }
        else{
            System.out.println("Hi");
        }
  
OUTPUT - Main.java:21: error: incompatible types: int cannot be converted to boolean
        if (x=20){

public class Main {

    public static void main(String[] args) {
        // Print Hello to the console
        
        int x = 10 ;
        if (x==20){
            System.out.println("Hello");
        }
        else{
            System.out.println("Hi");
        }
    }
}
OUTPUT -    Hi

public class Main{
    public static void main(String[] args){
        boolean x = true;
        if (x = false){
            System.out.println("Hello");
        }
        else{
            System.out.println("Hi");
        }
    }
}
OUTPUT -    Hi

public class Main{
    public static void main(String[] args){
        boolean x = false;
        if (x == false){
            System.out.println("Hello");
        }
        else{
            System.out.println("Hi");
        }
    }
}
OUTPUT - Hello

public class Main{
    public static void main(String[] args){
        if (true){
            System.out.println("Hello");
        }
    }
}

public class Main{
    public static void main(String[] args){
        if (true)
            System.out.println("Hello");
    }
}

public class Main{
    public static void main(String[] args){
        if (true);
            System.out.println("Hello");
    }
}
OUTPUT - Hello
public class Main{
    public static void main(String[] args){
        if (true);
    }
}
Valid w/o error but no output

public class Main{
    public static void main(String[] args){
        if (true)
            int x = 10;
    }
}

class Test {
    public static void main(String[] args){
        if (true)
            int x = 10;
    }
}
OUTPUT - error: variable declaration not allowed here            int x = 10;
  Declarative statement shud nt be allowed in if stmt w/o {}

        if (true)
            System.out.println("HEllO");
  is allowed
            if (true);
  is allowed
            if (true)
            x = 10;
  is not allowed

  ; is valid java stamt called as empty stmnt
************************************************************************************
class Test {
    public static void main(String[] args)
    {
        int x = 10;
        if (x == 10)
            break;    // break not allowed inside if loop but continue is allowed as below
        System.out.println("Hello");
    }
}
ERROR!
/tmp/kpvS3DFQ7S/Test.java:9: error: break outside switch or loop

class Test {
    public static void main(String[] args)
    {
        int x = 10;
        if(x == 10)
            continue;
        System.out.println("Hello");
    }
}
/tmp/82WTNXHqov/Test.java:9: error: continue outside of loop
**********************************************************************
class Test {
    public static void main(String[] args)
    {
        for (int i=0; i<10; i++)
        {
            if (i % 2 == 0)
                continue;
            System.out.println(i);
        }
    }
}
java -cp /tmp/oYdSmUnJqZ/Test
1
3
5
7
9
*************************************************************************************
class Test {
    public static void main(String[] args)
    {
        for (int i=0; i<3; i++)
        {
            for (int j=0; j<3; j++)
            {
                if (i == j)
                    continue;
                    System.out.println(i+"..."+j);
            }
        }
    }
}
java -cp /tmp/4VcRYgj96B/Test
0...1
0...2
1...0
1...2
2...0
2...1
************************************************************************************
class Test {
    public static void main(String[] args)
    {
        int x = 0;
        do
        {
            x ++;
            System.out.println(x);
            if (++x < 5)
                continue;
            x++;
            System.out.println(x);
        }while (++x < 10);
    }
}
java -cp /tmp/zxmAfKc6o8/Test
1
4
6
8
10
********************************************************************************
class Test {
    public static void main(String[] args)
    {
        final int a=10, b=20;
        while (a > b)
        {
            System.out.println("Hello");
        }
        System.out.println("Hi");
    }
}
/tmp/vv4i5pn6ti/Test.java:8: error: unreachable statement
*************************************************************************************
class Test {
    public static void main(String[] args)
    {
        do
        {
            System.out.println("Hello");
        }
        while (true);
        System.out.println("Hi");
    }
}
/tmp/NyRlXp4gsT/Test.java:11: error: unreachable statement
*********************************************************************************
class Test {
    public static void main(String[] args)
    {
        do
        {
            System.out.println("Hello");
        }
        while (false);
        System.out.println("Hi");
    }
}
java -cp /tmp/rtFGFX9kXs/Test
Hello
Hi
*************************************************************************************
class Test {
    public static void main(String[] args)
    {
        int i=0;
        for(System.out.println("Hello U R Sleeping"); i<3; i++);
        {
            System.out.println("No I'm not sleeping");
        }
    }
}
java -cp /tmp/2MTE1MccZi/Test
Hello U R Sleeping
No I'm not sleeping
**************************************************************************************
class A {
    public static void main(String[] args)
    {
        System.out.println("This is class A");
    }
}
class B {
    public static void main(String[] args)
    {
        System.out.println("This is class B");
    }
}
class D {
}
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase\Test> javac Tests.java
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase\Test> java A
This is class A
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase\Test> java B
This is class B
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase\Test> java D
Error: Main method not found in class D, please define the main method as:
   public static void main(String[] args)
or a JavaFX application class must extend javafx.application.Application
*********************************************************************************************
  
