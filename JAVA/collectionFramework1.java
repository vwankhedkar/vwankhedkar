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
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
********************************************************************************************
