package com.basic;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.ListIterator;
class Book {
	int id;
	String name,author, publisher;
	int quantity;
	public Book(int id, String name, String author, String publisher, int quantity) {
		this.id = id;
		this.name = name;
		this.author = author;
		this.publisher = publisher;
		this.quantity = quantity;
	}
}
public class HashSetDemo {
	public static void main(String[] args) {
		List<Book> list = new ArrayList<Book>();
		Book b1=new Book(101,"Let us C","Yashwant Kanetkar","BPB",8);   
	    Book b2=new Book(102,"Java Program Questation","Rajendra","Technolamror",4);   
	    Book b3=new Book(103,"Operating System","Galvin","Wiley",6);   
		list.add(b1);
		list.add(b2);
		list.add(b3);
		System.out.println("Original content of list is: "); 
		for (Book b : list) {
			System.out.println(b.id+" "+b.name+" "+b.author+" "+b.publisher+" "+b.quantity);
		}
		ListIterator<Book> itr = list.listIterator();
		System.out.println("Modified content of list in backward is: ");
		while (itr.hasNext()) {
			Book st=(Book)itr.next(); 
			System.out.println(st.quantity+" "+st.publisher+" "+st.author+" "+st.name+" "+st.id);
		}
	}
}
Original content of list is: 
101 Let us C Yashwant Kanetkar BPB 8
102 Java Program Questation Rajendra Technolamror 4
103 Operating System Galvin Wiley 6
Modified content of list in backward is: 
8 BPB Yashwant Kanetkar Let us C 101
4 Technolamror Rajendra Java Program Questation 102
6 Wiley Galvin Operating System 103
********************************************************************************************
package com.basic;
import java.util.Iterator;
import java.util.LinkedList;
public class HashSetDemo {
	public static void main(String[] args) {
		LinkedList<String> al = new LinkedList<String>();
		al.add("Vaishali");
		al.add("Rupali");
		al.add("Sandeep");
		al.add("Vishal");
		Iterator<String> itr = al.iterator();
		while(itr.hasNext()) {
			System.out.print(itr.next()+" ");
		}
	}
}
Vaishali Rupali Sandeep Vishal 
********************************************************************************************
package com.basic;
import java.util.ArrayList;
import java.util.Iterator;
public class HashSetDemo {
	public static void main(String[] args) {
		ArrayList<String> al = new ArrayList<String>();
		al.add("Vaishali");
		al.add("Rupali");
		al.add("Sandeep");
		al.add("Vishal");
		Iterator itr = al.iterator();
		while(itr.hasNext()) {
			System.out.print(itr.next()+" ");
		}
	}
}
Vaishali Rupali Sandeep Vishal 
********************************************************************************************
package com.basic;
import java.text.SimpleDateFormat;
import java.util.Date;
public class HashSetDemo {
	public static void main(String[] args) throws Exception {
		String sDate1="31/12/1998";   
	    String sDate2 = "31-Dec-1998";   
	    String sDate3 = "12 31, 1998";   
	    String sDate4 = "Thu, Dec 31 1998";   
	    String sDate5 = "Thu, Dec 31 1998 23:37:50";   
	    String sDate6 = "31-Dec-1998 23:37:50";  
	    SimpleDateFormat formatter1=new SimpleDateFormat("dd/my/yyyy");
	    SimpleDateFormat formatter2=new SimpleDateFormat("dd-MMM-yyyy");   
	    SimpleDateFormat formatter3=new SimpleDateFormat("MM dd, yyyy");   
	    SimpleDateFormat formatter4=new SimpleDateFormat("E, MMM dd yyyy");   
	    SimpleDateFormat formatter5=new SimpleDateFormat("E, MMM dd yyyy HH:mm:ss");   
	    SimpleDateFormat formatter6=new SimpleDateFormat("dd-MMM-yyyy HH:mm:ss"); 
	    Date date1 = formatter1.parse(sDate1);
	    Date date2 = formatter1.parse(sDate1);
	    Date date3 = formatter1.parse(sDate1);
	    Date date4 = formatter1.parse(sDate1);
	    Date date5 = formatter1.parse(sDate1);
	    Date date6 = formatter1.parse(sDate1);
	    System.out.println("String to Date converter by technolamror");  
	    System.out.println(sDate1+"\t"+date1);
	    System.out.println(sDate2+"\t"+date2);   
	    System.out.println(sDate3+"\t"+date3);   
	    System.out.println(sDate4+"\t"+date4);   
	    System.out.println(sDate5+"\t"+date5);   
	    System.out.println(sDate6+"\t"+date6);  
	}
}
String to Date converter by technolamror
31/12/1998	Sat Jan 31 00:01:00 IST 1998
31-Dec-1998	Sat Jan 31 00:01:00 IST 1998
12 31, 1998	Sat Jan 31 00:01:00 IST 1998
Thu, Dec 31 1998	Sat Jan 31 00:01:00 IST 1998
Thu, Dec 31 1998 23:37:50	Sat Jan 31 00:01:00 IST 1998
31-Dec-1998 23:37:50	Sat Jan 31 00:01:00 IST 1998
********************************************************************************************
package com.basic;
public class HashSetDemo {
	public static void main(String[] args) throws Exception {
		String s = "32.6";
		String s1="9990449935";
		int i = 200;
		String s2 = "200";
		System.out.println(Integer.parseInt(s2));
		System.out.println(Integer.parseInt(s2)+200);
		System.out.println(String.valueOf(i));
		System.out.println(i+100);
		System.out.println(String.valueOf(i)+100);
		System.out.println(Double.parseDouble(s));
		System.out.println(Float.parseFloat(s));
		System.out.println(Long.parseLong(s1));		
	}
}
200
400
200
300
200100
32.6
32.6
9990449935
********************************************************************************************
package com.basic;
import java.io.*;
import java.net.*;
import java.net.InetAddress;
public class HashSetDemo {
	public static void main(String[] args) throws Exception {
		try {
		InetAddress ip = InetAddress.getByName("www.google.com");
		System.out.println("Host Name : " + ip.getHostName());
		System.out.println("Ip Address : " + ip.getHostAddress());
		} catch (Exception e) { System.out.println(e);
	 }
   }
}
Host Name : www.google.com
Ip Address : 142.250.182.68
********************************************************************************************
package com.basic;
import java.io.*;
import java.net.*;
import java.net.InetAddress;
public class HashSetDemo {
	public static void main(String[] args) throws Exception {
		try {
			URL url = new URL("http://www.technolamror.com/java");
			System.out.println("Protocol : " +url.getProtocol());
			System.out.println("Host Name : " +url.getHost());
			System.out.println("Port Number : " +url.getPort());
			System.out.println("File Name : " +url.getFile());
		} catch(Exception e) {System.out.print(e);}
   }
}
Protocol : http
Host Name : www.technolamror.com
Port Number : -1
File Name : /java
********************************************************************************************
package com.basic;
import java.io.*;
public class HashSetDemo {
	public static void main(String[] args){
		try {
		FileInputStream fin = new FileInputStream("C:\\Trainings\\abc.txt");
		int i = fin.read();
		System.out.println((char)i);
		fin.close();
		} catch(Exception e) {System.out.println(e);
	 }
   }
}		===> 9
********************************************************************************************
package com.basic;
import java.io.*;
public class HashSetDemo {
	public static void main(String[] args){
		try {
			FileOutputStream fout = new FileOutputStream("C:\\Trainings\\abc.txt");
			fout.write(65);
			fout.close();
			System.out.println("success...");
		} catch(Exception e) {System.out.println(e);	
		}
		try {
		FileInputStream fin = new FileInputStream("C:\\Trainings\\abc.txt");
		int i = fin.read();
		System.out.println((char)i);
		fin.close();
		} catch(Exception e) {System.out.println(e);
	 }
   }
}
success...
A
********************************************************************************************
package com.basic;
public class HashSetDemo extends Thread{
	public void run(){
		for (int i=0; i<=3; i++) {
			try {
				Thread.sleep(500);
			} catch(Exception e) {System.out.println(e);}
		}
	}
	public static void main(String[] args){	
		HashSetDemo t1 = new HashSetDemo();
		HashSetDemo t2 = new HashSetDemo();
		HashSetDemo t3 = new HashSetDemo();
		t1.start();
		try {
			t1.join();
		} catch(Exception e) {System.out.println(e);}
		t2.start();
		t3.start();
   }
}
********************************************************************************************
package com.basic;
public class HashSetDemo extends Thread{
	public void run(){
		System.out.println("Thread running ...");
	   }
	public static void main(String[] args){	
		HashSetDemo t1 = new HashSetDemo();
		t1.start();
   }
}	===> Thread running ...
********************************************************************************************
package com.basic;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class HashSetDemo extends Thread{
	public static void main(String[] args){	
		Pattern p = Pattern.compile(".s");
		Matcher m = p.matcher("as");
		boolean b1 = m.matches();
		boolean b2 = Pattern.compile(".s").matcher("as").matches();
		boolean b3 = Pattern.matches(".s", "as");
		System.out.print(b1+" "+b2+" "+b3);
   }
}	==>	true true true
********************************************************************************************
package com.basic;
import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
public class HashSetDemo extends Thread{
	public static void main(String[] args){	
		try{   
			//step1 load the driver class   
			Class.forName("oracle.jdbc.driver.OracleDriver");   
			//step2 create  the connection object  
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");   
			//step3 create the statement object   
			Statement stmt=con.createStatement();   
			//step4 execute query   
			ResultSet rs=stmt.executeQuery("select * from emp");   
			while(rs.next())   
			System.out.println(rs.getInt(1)+"  "+rs.getString(2)+"  "+rs.getString(3));   
			//step5 close the connection object   
			con.close();   
			}catch(Exception e){ System.out.println(e);}   
			}   
			} 
java.lang.ClassNotFoundException: oracle.jdbc.driver.OracleDriver
********************************************************************************************
package com.basic;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
public class HashSetDemo extends Thread{
	public static void main(String[] args){	
		try{   
			Class.forName("oracle.jdbc.driver.OracleDriver");   
			Connection 
			con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");   
			PreparedStatement stmt=con.prepareStatement("insert into Emp values(?,?)");   
			stmt.setInt(1,101);//1 specifies the first parameter in the query   
			stmt.setString(2,"Ratan");   
			int i=stmt.executeUpdate();   
			System.out.println(i+" records inserted");   
			con.close();   
			}catch(Exception e){ System.out.println(e);}   
			}   
			}   
java.lang.ClassNotFoundException: oracle.jdbc.driver.OracleDriver
********************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		String string, sub; 
	     int i, c, length; 
	     Scanner in = new Scanner(System.in); 
	     System.out.println("Enter a string to print it's all substrings : "); 
	     string  = in.nextLine();  
	     length = string.length(); 
		 System.out.println("Substrings of \""+string+"\" are :- "); 
		 for( c = 0 ; c < length ; c++ ) 
		 { 
			 for( i = 1 ; i <= length - c ; i++ ) 
			 { 
				 sub = string.substring(c, c+i); 
				 System.out.print(sub + " "); 
			 } 
		 } 
	} 
}
Enter a string to print it's all substrings : 
substring
Substrings of "substring" are :- 
s su sub subs subst substr substri substrin substring u ub ubs ubst ubstr ubstri ubstrin ubstring b bs bst bstr bstri bstrin bstring s st str stri strin string t tr tri trin tring r ri rin ring i in ing n ng g 
********************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		String original, reverse = ""; 
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter string : ");
		original = sc.nextLine();
		int len = original.length();
		for (int i=len-1; i>=0; i--)
			reverse = reverse + original.charAt(i);
		System.out.println("Reversed string is : " + reverse);
		StringBuffer sb = new StringBuffer("Java is a fun");
		System.out.println("Reversed string is : " + sb.reverse());
	} 
}
Enter string : Java Programming
Reversed string is : gnimmargorP avaJ
Reversed string is : nuf a si avaJ
********************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		String inputString;
		Scanner in = new Scanner(System.in);
		System.out.print("Enter string : ");
		inputString = in.nextLine();
		int len = inputString.length();
		int i, begin, end, middle;
		begin = 0;
		end = len - 1;
		middle = (begin + end)/2;
		for (i=begin; i<=middle; i++) {
			if (inputString.charAt(begin) == inputString.charAt(end)) {
				begin++;
				end --;
				
			} else
				break;
		}
		if (i==middle + 1)
			 System.out.println("Palindrome");
		else
			 System.out.println("Not Palindrome");
	}
}
Enter string : Java
Not Palindrome
Enter string : malayalam
Palindrome
********************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Main {
	public static void main(String []args) { 
		int c, first, last, middle, n, search, array[]; 
		Scanner in = new Scanner(System.in); 
		System.out.println("Enter number of elements"); 
		n = in.nextInt();  
		array = new int[n]; 
		System.out.println("Enter " + n + " integers"); 
		for (c = 0; c < n; c++) 
		array[c] = in.nextInt(); 
		System.out.println("Enter value to find"); 
		search = in.nextInt(); 
		first  = 0; 
		last  = n - 1; 
		middle = (first + last)/2; 
		while( first <= last ) 
		{ 
		if ( array[middle] < search ) 
		first = middle + 1;     
		else if ( array[middle] == search )  
		{ 
		System.out.println(search + " found at location " + (middle + 1) + 
		"."); 
		break; 
		} 
		else 
		last = middle - 1; 
		middle = (first + last)/2; 
		} 
		if ( first > last ) 
		System.out.println(search + " is not present in the list.\n"); 
	}
}
Enter number of elements
5
Enter 5 integers
4
3
8
9
0
Enter value to find
8
8 found at location 3.
********************************************************************************************
package com.tryPrograms;
import java.util.Scanner;
public class Main {
	public static void main(String []args) { 
		 int c, n, search, array[]; 
		  
		    Scanner in = new Scanner(System.in); 
		    System.out.println("Enter number of elements"); 
		    n = in.nextInt();  
		    array = new int[n]; 
		  
		    System.out.println("Enter " + n + " integers"); 
		  
		    for (c = 0; c < n; c++) 
		      array[c] = in.nextInt(); 
		  
		    System.out.println("Enter value to find"); 
		    search = in.nextInt(); 
		  
		    for (c = 0; c < n; c++) 
		    { 
		      if (array[c] == search)     /* Searching element is present */ 
		      { 
		         System.out.println(search + " is present at location " + (c + 1) + "."); 
		          break; 
		      } 
		      if (c == n)  /* Searching element is absent */ 
		      System.out.println(search + " is not present in array."); 
	}
}
}
Enter number of elements
5
Enter 5 integers
3
4
5
6
78
Enter value to find
78
78 is present at location 5.
********************************************************************************************
package com.tryPrograms;
import java.io.IOException;
public class Main {
	public static void main(String []args) { 
		 Runtime rs = Runtime.getRuntime();
		 try {
			 rs.exec("notepad");
		 } catch(IOException e) {
			 System.out.print(e);
		 }
	}
}
********************************************************************************************
package com.tryPrograms;
import java.net.InetAddress;
import java.net.*;

public class Main {
	public static void main(String []args) throws Exception { 
		 Runtime rs = Runtime.getRuntime();
		 System.out.println("Free memory in JVM before Garbage Collection = "+rs.freeMemory());
		 rs.gc();
		 System.out.println("Free memory in JVM after Garbage Collection = "+rs.freeMemory());
		 System.out.println(InetAddress.getLocalHost());
	}
}
Free memory in JVM before Garbage Collection = 110476936
Free memory in JVM after Garbage Collection = 9640304
Vaishali/192.168.0.102
********************************************************************************************
package com.tryPrograms;
import java.util.Random;
public class Main {
	public static void main(String []args) throws Exception { 
		 Random t = new Random();
		 for (int c=1; c<=5; c++)
			 System.out.println(t.nextInt(100));
	}
}
9
9
69
85
66
********************************************************************************************

********************************************************************************************
********************************************************************************************
********************************************************************************************
