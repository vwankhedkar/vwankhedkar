function isEmpty(obj) {
    return Object.keys(obj).length == 0
}
console.log(isEmpty({}));
console.log(isEmpty({a : 1}))
(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\JavaScript> node .\try.js
true
false
*******************************************************************************************
function mergeObj(obj1, obj2) {
    return {...obj1, ...obj2}
}
console.log(mergeObj({a:1, b:2}, {b:3, c:4}))
(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\JavaScript> node .\try.js
{ a: 1, b: 3, c: 4 }
*******************************************************************************************
function cloneObj(obj) {
    return {...obj}
}
const original = {a:1, b:2}
const copy = cloneObj(original)
console.log(copy)
console.log(copy === original)
{ a: 1, b: 2 }
false
*******************************************************************************************
function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
}
const original = {a:1, b: {c : 2}};
const copy = deepClone(original)
console.log(copy)
console.log(copy.b === original.b)
{ a: 1, b: { c: 2 } }
false
*******************************************************************************************
function countProperties(obj) {
    return Object.keys(obj).length;
}
console.log(countProperties({a:1, b:2, c:3}))  ====>  3
*******************************************************************************************
const person = {
    name : 'Vais',
    Age : 30,
    city : 'Bangalore'
}
const keys = Object.keys(person);
const values = Object.values(person);
console.log(keys);
console.log(values)
[ 'name', 'Age', 'city' ]
[ 'Vais', 30, 'Bangalore' ]
*******************************************************************************************
function hasProperty(obj, key) {
    return obj.hasOwnProperty(key);
}
console.log(hasProperty({a:1, b:2}, 'a'));
console.log(hasProperty({a:1, b:2}, 'c'));
true
false
*******************************************************************************************
function objectToPairs(obj) {
    return Object.entries(obj);
}
console.log(objectToPairs({a:1, b:2, c:3}))
[ [ 'a', 1 ], [ 'b', 2 ], [ 'c', 3 ] ]
*******************************************************************************************
function getMethods(obj) {
    return Object.keys(obj).filter(key => typeof obj[key] === 'function')
}
const obj = {
    a : 1,
    b : 2,
    foo() {return 'foo'},
    bar() {return 'bar'}
};
console.log(getMethods(obj));
[ 'foo', 'bar' ]

*******************************************************************************************

*******************************************************************************************



  
