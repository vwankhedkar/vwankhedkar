let nums = [1, 2, 3, 4, 5]
let result = nums.filter( n => n % 2 == 0)
    .map( n => n*2)
    .reduce((a,b) => a+b);
console.log(result)

OUTPUT : 12
****************************************************
function removeDuplicates(arr) {
    return arr.filter((item, index) => arr.indexOf(item) == index);
}
const numbers = [1, 2, 2, 3, 4, 4, 5];
console.log(removeDuplicates(numbers));
[ 1, 2, 3, 4, 5 ]
********************************************************************
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
console.log([...array1, ...array2]);
console.log(array1.concat(array2));
[ 1, 2, 3, 4, 5, 6 ]
[ 1, 2, 3, 4, 5, 6 ]
********************************************************************
function flattenArray(arr) {
return arr.reduce(
(acc, item) =>
Array.isArray(item) ? acc.concat(flattenArray(item)) : acc.concat(item),
[]
);
}
const nestedArray = [1, [2, [3, 4], 5], 6];
console.log(flattenArray(nestedArray));
[ 1, 2, 3, 4, 5, 6 ]
********************************************************************
const arr = [15, 7, 20, 3, 45];
function findSecondLargest(arr) {
let largest = -Infinity;
let secondLargest = -Infinity;

for (let num of arr) {
if (num > largest) {
secondLargest = largest;
largest = num;
} else if (num > secondLargest && num < largest) {
secondLargest = num;
 }
}
 return secondLargest === -Infinity ? null : secondLargest;
}
const numbers = [12, 35, 1, 10, 34, 1];
console.log(findSecondLargest(numbers)); `==>    34
********************************************************************

********************************************************************
********************************************************************

********************************************************************
********************************************************************

********************************************************************
********************************************************************

********************************************************************
********************************************************************

********************************************************************
