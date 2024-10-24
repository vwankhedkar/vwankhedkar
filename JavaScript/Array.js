let data = [5,7,8,9];
console.log(data.push(3));
console.log(data);
console.log(data.pop());
console.log(data);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
5
[ 5, 7, 8, 9, 3 ]
3
[ 5, 7, 8, 9 ]
***********************************************************************
let data = [5,7,8,9];
console.log(data.shift());
console.log(data);
console.log(data.unshift(9));
console.log(data);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
5
[ 7, 8, 9 ]
4
[ 9, 7, 8, 9 ]
*****************************************************************
let data = [5,7,8,9,4];
console.log(data.splice(2));
console.log(data);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
[ 8, 9, 4 ]
[ 5, 7 ]
******************************************************************
let data = [5,7,8,9,4];
console.log(data.splice(2, 1));
console.log(data);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
[ 8 ]
[ 5, 7, 9, 4 ]
********************************************************************
let data = [5,7,8,9,4];
console.log(data.splice(2, 2, 11, 15));
console.log(data);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
[ 8, 9 ]
[ 5, 7, 11, 15, 4 ]
*********************************************************************
let nums = [];
nums[0] = 5;
nums[5] = 9;
for(let n of nums){
    console.log(n);
}
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
5
undefined
undefined
undefined
undefined
9

let nums = [];
nums[0] = 5;
nums[5] = 9;
for(let key in nums){
    console.log(nums[key]);
}
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
5
9
********************************************************************
let nums = [5,4,7,8]
console.log(nums);
let [a,b,,d] = nums;
console.log(d);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
[ 5, 4, 7, 8 ]
8
*******************************************************************
let a = 5;
let b = 6;
[a, b] = [b, a];
console.log(a, b)
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
6 5
******************************************************************

