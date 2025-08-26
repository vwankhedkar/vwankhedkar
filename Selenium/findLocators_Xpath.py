
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
//table[@id='customers']//tr//td[contains(text(), 'Canada')]/preceding-sibling::td[1]
Italy
//table[@id='customers']/child::tbody/child::tr[7]/td[3]
//table[@id='customers']//tbody//td[contains(text(), 'Italy')]
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
******************************************************************************
https://www.iplt20.com/points-table/men/2024
//div[@class='ih-pt-ic ']/div//following-sibling::h2
//table[@class="ih-td-tab"]/tbody/tr//following-sibling::h2
