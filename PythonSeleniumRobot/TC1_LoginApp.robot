*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Test Cases ***
LoginTest
    open browser    https://demo.nopcommerce.com/   chrome
    click link    xpath:<a href="/login?returnUrl=%2F" class="ico-login">Log in</a>
    input text    id:Email vwankhedkar@gmail.com
    input text    id:Password   Test123
    click element    xpath://*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button
            ----- ***** ------

*** Settings ***
Library  SeleniumLibrary

*** Variables  ***
${brower}  firefox
${url}  https://demo.nopcommerce.com/

*** test cases ***
LoginTest
    open browser    ${url}  ${browser}
    loginToApplication
    close browser
    
*** keywords ***
loginToApplication
    click link  xpath://a[@class='ico-Login']
    input text  id:Email    abc@gmail.com
    input text  id:Password  Test@123
    click element xpath://input[@class='button-1 Login-button']\

        ------------ *** -------------------

*** Settings ***
Library  SeleniumLibrary

*** Variables  ***
${brower}  firefox
${url}  https://demo.nopCommerce.com/

*** test cases ***
    open browser    ${url}  ${browser}
    maximize browser window
    title should be nopCommerce demo store
    click link xpath://a[@class='ico-Login']
    ${"email_txt"}  set variable    id:Email
    
    element should be visible   ${"email_txt"}
    element should be enabled   ${"email_txt"}

    input text  ${"email_txt"}  abc@gmail.com
    sleep   5
    clear element text  ${"email_txt"}
    sleep   3
    close browser

*** keywords ***
loginToApplication
    click link  xpath://a[@class='ico-Login']
    input text  id:Email    abc@gmail.com
    input text  id:Password  Test@123
    click element xpath://input[@class='button-1 Login-button']\


*** Keywords ***
