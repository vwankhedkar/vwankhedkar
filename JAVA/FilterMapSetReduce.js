let map = new Map();
map.set("Skill", "Python");
map.set("name", "Vaishali");
map.set("address", "Bangalore");
map.set("Skill", "Java")
console.log(map.has("Skill"));
console.log(map.get("Skill"));

map.forEach((v, k) => {
    console.log(k, " : ", v);
}); 
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
true
Java
Skill  :  Java
name  :  Vaishali
address  :  Bangalore
**************************************************************************
let num = new Set();
num.add(3);
num.add(4);
num.add(3);
num.add("Vais");
num.add("Python");
num.add("Java");
console.log(num.has("Java"))
console.log(num.has("python")) // case-sensitive
num.forEach(value => {
    console.log(value);
});
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
true
false
3
4
Vais
Python
Java
*****************************************************************************
let num = new Set("Bookkeepeer");
console.log(num);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
Set(6) { 'B', 'o', 'k', 'e', 'p', 'r' }
*****************************************************************************
let num = [10, 20, 30, 40, 20]
num.forEach((n, i, num) => {
    console.log(n, i, num)
});
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
10 0 [ 10, 20, 30, 40, 20 ]
20 1 [ 10, 20, 30, 40, 20 ]
30 2 [ 10, 20, 30, 40, 20 ]
40 3 [ 10, 20, 30, 40, 20 ]
20 4 [ 10, 20, 30, 40, 20 ]
***************************************************************************
let nums = [11, 20, 30, 47, 20];
console.log(nums.filter(n => n%2===0));
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
[ 20, 30, 20 ]
**************************************************************************
let nums = [11, 20, 30, 47, 20];
nums.filter(n => n%2===0)
    .forEach(n => {
        console.log(n);
    });
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
20
30
20
************************************************************************
let nums = [11, 20, 30, 47, 20];
nums.filter(n => n%2===0)
    .forEach(n => {
        console.log(n*2);
    });
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
40
60
40
****************************************************************************
let nums = [1, 2, 3, 4, 5, 6]
let result = nums.filter(n => n%2===0)
                 .map(n => n * 2)
                 .reduce((a,b) => a+b);
console.log(result);
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
24
