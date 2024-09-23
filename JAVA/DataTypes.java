// for b = 10.5  /tmp/n8m0g4uaM4/Test.java:6: error: incompatible types: possible lossy conversion from double to byte
// for b = & 128 values /tmp/WEYDE5l5ou/Test.java:6: error: incompatible types: possible lossy conversion from int to byte
class Test {
    public static void main(String[] args) {
        byte b = 12;
        System.out.println(b);
    }
}

//Integer : for 2147483648 /tmp/MBEwpbRvHP/Test.java:6: error: integer number too large int x = 2147483648;

class Test {
    public static void main(String[] args) {
        int x = 2147483647;
        System.out.println(x);
    }
}

// Float & Double
class Test {
    public static void main(String[] args) {
        System.out.println(Float.MAX_VALUE);
        System.out.println(Float.MIN_VALUE);
        System.out.println(Double.MAX_VALUE);
        System.out.println(Double.MIN_VALUE);
    }
}

/ * OUTPUT :
3.4028235E38
1.4E-45
1.7976931348623157E308
4.9E-324
    */
    
// Boolean
class Test {
    public static void main(String[] args) {
        boolean b = true;
        System.out.println(b);
    }
}

// char 
class Test {
    public static void main(String[] args) {
        char c = 'c';
        System.out.println(c);
    }
}

// Octal
class Test {
    public static void main(String[] args) {
        int x = 0XBeef;
        System.out.println(x);
    }
}
OUTPUT : 48879

class Test {
    public static void main(String[] args) {
        int x = 0XBeer;
        System.out.println(x);
    }
}

ERROR!
/tmp/KVCn4XbXlT/Test.java:6: error: ';' expected
        int x = 0XBeer;

// Decimal, Octal, Hexadecimal
class Test {
    public static void main(String[] args) {
        int x = 10;
        int y = 010;
        int z = 0x10;
        System.out.println(x+"..."+y+"..."+z);
    }
}
OUTPUT : 10...8...16

// Double
class Test {
    public static void main(String[] args) {
        double d = 123.456;
        System.out.println(d);
    }
}

double d = 0786 // interger number too large as decimal takes only 0-7
double d = 0xFace // valid
double d = 0786.0 // valid
double d = 0xFace.0 //invalid
double d = 10 // valid
double d = 0777 //valid

class Test {
    public static void main(String[] args) {
        double d = 1.2e3;
        System.out.println(d);
    }
}
OUTPUT - 1200.0

