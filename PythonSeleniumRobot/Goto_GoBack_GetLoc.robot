*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
MultipleBrowsers
    open browser    https://www.google.com     firefox
    maximize browser window
    ${loc1}  get location
    log to console  ${loc1}
    sleep   3

    open browser    https://www.bing.com     firefox
    maximize browser window
    ${loc2}     get location
    log to console  ${loc2}
    sleep   3

    go to   https://www.bing.com
    ${loc}  get location
    log to console  ${loc}
    sleep   3

    go back
    ${loc}  get location
    log to console  ${loc}
    sleep   3

