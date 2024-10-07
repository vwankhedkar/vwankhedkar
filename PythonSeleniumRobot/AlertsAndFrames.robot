*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
MyTestCase
    Open Browser    https://testautomationpractice.blogspot.com/    firefox
    Maximize Browser Window

    click element   xpath://*[@id="confirmBtn"]
    sleep   3
    #handle alert    accept
    #handle alert    dismiss
    #handle alert    leave
    alert should be present    Press a button!
    #alert should not be present    Press a button!
------------------------------------ ****************** -------------------------------

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
MyTestCase
    Open Browser    https://seleniumhq.github.io/selenium/docs/api/java/index    firefox
    Maximize Browser Window

    select frame    packageListFrame   #id name path
    click link  #link
    unselect frame  #id
    sleep   3

    select frame    packageListFrame1   #id name path
    click link  #link
    unselect frame  #id
    sleep   3
    close browser


