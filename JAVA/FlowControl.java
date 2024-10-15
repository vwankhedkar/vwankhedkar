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

  
