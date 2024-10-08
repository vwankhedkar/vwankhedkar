*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
ScrollingTest
    open browser    https://testautomationpractice.blogspot.com/   firefox
    maximize browser window
    # execute javascript  window.scrollTo(0, 1500) # scroll with pixelsize
    # scroll element into view    xpath://*[@id="HTML1"]/h2
    execute javascript  window.scrollTo(0,document.body.scrollHeight)  #end of page
    sleep   5ac
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #start of page

*********************************************************************************************
ForLoop

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
#ForLoop1
    #FOR    ${i}    IN RANGE    1    10
    #    Log To Console    ${i}
    #END

#ForLoop2
#    FOR    ${i}    IN    1 2 3 4 5 6 7 8 9
#        Log To Console    ${i}
#    END

#ForLoop3
#    @{items}    Create List    1 2 3 4 5
#    FOR    ${i}    IN    @{items}
#        Log To Console    ${i}
#    END

#ForLoop4
#    FOR    ${i}    IN    ABC XYZ PQR LMN DEF
#        Log To Console    ${i}
#    END

#ForLoop5
#    @{namelist}     create list     ABC XYZ PQR LMN DEF
#    FOR    ${i}    IN   @{namelist}
#        Log To Console    ${i}
#    END

#ForLoop5
#    @{namelist}     create list     ABC XYZ PQR LMN DEF
#    FOR    ${i}    IN   @{namelist}
#        Log To Console    ${i}
#    END

ForLoop6
    @{items}    Create List    1    2    3    4    5    6
    FOR    ${i}    IN    @{items}
        Log To Console    ${i}
        Exit For Loop If    ${i} == 3
    END

