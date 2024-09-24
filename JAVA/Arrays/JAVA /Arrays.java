// corresponding class names for array types
class Test {
    public static void main(String[] args)
    {
        int[] x = new int[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT -    [I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [[I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [B

class Test {
    public static void main(String[] args)
    {
        boolean[] x = new boolean[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [Z



