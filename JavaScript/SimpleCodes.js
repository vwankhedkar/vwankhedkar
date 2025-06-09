let num = 10;
let str = "Hello";
let bool = true;
let obj = {};
let func = function() {};
console.log(typeof num);
console.log(typeof str);
console.log(typeof bool);
console.log(typeof obj);
console.log(typeof func);
(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\JavaScript> node .\try.js
number
string
boolean
object
function
*****************************************************************************
let obj1 = {
    value: 42,
    valueOfThis: function() {
        return this.value;
    }
}
console.log(obj1.valueOfThis());    ===>>> 42

const numbers = [1, 2, 3, 4, 5];
const doublednum = numbers.map(number=>number*2);
console.log(doublednum);
const evennum = numbers.filter(number=>number%2);
console.log(evennum);
const sum = numbers.reduce((accumulator,number)=>accumulator+number,0);
console.log(sum)
(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\JavaScript> node .\try.js
[ 2, 4, 6, 8, 10 ]
[ 1, 3, 5 ]
15
*****************************************************************************

*****************************************************************************

*****************************************************************************

*****************************************************************************
