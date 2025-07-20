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
