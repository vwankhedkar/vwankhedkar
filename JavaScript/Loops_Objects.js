let i = 1;

while (i < 6)
{
    console.log("Hi ", i)
    i++;
}
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
Hi  1
Hi  2
Hi  3
Hi  4
Hi  5
*********************************************************************
let i = 10;

do
{
    console.log("Hi ", i)
    i++;
}
while (i <= 5)
OUTPUT -  10
************************************************************************
for (let i=0; i<3; i++)
{
    console.log("Hi", i)
    for (let j=0; j<3; j++)
        console.log("Hello", j);
}
OUTPUT
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
Hi 0
Hello 0
Hello 1
Hello 2
Hi 1
Hello 0
Hello 1
Hello 2
Hi 2
Hello 0
Hello 1
Hello 2
*******************************************************************
let i = 54672
while (i > 0)
{
        console.log(i % 10);
        i = parseInt(i / 10);
}
OUTPUT   PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
2
7
6
4
5
**********************************************************************
let input = 'name'

let alien = {
    name: 'Vaishali',
    tech: 'JS',
    'work exp': 4
}
console.log(alien);
console.log(alien.name);
console.log(alien['tech']);
console.log(alien['work exp']);

OUTPUT  - PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
{ name: 'Vaishali', tech: 'JS', 'work exp': 4 }
Vaishali
JS
4
*************************************************************************
let input = 'name'

let alien = {
    name: 'Vaishali',
    tech: 'JS',
    laptop: {
        cpu : 'i7',
        ram : 7,
        brand : 'Asus'
    }
}
console.log(alien);
console.log(alien.tech);
console.log(alien.laptop);
console.log(alien.laptop.brand);
OUTPUT -   PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
{
  name: 'Vaishali',
  tech: 'JS',
  laptop: { cpu: 'i7', ram: 7, brand: 'Asus' }
}
JS
{ cpu: 'i7', ram: 7, brand: 'Asus' }
Asus
*****************************************************************************
let input = 'name'

let alien = {
    name: 'Vaishali',
    tech: 'JS',
    laptop: {
        cpu : 'i7',
        ram : 7,
        brand : 'Asus'
    }
}
console.log(alien);
console.log(alien.tech);
console.log(alien.laptop);
console.log(alien.laptop.brand);
console.log(alien.laptop.brand.length);
console.log(alien.laptop.brand1?.length);   // ? print undefined if object not available like brand1 w/o giving an error

delete alien.laptop
console.log(alien);
OUTPUT
PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
{
  name: 'Vaishali',
  tech: 'JS',
  laptop: { cpu: 'i7', ram: 7, brand: 'Asus' }
}
JS
{ cpu: 'i7', ram: 7, brand: 'Asus' }
Asus
4
undefined
{ name: 'Vaishali', tech: 'JS' }
*******************************************************************************************
let input = 'name'

let alien = {
    name: 'Vaishali',
    tech: 'JS',
    laptop: {
        cpu : 'i7',
        ram : 7,
        brand : 'Asus'
    }
}

for (let key in alien)
{
    console.log(key, alien[key]);
}
OUTPUT  -  PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> node first.js
name Vaishali
tech JS
laptop { cpu: 'i7', ram: 7, brand: 'Asus' }
***********************************************************************************************
  

