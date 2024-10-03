class Test {
    public static void main(String[] args){
    //int x = (10 < 20) ? 30 : 40; // 30
    int x = (10 > 20) ? 30 : ((40 > 50) ? 60 : 70); // 70
    System.out.println(x);
    }
}
OUTPUT - 1
2
3
4
5
6
32

1. Unary operators
  [], x++, x--
  ++x, --x, ~, !
  new, <type>
2. Arithmatic operators
  *, /, %
  +, -
3. Shift Operators
  >>, >>>, <<
4. Comparison operators
  <, <=, >, >=, instalceof
5. equality operators
  ==, !=
6. Bitwise operators
  &, ^, |
7. Short circuit operators
  &&
  ||
8. Conditional operators
  ?:
9. Assignment operators
  =, +=, -=, *= ......

  
