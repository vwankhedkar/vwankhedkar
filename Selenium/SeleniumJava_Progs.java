package com.PractiseProgs;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Point;
import org.openqa.selenium.firefox.FirefoxDriver;
public class openHTML {
	public static void main(String[] args) throws InterruptedException {
		FirefoxDriver driver = new FirefoxDriver();
		driver.get("https://www.google.com");
		Thread.sleep(2000);
		Dimension d = new Dimension(200, 200);
		driver.manage().window().setSize(d);
		Thread.sleep(2000);
		Point p = new Point(300,200);
		driver.manage().window().setPosition(p);
		Thread.sleep(2000);
		driver.manage().window().maximize();
		driver.quit();
	}
}
************************************************************************************
package com.PractiseProgs;
import java.util.Scanner;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
public class openHTML {
    public static void main(String[] args) throws InterruptedException {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Browser : GC (Chrome) / FF (Firefox) / ME (Edge): ");
        String browser = sc.next();
        WebDriver driver = null;
        if (browser.equalsIgnoreCase("GC")) {
            driver = new ChromeDriver();
        } else if (browser.equalsIgnoreCase("FF")) {
            driver = new FirefoxDriver();
        } else if (browser.equalsIgnoreCase("ME")) {
            driver = new EdgeDriver();
        } else {
            System.out.println("Invalid browser input. Please enter GC, FF, or ME.");
            System.exit(0);
        }
        driver.get("https://www.google.com");
        Thread.sleep(2000);
        System.out.println("Page Title: " + driver.getTitle());
        System.out.println("Current URL: " + driver.getCurrentUrl());
        driver.manage().window().maximize();
        Thread.sleep(2000);
        driver.quit();
        sc.close();
    }
}
*****************************************************************************
package com.PractiseProgs;
import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils; 
import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.firefox.FirefoxDriver;
public class openHTML {
    public static void main(String[] args) throws InterruptedException, IOException {
    	System.setProperty("webdriver.firefox.profile", "default");
    	FirefoxDriver driver = new FirefoxDriver();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
		driver.get("https://www.amazon.in");
		driver.manage().window().maximize();
		driver.findElement(By.xpath("//span[contains(@id,'nav-link-accountList-nav-line-1')]")).click();
		driver.findElement(By.xpath("//input[@type='email']")).sendKeys("987437837");
		driver.findElement(By.xpath("//input[@class='a-button-input']")).click();
		File srcFile = driver.getScreenshotAs(OutputType.FILE);
		File destFile = new File("C:\\Java-Selenium-Train\\eclipse-workspace\\JavaSelenium\\src\\com\\PractiseProgs\\actTime.png");
		FileUtils.copyFile(srcFile, destFile);
		driver.close();
    }
}
*****************************************************************************
package com.PractiseProgs;
import java.io.IOException;
import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
public class openHTML {
    public static void main(String[] args) throws IOException {
        WebDriver driver = new FirefoxDriver();
        driver.get("https://www.actitime.com/login-to-product");
        driver.findElement(By.id("username")).sendKeys("admin");
        driver.findElement(By.name("pwd")).sendKeys("manager");
        driver.findElement(By.id("loginButton")).click();
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(20));
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("logoutLink")));
        String title = driver.getTitle();
        System.out.println("Page Title: " + title);
        driver.quit();
    }
}
*****************************************************************************
package com.PractiseProgs;
import java.io.IOException;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
public class openHTML {
    public static void main(String[] args) throws IOException {
    	WebDriver driver = new FirefoxDriver();
    	driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
    	driver.get("https://www.facebook.com");
    	driver.manage().window().maximize();
    	System.out.print(driver.getCurrentUrl());
    	WebDriverWait wait = new WebDriverWait(driver,Duration.ofSeconds(10));
    	wait.until(ExpectedConditions.urlContains("facebook"));
    	driver.quit();
    }
}
*****************************************************************************
package com.PractiseProgs;
import java.io.IOException;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
public class openHTML {
    public static void main(String[] args) throws IOException {
    	WebDriver driver = new FirefoxDriver();
    	driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
    	driver.get("https://www.facebook.com");
    	driver.manage().window().maximize();
    	System.out.println(driver.getCurrentUrl());
    	WebDriverWait wait = new WebDriverWait(driver,Duration.ofSeconds(10));
    	wait.until(ExpectedConditions.urlContains("facebook"));
    	WebElement ev = driver.findElement(By.id("email"));
    	ev.sendKeys("abc@gmail.com");
    	String values = ev.getAttribute("value");
    	System.out.println(values);
    	driver.quit();
    }
}
*****************************************************************************
package com.PractiseProgs;
import java.io.IOException;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
public class openHTML {
    public static void main(String[] args) throws IOException {
    	WebDriver driver = new FirefoxDriver();
    	driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
    	driver.get("https://www.facebook.com");
    	driver.manage().window().maximize();
    	System.out.println(driver.getCurrentUrl());
    	WebDriverWait wait = new WebDriverWait(driver,Duration.ofSeconds(10));
    	wait.until(ExpectedConditions.urlContains("facebook"));
    	WebElement ev = driver.findElement(By.id("email"));
    	ev.sendKeys("abc@gmail.com");
    	ev.clear();
    	ev.sendKeys("xyz@gmail.com");
    	String values = ev.getAttribute("value");
    	System.out.println(values);
    	// Change values without clear methood
    	ev.sendKeys(Keys.CONTROL+"a");
    	ev.sendKeys(Keys.DELETE);
    	ev.sendKeys("lmn@gmail.com");
    	driver.quit();
    }
}
*****************************************************************************
With Backspace
package com.PractiseProgs;
import java.io.IOException;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
public class openHTML {
    public static void main(String[] args) throws IOException {
    	WebDriver driver = new FirefoxDriver();
    	driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
    	driver.get("https://www.facebook.com");
    	driver.manage().window().maximize();
    	System.out.println(driver.getCurrentUrl());
    	WebDriverWait wait = new WebDriverWait(driver,Duration.ofSeconds(10));
    	wait.until(ExpectedConditions.urlContains("facebook"));
    	WebElement ev = driver.findElement(By.id("email"));
    	ev.sendKeys("abc@gmail.com");
    	ev.clear();
    	ev.sendKeys("xyz@gmail.com");
    	String values = ev.getAttribute("value");
    	System.out.println(values);
    	int count = values.length();
		for (int i=0; i<=count; i++)
		ev.sendKeys(Keys.BACK_SPACE);
	    driver.quit();
    }
}
*****************************************************************************
copy paste from 1 textbox to other
package com.PractiseProgs;
import java.io.IOException;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
public class openHTML {
    public static void main(String[] args) throws IOException {
    	WebDriver driver = new FirefoxDriver();
    	driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
    	driver.get("https://www.facebook.com");
    	driver.manage().window().maximize();
    	System.out.println(driver.getCurrentUrl());
    	WebDriverWait wait = new WebDriverWait(driver,Duration.ofSeconds(10));
    	wait.until(ExpectedConditions.urlContains("facebook"));
    	WebElement ev = driver.findElement(By.id("email"));
    	ev.sendKeys("abc@gmail.com");
    	ev.sendKeys(Keys.CONTROL+"a");
    	ev.sendKeys(Keys.CONTROL+"c");
	WebElement ev1 = driver.findElement(By.id("pass"));
    	ev1.clear();
    	ev1.sendKeys(Keys.CONTROL+"v");
	    driver.quit();
    }
}
*****************************************************************************
package com.PractiseProgs;
import java.time.Duration; // Recommended for Selenium 4
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.Point; // Correct Point class for WebElement
import org.openqa.selenium.firefox.FirefoxDriver;
public class openHTML {
    public static void main(String[] args) {
        WebDriver driver = new FirefoxDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20));
        driver.get("https://www.facebook.com");
        driver.manage().window().maximize();
        WebElement em = driver.findElement(By.id("email"));
        Point p = em.getLocation(); // Get the x, y coordinates
        System.out.println("X coordinate (in pixels): " + p.getX());
        System.out.println("Y coordinate (in pixels): " + p.getY());
        driver.quit();
    }
}
X coordinate (in pixels): 746
Y coordinate (in pixels): 148
*****************************************************************************
package com.PractiseProgs;
import org.openqa.selenium.By; import 
org.openqa.selenium.Dimension; import 
org.openqa.selenium.Point; import 
org.openqa.selenium.WebDriver; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.firefox.FirefoxDriver; 
public class openHTML { 
public static void main(String[] args) 
{ 
	WebDriver driver=new FirefoxDriver(); 
	driver.get("http://www.facebook.com"); 
	WebElement em=driver.findElement(By.id("email")); 
	Point p1=em.getLocation(); 
	int x1=p1.getX(); 
	System.out.println("X value of email field: "+x1); 
	WebElement nxt=driver.findElement(By.id("pass")); 
	Point p2=nxt.getLocation(); 
	int x2=p2.getX(); 
	System.out.println("X value of next button: "+x2); 
	Dimension s = em.getSize(); 
	System.out.println("Height of the textbox: "+s.getHeight()); 
	System.out.println("Width of the textbox: "+s.getWidth()); 
	if(x2-x1<=0) 
	{ 
		System.out.println("Email textbox and next button aligned  horizontally"); 
	} 
	else 
	{ 
		System.out.println("Not alligned Horizontally"); 
	} 
  } 
}
X value of email field: 746
X value of next button: 762
Height of the textbox: 51
Width of the textbox: 363
Not alligned Horizontally
*****************************************************************************
package com.PractiseProgs;
import org.openqa.selenium.By; import 
org.openqa.selenium.Dimension; import 
org.openqa.selenium.WebDriver; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.firefox.FirefoxDriver; 
public class openHTML { 
	public static void main(String[] args) 
	{ 
		WebDriver driver=new FirefoxDriver(); 
		driver.get("http://www.facebook.com"); 
		WebElement em=driver.findElement(By.id("email")); 
		Dimension s1 = em.getSize(); 
		int w1 = s1.getWidth(); 
		WebElement nxt=driver.findElement(By.id("pass")); 
		Dimension s2=nxt.getSize(); 
		int w2=s2.getWidth(); 
		System.out.println("Width of Email textbox: "+w1); 
		System.out.println("Width of next button: "+w2); 
		if(w1==w2) 
		{ 
			System.out.println("Width of email textbox and next button is same"); 
		} 
		else 
		{ 
			System.out.println("Width of email textbox & next button is not same"); 
		} 
	} 
} 
Width of Email textbox: 363
Width of next button: 300
Width of email textbox & next button is not same
*****************************************************************************
package com.PractiseProgs;

import java.sql.Time;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.RemoteWebDriver;

public class openHTML { 
	public static void main(String[] args) throws InterruptedException 
	{ 
		WebDriver driver=new FirefoxDriver(); 
		driver.get("http://demo.vtiger.com");
		WebElement un = driver.findElement(By.name("username")); 
		System.out.println(un.getCssValue("font-size"));
		System.out.println(un.getCssValue("color")); 
		RemoteWebDriver r= (RemoteWebDriver) driver; 
		String c="document.getElementsByTagName('input').value='admin'"; 
		r.executeScript(c); 
		String xp="//button[@type=\"submit\"]"; 
		WebElement btn = driver.findElement(By.xpath(xp)); 
		btn.sendKeys(Keys.ENTER); 
		driver.quit();
	}
} 
*****************************************************************************
package com.PractiseProgs;

import java.sql.Time;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver; 
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
public class openHTML { 
	public static void main(String[] args) throws InterruptedException 
	{ 
		WebDriver driver=new FirefoxDriver(); 
		driver.get("http://amazon.in");
		WebElement un = driver.findElement(By.xpath("//input[contains(@class,'nav-input nav-progressive-attribute')]")); 
		System.out.println(un.getCssValue("font-size"));
		System.out.println(un.getCssValue("color")); 
		RemoteWebDriver r= (RemoteWebDriver) driver; 
		String c="document.getElementsByClassName('nav-input nav-progressive-attribute').value='laptop'"; 
		r.executeScript(c); 
		Thread.sleep(5000);
		String xp="//input[@placeholder='Search Amazon.in']"; 
		WebElement btn = driver.findElement(By.xpath(xp)); 
		btn.sendKeys(Keys.ENTER); 
		driver.quit();
	}
} 
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
*****************************************************************************
