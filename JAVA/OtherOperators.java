// instanceof 
Object o = l.get();
if (o instanceof Student) {
  Student s = (Student)o;
  // perform student specific functionality
}
else if (o instanceof Customer){
  Customer c = (Customer)o;
  // perform customer specific functionality
}
class Test {
    public static void main(String[] args){
    Thread t = new Thread();
    System.out.println(t instanceof Thread); // true
    System.out.println(t instanceof Object);  // true
    System.out.println(t instanceof Runnable);  // true
    System.out.println(t instanceof String);  // false - error: incompatible types: Thread cannot be converted to String
    }
}
class Test {
    public static void main(String[] args){
    System.out.println(null instanceof Thread); // false
    System.out.println(null instanceof Object);  // false
    System.out.println(null instanceof String);  // false
    System.out.println(null instanceof Runnable);  // false
    }
}
class Test {
    public static void main(String[] args){
    System.out.println(true & false); // false
    System.out.println(true | false);  // true
    System.out.println(true ^ false);  // true
    System.out.println(true ^ true);  // false
    }
}
class Test {
    public static void main(String[] args){
    System.out.println(4 & 5); // 4   100 & 101 = 100
    System.out.println(4 | 5);  // 5  100 | 101 = 101
    System.out.println(4 ^ 5);  // 1  100 & 101 = 001
    System.out.println(4 ^ 4);  // 0
    }
}
class Test {
    public static void main(String[] args){
    System.out.println(~true); // error: bad operand type boolean for unary operator '~'4
    //System.out.println(~4);  
    }
}
class Test {
    public static void main(String[] args){
    System.out.println(!4); // error: bad operand type int for unary operator '!'
    System.out.println(!true);  // -5
    }

& | ^ - applicable for boolean and integral
~ - applicable only for integral but not for boolean
! - applicable only for boolean but not for integral

implicit typecasting
class Test {
    public static void main(String[] args){
    int x = 'a';
    double d = 10;
    System.out.println(x); // 97
    System.out.println(d);  // 10.0
    }
}

explicit type casting
class Test {
    public static void main(String[] args){
    int x = 130;
    byte b = x; // error: incompatible types: possible lossy conversion from int to byte
    byte b = (byte)x // -126
    System.out.println(b); 
    }
}

class Test {
    public static void main(String[] args){
    int x = 150;
    short s = (short)x;
    System.out.println(s);//150
    byte b = (byte)x; 
    System.out.println(b);  // -106
    }
}
class Test {
    public static void main(String[] args){
    double d = 130.456;
    int x = (int)d;
    System.out.println(x);//130
    byte b = (byte)d; 
    System.out.println(b);  // -126
    }
}
    int x = 10; // simple assignment operator
    a=b=c=d=20; // Chained assignment
    a += 20; // compound += -= *= /= %= &= |= ^= >>= >>>=

class Test {
    public static void main(String[] args){
    byte b = 10;
    //b = b+1; //error: incompatible types: possible lossy conversion from int to byte
   // b++; // 11
   // b += 1; // 11
    b = (byte)(b+1); // 11
    System.out.println(b);  // -126
    }
}
class Test {
    public static void main(String[] args){
    int a,b,c,d;
    a = b = c = d = 20;
    a += b -= c *= d /= 2;
    System.out.println(a +" "+ b +" " + c + " " + d + " "); // -160 -180 200 10 
    }
}
// conditional / ternary operator
class Test {
    public static void main(String[] args){
    // int x = (10 < 20) ? 30 : 40; // 30
    int x = (10 > 20) ? 30 : ((40 > 50) ? 60 : 70); // 70
    System.out.println(x);
    }
}


