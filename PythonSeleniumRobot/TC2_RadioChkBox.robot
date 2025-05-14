*** Settings ***
Library  SeleniumLibrary

*** variables ***
${browser}  firefox
${url}  https://https://practiceselenium.com/practice-form.html

*** test cases ***
    open browser    ${url}  ${browser}
    maximize browser window
    select radio button sex female
    select radio button exp 5
    close browser

*** Settings ***
Library  SeleniumLibrary

*** variables ***
${browser}  firefox
${url}  https://practiceselenium.com/practice-form.html

*** test cases ***
Testing Radio Buttons and Check Boxes
    open browser    ${url}  ${browser}
    maximize browser window
    set selenium speed 2seconds

    # Selecting Radio buttons
    select radio button sex female
    select radio button exp 5

    # Selecting Check Box
    select checkbox BlackTea
    select checkbox RedTea

    unselect checkbox BlackTea
    close browser
*******************************************************************
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}          https://demoqa.com/automation-practice-form

*** Test Cases ***
TestingInputBox
    Open Browser    ${url}      ${browser}
    Maximize Browser Window
   # Click Element    xpath://*[@id="close-button-id"]
    #Scroll Element Into View    id:gender-radio-2
    #Click Element               id:gender-radio-2
    Scroll Element Into View    id:gender-radio-2
    Execute JavaScript    document.getElementById("gender-radio-2").click()
    Scroll Element Into View    id:hobbies-checkbox-1
    Execute JavaScript    document.getElementById("hobbies-checkbox-1").click()
    Execute JavaScript    document.getElementById("hobbies-checkbox-1").checked = false
