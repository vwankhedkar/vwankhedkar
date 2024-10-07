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

