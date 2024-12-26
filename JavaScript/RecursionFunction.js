function show() {
    console.log("Hi");
}
show();
OUTPUT - Hi
************************************
function show() {
    console.log("Hi");
}
function abc() {
    show();
}
abc();
OUTPUT - Hi
*********************************
function fact(n) {
    if (n == 0)
        return 1;
    else
        return n * fact(n-1);
}
let n = 5;
let result = fact(n)
console.log(result)
OUTPUT - 120
