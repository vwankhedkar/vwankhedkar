package com.WebTesting;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) {
		//configure your browser
		//System.setProperty("webdriver.chrome.driver", "C:\\Users\\Azar. A.R\\eclipse-workspace\\SCalss1\\Drivers\\chromedriver.exe");
		//Instantiate for webdrivers
		WebDriver d=new ChromeDriver();
		//to maximize browser
		d.manage().window().maximize();
		//to launch given url
		d.get("https://www.facebook.com");
		//to get the title of the webpage launched
		String title = d.getTitle();
		System.out.println(title);
		//to get the url of the current page
		String url = d.getCurrentUrl();
		System.out.println(url);
		//to quit the browser
		d.quit();
	}
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) {
		//Instantiate for webdrivers
		WebDriver d=new ChromeDriver();
		//to maximize browser
		d.manage().window().maximize();
		//to launch given url
		d.get("https://www.facebook.com");
		//to get the title of the webpage launched
		String title = d.getTitle();
		System.out.println("Title is:"+ title);
		//to get the url of the current page
		String url = d.getCurrentUrl();
		System.out.println("URL is: "+ url);
		//to quit the browser
		d.quit();
	}
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) {
		WebDriver driver=new ChromeDriver();
		driver.get("https://www.facebook.com/");
		//to find locator of the user name
		WebElement txtUserName = driver.findElement(By.id("email"));
		//to pass values in the text box
		txtUserName.sendKeys("azarara321@gmail.com");
		//to find locator of the password field
		WebElement txtPassword = driver.findElement(By.name("pass"));
		txtPassword.sendKeys("123456789");
		//to find locator of login button
		WebElement btnLogin = driver.findElement(By.className("login"));
		//to click button
		btnLogin.click();
	}
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) {
		WebDriver driver=new ChromeDriver();
		driver.get("https://demo.automationtesting.in/Register.html");
		WebElement txtMail = driver.findElement(By.xpath("//input[@type='email']"));
		txtMail.sendKeys("abc@gmail.com");
		WebElement txtFst = driver.findElement(By.xpath("(//input[@type='text'])[1]"));
		txtFst.sendKeys("azar");
		WebElement txtLst = driver.findElement(By.xpath("(//input[@type='text'])[2]"));
		txtLst.sendKeys("AR");
	}
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) {
		WebDriver driver=new ChromeDriver();
		driver.get("https://www.facebook.com/");
		WebElement txtMail = driver.findElement(By.id("email"));
		txtMail.sendKeys("azarara321@gmail.com");
		String mail = txtMail.getAttribute("value");
		System.out.println(mail);
	}
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://greenstech.in/selenium-course-content.html");
		WebElement txtAdd = driver.findElement(By.xpath("//h6[contains(text(),'Greens')]"));
		String text = txtAdd.getText();
		System.out.println(text);
		WebElement txtAdd1 = driver.findElement(By.xpath("//p[@class='mail-info']"));
		String text2 = txtAdd1.getText();
		System.out.println(text2);
	}
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
public class Sample {
	public static void main(String[] args) throws InterruptedException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		Actions a = new Actions(driver);
		driver.get("https://www.shopclues.com/wholesale.html");
    // To move mouse point
		WebElement sport = driver.findElement(By.xpath("//a[text()='Sports & More']"));
		a.moveToElement(sport).perform();
		Thread.sleep(3000);
		WebElement weight = driver.findElement(By.xpath("//a[text()='Weight Gainers']"));
		weight.click();
	}
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
public class Sample {
	public static void main(String[] args) throws InterruptedException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://demo.guru99.com/test/drag_drop.html");
		Actions ac = new Actions(driver);
		WebElement sour = driver.findElement(By.xpath("//a[text()=' BANK ']"));
		WebElement dest = driver.findElement(By.xpath("(//li[@class='placeholder'])[1]"));
		ac.dragAndDrop(sour, dest).perform();
		Thread.sleep(3000);
		WebElement sour2 = driver.findElement(By.xpath("//a[text()=' 5000 ']"));
		WebElement dest2 = driver.findElement(By.id("amt7"));	
		ac.dragAndDrop(sour2, dest2).perform();
	}
}
***************************************************************************************
package com.WebTesting;
import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
public class Sample {
	public static void main(String[] args) throws AWTException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://www.greenstechnologys.com/");
		Actions a = new Actions(driver);
		Robot r = new Robot();
		WebElement paragraph = driver.findElement(By.xpath("//p[@style=\"text-align: center;float:left;font-size: 18px;padding-left:20%;padding-top: 12px;\"]"));
		// doubleClick action
    a.doubleClick(paragraph).perform();
    // rightClick in action
		a.contextClick(paragraph).perform();
    // For using down key
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
    // For using Enter key
		r.keyPress(KeyEvent.VK_ENTER);
		r.keyRelease(KeyEvent.VK_ENTER);
	}
}
***************************************************************************************
package com.WebTesting;
import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) throws AWTException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("http://demo.automationtesting.in/Alerts.html");
		driver.findElement(By.xpath("//button[@class=\"btn btn-danger\"]")).click();
		// Switching into simple alert
		Alert a = driver.switchTo().alert();
		a.accept(); // accept alert
	}
}
***************************************************************************************
package com.WebTesting;
import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) throws AWTException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("http://demo.automationtesting.in/Alerts.html");
		driver.findElement(By.xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a")).click();
		driver.findElement(By.xpath("//*[@id='CancelTab']/button")).click();
		// Switching into simple alert
		Alert a = driver.switchTo().alert();
		a.accept(); // accept alert
	}  
}
***************************************************************************************
package com.WebTesting;
import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) throws AWTException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("http://demo.automationtesting.in/Alerts.html");
		driver.findElement(By.xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a")).click();
		driver.findElement(By.xpath("//*[@id=\"Textbox\"]/button")).click();
		// Switching into simple alert
		Alert a = driver.switchTo().alert();
		a.sendKeys("Azar");
		a.accept(); // accept alert
	}  
}
***************************************************************************************
package com.WebTesting;
import java.awt.AWTException;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) throws AWTException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://www.facebook.com");
		JavascriptExecutor js = (JavascriptExecutor)driver;
		WebElement txtEmail = driver.findElement(By.id("email"));
		js.executeScript("arguments[0].setAttribute('value','azerara321@gmail.com')", txtEmail);
		Object object = js.executeScript("return arguments[0].getAttribute('value')", txtEmail);
		String s1 = (String)object;
		System.out.println(s1);
		WebElement txtPass = driver.findElement(By.id("pass"));
		js.executeScript("arguments[0].setAttribute('value','12345')", txtPass);
		WebElement btnLogin = driver.findElement(By.name("login"));
		js.executeScript("arguments[0].click", btnLogin);
	}  
}
***************************************************************************************
package com.WebTesting;
import java.awt.AWTException;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) throws AWTException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		JavascriptExecutor js = (JavascriptExecutor)driver;
		driver.get("http://toolsqa.com");
		WebElement txtScroll = driver.findElement(By.xpath("//div[text()='Selenium Online Trainings']"));
		// Scroll up
		js.executeScript("arguments[0].scrollIntoView(false)", txtScroll);
		// scroll down
		js.executeScript("arguments[0].scrollIntoView(true)", txtScroll);
	}  
}
***************************************************************************************
package com.WebTesting;
import java.io.IOException;
import java.io.File;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.apache.commons.io.FileUtils;
import com.Excel.TakeScreenshot;

public class Sample {
	public static void main(String[] args) throws IOException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("http://www.greenstechnology.com/");
        // Take screenshot
        File src = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
        File dest = new File("C:\\Java-Selenium-Train\\eclipse-workspace\\SeleniumMaven1\\src\\test\\java\\com\\WebTesting\\Sample.png");
        FileUtils.copyFile(src, dest);
	}  
}
***************************************************************************************
package com.WebTesting;
import java.io.IOException;
import java.io.File;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.apache.commons.io.FileUtils;
import com.Excel.TakeScreenshot;
public class Sample {
	public static void main(String[] args) throws InterruptedException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("http://www.facebook.com");
		WebElement btnLogin = driver.findElement(By.name("login"));
		boolean displayed = btnLogin.isDisplayed();
		System.out.println(displayed);
		WebElement btnCreate = driver.findElement(By.xpath("//a[text()='Create new account']"));
		btnCreate.click();
		Thread.sleep(3000);
		WebElement rdoGender = driver.findElement(By.name("sex"));
		rdoGender.click();
		boolean selected2 = rdoGender.isSelected();
		System.out.println(selected2);
	}  
}
***************************************************************************************
package com.WebTesting;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class Sample {
	public static void main(String[] args) throws InterruptedException {
		WebDriver driver=new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://netbanking.hdfcbank.com/netbanking/");
		driver.switchTo().frame("login_page");
		Thread.sleep(2000);
		WebElement login = driver.findElement(By.cssSelector("a.btn.btn-primary.login-btn"));
		login.click();
		driver.switchTo().defaultContent();
	}  
}
***************************************************************************************

***************************************************************************************
***************************************************************************************

***************************************************************************************
***************************************************************************************

***************************************************************************************
