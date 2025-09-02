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
function removeFalsyValues(arr) {
    return arr.filter(Boolean);
}
function removeFalsyValues1(arr) {
    return arr.filter((item) => item);
}
const array = [0, 1, false, 2, "", 3, null, undefined, NaN];
console.log(removeFalsyValues(array)); 
console.log(removeFalsyValues1(array)); 
[ 1, 2, 3 ]
[ 1, 2, 3 ]
********************************************************************
function shuffle(arr) {
    for (let i=arr.length-1; i>0; i--) {
        const j = Math.floor(Math.random()*(i+1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}
function getShuffle(arr) {
    const newArr = arr.slice();
    for (let i=newArr.length-1; i>0; i--) {
        const j = Math.floor(Math.random()*(i+1));
        [newArr[i], newArr[j]] - [newArr[j], newArr[i]];
    }
    return newArr;
}
const array = [0, 1, 2, 3, 4, 5];
console.log(shuffle(array)); 
console.log(getShuffle(array)); 
[ 4, 2, 5, 1, 3, 0 ]
[ 4, 2, 5, 1, 3, 0 ]
********************************************************************
function sort1(arr) {
    let low = 0,
    mid = 0;
    let high = arr.length - 1;
    while (mid <= high) {
        if (arr[mid] === 0) {
            [arr[low], arr[mid]] = [arr[mid], arr[low]];
            low++;
            mid++;
        } else if (arr[mid] === 1) {
            mid++;
        } else {
            // arr[mid] === 2
            [arr[mid], arr[high]] = [arr[high], arr[mid]];
            high--;
        }
    }
    return arr;
}
function sort2(arr) {
    let count0 = 0,
    count1 = 0,
    count2 = 0;
    for (let num of arr) {
        if (num === 0) count0++;
        else if (num === 1) count1++;
        else count2++;
    }
    let i = 0;
    while (count0--) arr[i++]=0;
    while (count1--) arr[i++]=1;
    while (count2--) arr[i++]=2;
    return arr;
}
const arr = [2, 0, 1, 2, 1, 0, 0, 2];
console.log(sort1([...arr])); 
console.log(sort2([...arr])); 
[
  0, 0, 0, 1,
  1, 2, 2, 2
]
[
  0, 0, 0, 1,
  1, 2, 2, 2
]
********************************************************************
function chunkArray(arr, size) {
    const chunkArr = [];
    for (let i=0; i<arr.length; i+=size) {
        chunkArr.push(arr.slice(i,i+size));
    }
    return chunkArr;
}
const data = [1, 2, 3, 4, 5, 6, 7];
console.log(chunkArray(data, 3)); // [[1,2,3],[4,5,6],[7]]
console.log(chunkArray(data, 2)); // [[1,2],[3,4],[5,6],[7]]
[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7 ] ]
[ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ], [ 7 ] ]
********************************************************************
function maxSubarraySum(arr) {
    let maxSoFar = arr[0];
    let maxHere = arr[0];
    for (let i=0; i<arr.length; i++) {
        maxHere = Math.max(arr[i], maxHere+arr[i]);
        maxSoFar = Math.max(maxSoFar, maxHere);
    }
    return maxSoFar;
}
function maxSubarraySum1(arr) {
    let maxSum = -Infinity;
    for (let i = 0; i < arr.length; i++) {
    let currentSum = 0;
    for (let j = i; j < arr.length; j++) {
    currentSum += arr[j];
    maxSum = Math.max(maxSum, currentSum);
    }
  }
    return maxSum;
}
const arr = [-2, -3, 4, -1, -2, 1, 5, -3];
console.log(maxSubarraySum(arr)); // Output: 7 (for subarray [4, -1, -2, 1, 5]
console.log(maxSubarraySum1(arr));
7
7
********************************************************************
function findPairsWithSet(arr, targetSum) {
    const seen = new Set();
    const pairs = [];
    for (let num of arr) {
        const complement = targetSum - num;
        if (seen.has(complement)) {
            pairs.push([complement, num]);
        }
        seen.add(num);
    }
    return pairs;
}
function findPairsBruteForce(arr, targetSum) {
    const pairs = [];
    for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
    if (arr[i] + arr[j] === targetSum) {
    pairs.push([arr[i], arr[j]]);
            }
        }
    }
    return pairs;
}
const array = [1, 5, 7, -1, 5];
const target = 6;
console.log(findPairsBruteForce(array, target));
console.log(findPairsWithSet(array, target));
[ [ 1, 5 ], [ 1, 5 ], [ 7, -1 ] ]
[ [ 1, 5 ], [ 7, -1 ], [ 1, 5 ] ]
********************************************************************

********************************************************************

********************************************************************

********************************************************************
