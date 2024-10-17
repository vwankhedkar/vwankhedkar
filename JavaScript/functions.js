function greet()
{
    console.log("Hello World!")
}
greet()
console.log("*************") 
greet()
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
Hello World!
*************
Hello World!
*******************************************************
function greet(user)
{
    return `Hello ${user}!!!`
}
let user = 'vaishali'
let str = greet(user)
console.log(str) 
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
Hello vaishali!!!
***************************************************************
let add = function(num1, num2)
{
    return num1 + num2;
}
let sum = add;
let result = sum(5, 6);
console.log(result);
console.log(sum);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
11
[Function: add]
*******************************************************************
  
