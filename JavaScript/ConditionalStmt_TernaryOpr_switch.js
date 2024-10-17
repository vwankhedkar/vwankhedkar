let num1 = 3;
let num2 = 4;
let result = num1 > num2;
if (result)
    console.log("num1 is greater than num2");
else
    console.log("num2 is greater than num1");
console.log("Bye ...");

OUTPUT -
num2 is greater than num1
Bye ...
*********************************************
  
let num1 = 6;
let num2 = 4;
let result = num1 > num2;
if (result){
    console.log("num1 is greater than num2");
}
else {
    console.log("num2 is greater than num1");
    console.log("Yeeeee");
}
console.log("Bye ...");
OUTPUT 
num1 is greater than num2
Bye ...
*************************************************
let num1 = 10;
let num2 = 9;
let num3 = 7;

if (num1 > num2 && num1 > num3){
    console.log("num1 is greatest");
}
else if(num2 > num3) {
    console.log("num2 is greatest");
}
else {
    console.log("num3 is greatest");
}
console.log("Bye ...");
OUTPUT -
num1 is greatest
Bye ...
**********************************************************
let num = 7;
let result
// if (num % 2 === 0)
//     result = "Even"
// else
//     result = "Odd"
// console.log(result);

result = num % 2 === 0 ? "Even" : "Odd"
console.log(result);
OUTPUT -   Odd
**************************************************************

let day = "Monday"

switch(day) {
    case 'Monday':
        console.log("7am");
        break;
    case 'Tuesday':
    case 'Wednesday':
    case 'Thursday':
        console.log("4am");
        break;
    case 'Friday':
        console.log("9am");
        break;
    case 'Saturday':
    case 'Sunday':
        console.log("10am");
        break;
    default:
        console.log("Watch TV")
}
console.log("Bye...");

OUTPUT -
7am
Bye...
