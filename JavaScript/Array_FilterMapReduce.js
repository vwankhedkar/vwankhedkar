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
function findSecondLargest(arr) {
    const uniqArr = [...new Set(arr)];
    if (uniqArr.length<2) return null;
    uniqArr.sort((a,b) => b-a);
    return uniqArr[1];
}
const numbers = [12, 35, 1, 10, 34, 34, , 35, 1];
console.log(findSecondLargest(numbers));    ==> 34
********************************************************************
function countOccurrences(arr) {
const counts = {};
arr.forEach((item) => {
counts[item] = (counts[item] || 0) + 1;
});
return counts;
}
const fruits = ["apple", "banana", "apple", "orange", "banana","grape"];
console.log(countOccurrences(fruits));
{ apple: 2, banana: 2, orange: 1, grape: 1 }
********************************************************************
function rotateArray(arr, n) {
    const length = arr.length;
    n = n % length;
    arr.push(...arr.splice(0, n));
    return arr;
}
// using array reversal method
function reverse(arr, start, end) {
    while (start < end) {
        [arr[start], arr[end]] = [arr[end], arr[start]];
        start++;
        end--;
    }
   return arr;
}
function rotateArray1(arr, n) {
    const length = arr.length;
    n = n % length;
    reverse(arr, 0, n - 1);
    reverse(arr, n, length - 1);
    reverse(arr, 0, length - 1);
    return arr;
}
const array = [1, 2, 3, 4, 5];
console.log(rotateArray(array,2));
const array1 = [1, 2, 3, 4, 5];
console.log(rotateArray1(array1,3));
[ 3, 4, 5, 1, 2 ]
[ 4, 5, 1, 2, 3 ]
********************************************************************
function union(arr1, arr2) {
    return [...new Set([...arr1, ...arr2])];
}
function union1(arr1, arr2) {
    return arr1
     .concat(arr2)
     .filter((item,index,array) => array.indexOf(item) === index);
}
const a = [1, 2, 3];
const b = [3, 4, 5];
console.log(union(a, b));
console.log(union1(a, b));
[ 1, 2, 3, 4, 5 ]
[ 1, 2, 3, 4, 5 ]
********************************************************************
function getIntersection(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
    const intersection = [];
    for (let item of arr2) {
        if (set1.has(item))
            intersection.push(item);
    }
    return intersection;
}
const a = [1, 2, 3, 3, 4];
const b = [3, 4, 5, 6, 6, 7];
console.log(getIntersection(a, b));    ===>    [ 3, 4 ]
********************************************************************
function getIntersection(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
    const intersection = [];
    for (let item of arr2) {
        if (set1.has(item))
            intersection.push(item);
    }
    return intersection;
}
function getIntersection1(arr1, arr2) {
    arr = arr1.filter((item) => arr2.includes(item));
    const set = new Set(arr);
    return set;
}
const a = [1, 2, 3, 3, 4];
const b = [3, 4, 5, 6, 6, 7];
console.log(getIntersection(a, b));
console.log(getIntersection1(a, b));
[ 3, 4 ]
Set(2) { 3, 4 }
********************************************************************
********************************************************************

********************************************************************
********************************************************************

********************************************************************
