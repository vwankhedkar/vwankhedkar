*** settings ***
Library     SeleniumLibrary

*** variables ***
${browser}  firefox
${url}  https://practiceselenium.com/practice-form.html

*** Test Cases ***
Handling DropDown and Lists
    open browser    ${url}  ${browser}
    maximize browser window

    # Drop Down
    select from list by label   continents Asia
    sleep 3
    select from list by index   continents 6
    #select from list by value continents value

    # List Box
    select from list by label selenium_commands     Switch  Commands
    select from list by label selenium_commands     WebElement Commands
    sleep 3

    unselect from list by label      selenium commands  Switch Commands
    # close browser

