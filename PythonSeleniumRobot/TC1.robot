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


*** Keywords ***
