*** Settings ***
Library    DatabaseLibrary
Library    OperatingSystem

Suite Setup    Connect To Database    pymysql    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
Suite Teardown    Disconnect From All Connections

*** Variables ***
${DBName}    mydb
${DBUser}    root
${DBPass}    root
${DBHost}    127.0.0.1
${DBPort}    3306

*** Test Cases ***
Create Person Table
    ${output}=    Execute SQL String    CREATE TABLE person (id INTEGER, first_name VARCHAR(20), last_name VARCHAR(20))
    Log To Console    ${output}
    Should Be Equal As Strings    ${output}    None

Inserting Data In Person Table
    ${output}=    Execute SQL String    INSERT INTO person VALUES (101, 'John', 'Canady')
    Log To Console    ${output}
    Should Be Equal As Strings    ${output}    None

    # multiple records
    ${output}=    Execute SQL Strict    ./TestData/mydb_person_insertData.sql
    Log To Console    ${output}
    Should Be Equal As strings    ${output}    None

Check David record present in Person Table
    check if exists in database select if from mydb.person where first_name="David";

Check Joe record Not present in Person Table
    check if not exists in database select id from mydb.person where first_name="Joe";

Check Person Table exists in mydb database
    table must exist person

Verify Row Count is Zero
    row count is 0 SELECT * FROM mydb.person WHERE first_name='xyz';

Verify Row Count is Equal to Some Value
    row count is equal to x SELECT * FROM mydb.person WHERE first_name = 'David';  1

Verify Row Count is Greater than Some Value
    row count is greater than x SELECT * FROM mydb.person WHERE first_name = 'David';   0

Verify Row Count is less than Some Value
    row count is less than x SELECT * FROM mydb.person WHERE first_name = 'David';  5

Update record in person table
    ${output}=  Execute SQL String  Update mydb.person set first_name='Joe' where id=104;
    log to console ${output}
    should be equal as strings  ${output}   None

Retrieve records from Person Table
    @{queryResults}=    query Select * from mydb.person;
    log to console  many @{queryResults}

Delete Records from person table
    ${output}=  Execute SQL String  Delete from mydb.person;
    should be equal as strings  ${output}   None

    
