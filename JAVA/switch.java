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
