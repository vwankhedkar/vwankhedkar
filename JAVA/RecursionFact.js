let num=1;
function show() {
    console.log("Hi Welcome...", num);
    num++ ;
    if (num <= 5)
        show()
}
show()
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
Hi Welcome... 1
Hi Welcome... 2
Hi Welcome... 3
Hi Welcome... 4
Hi Welcome... 5
**********************************************************************************
function fact(n){
    if (n==0)
        return 1;
    else
    return n * fact(n-1)
}
let num=5;   // num = 170 is the last number to try
let result = fact(num)
console.log(result)
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js 
120
***********************************************************************

