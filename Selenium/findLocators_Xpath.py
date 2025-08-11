
page -> https://www.hyrtutorials.com/p/add-padding-to-containers.html#google_vignette

Firstname text box
//input[@name='name']/preceding-sibling::input[1]
Email
//label[text()='Email']/following-sibling::input[1]
//label[text()='Email']/following-sibling::input[1]/parent::div
password textbox
//label[text()='Password']/following::input[1]
tablename checkbox
//td[text()='Maria Anders']/preceding-sibling::td/child::input
Canada
//td[text()='Yoshi Tannamuri']/following-sibling::td[1]
Get 3rd row values
//table[@id='contactList']/child::tbody/tr[4]/child::td
Austria
//table[@id='contactList']/child::tbody/tr[4]/child::td[3]
All textboxes
//div[@class='container']/child::input[@type='text']
//div[@class='container']/child::input[@type='text'][1]
All buttons
//div[@class='container']/descendant::button
whole frame boxes
//div[@class='buttons']/ancestor-or-self::div
