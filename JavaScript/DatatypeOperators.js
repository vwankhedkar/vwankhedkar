let num = 6
let firstname = "Vaishali"
let lastname = "Wankhedkar"
let user = firstname+ " " +lastname
let user1 = 'vaishali "Wankhedkar"'
let user2 = "vaishali \"Wankhedkar\""
let user3 = "vaishali \n Wankhedkar"
let user4 = "vaishali \v Wankhedkar"
let user5 = "vaishali\tWankhedkar"
let user6 = "vaishali\bWankhedkar"
let bool = 5<6
let nul = null
let abc
console.log(num, typeof num)
console.log(firstname, typeof firstname)
console.log(user, typeof user)
console.log(user1)
console.log(user2)
console.log(user3)
console.log(user4)
console.log(user5)
console.log(user6)
console.log(bool, typeof bool)
console.log(nul, typeof nul)
console.log(abc, typeof abc)
console.log(typeof (5 / "vais"))
console.log(typeof 5 / "vais")

OUTPUT
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
6 number
Vaishali string
Vaishali Wankhedkar string
vaishali "Wankhedkar"
vaishali "Wankhedkar"
vaishali
 Wankhedkar
vaishali
 Wankhedkar
vaishali        Wankhedkar
vaishalWankhedkar
true boolean
null object
undefined undefined
number
NaN
************************************************************
let str = "6"
let num = Number("123")
let x
console.log(str, typeof str)
console.log(num, typeof num)
console.log(x, typeof x)
x = 9
x = x + ""
console.log(x, typeof x)
x = x - 2
console.log(x, typeof x)
x = +x + 2
console.log(x)
x = !x
console.log(x, typeof x)
console.log(-7, typeof -7)
console.log(Boolean(0))
console.log(Boolean(-8))
console.log(Boolean(null))
console.log(Boolean(undefined))
console.log(Boolean("Vais"))
let y = parseInt("123 vais")
console.log(y)

OUTPUT -
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
6 string
123 number
undefined undefined
9 string
7 number
9
false boolean
-7 number
false
true
false
false
true
123
***************************************************************
num1 = true
num2 = true
num = num1 + num2 // + converts to number true is 1 and false is 0
console.log(num , typeof num)

OUTPUT -  2 number
***************************************************************
let num = 4
let x = num++ // post increment
console.log(x, num)
let y = ++num// post increment
console.log(y, num)

OUTPUT - 4 5
6 6
****************************************************************
let num = 4
let x = Math.pow(num, 4) // = 4 ** 4
console.log(x)

OUTPUT - 256


