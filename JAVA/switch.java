Syntax
switch(x) {
  case 1:  Action1;
           Break;
  case 2:  Action2;
           Break;
  ......
  case 3:  Action3;
           Break;
  Default:
          Default Action
}

Independent statements are not allowed inside switch statements
public class Main {
    public static void main(String[] args) {
        int x = 10;
        switch(x) {
            System.out.println("Hello");
        }
    }
}
OUTPUT
ERROR!
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
            ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                  ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                   ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                      ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                       ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                              ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                               ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                                      ^
/tmp/iSOEVPBrmK/Main.java:5: error: case, default, or '}' expected
            System.out.println("Hello");
                                       ^
9 errors

public class Main {
    public static void main(String[] args) {
        int x = 10;
        final int y = 20; // only  int y = 20 not allowed error thrown -> constant expression required case y:
        switch(x) {
            case 10:
            case y:
        }
    }
}
OUTPUT - no error
public class Main {
    public static void main(String[] args) {
        int x = 10;
        final int y = 20;
        switch(x) {
            case 10:
                System.out.println(10);
                break;
            case y:    // constant exoression required if no final used
                System.out.println(20);
                break;
        }
    }
}
OUTPUT - 10

  public class Main {
    public static void main(String[] args) {
        int x = 10;
        switch(x+1){
            case 10:
                System.out.println(10);
                break;
            case 10+20+30:
                System.out.println(60);
        }
    }
}
OUTPUT - no error

class Test {
    public static void main(String[] args) {
        byte b = 10;
        switch (b+1) {
            case 10:
            case 100:
            case 1000:
        }
    }
}
class Test {
    public static void main(String[] args) {
        byte b = 10;
        switch (b+1) {
            case 10:
                System.out.println(10);
                break;
            case 100:
                System.out.println(100);
                break;
            case 1000:
                System.out.println(1000);
                break;
        }
    }
}
OUTPUT - no error with switch (b) 
error is - Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
        Case constant of type int is incompatible with switch selector type byte
Same error for below code
class Test {
    public static void main(String[] args) {
        byte b = 10;
        switch (b) {
            case 10:
                System.out.println(10);
                break;
            case 100:
                System.out.println(100);
                break;
            case 1000:
                System.out.println(1000);
                break;
        }
    }
}

class Test {
    public static void main(String[] args) {
        byte b = 10;
        switch (b+1) {
            case 97:
                System.out.println(10);
                break;
            case 98:
                System.out.println(100);
                break;
            case 'a':
                System.out.println(1000);
                break;
        }
    }
}
OUTPUT  Exception in thread "main" java.lang.Error: Unresolved compilation problems: 
        Duplicate case
        Duplicate case

Default case can be written anywhere in switch 
class Test {
    public static void main(String[] args) {
        byte b = 98;
        switch (b+1) {
            case 97:
                System.out.println(97);
                break;
            default:
                System.out.println("default");
            case 98:
                System.out.println(98);
                break;
        }
    }
}
OUTPUT - 98

  

