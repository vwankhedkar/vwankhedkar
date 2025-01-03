s='VMWABCABCABA'
i=s.find('ABC') #find first occurance of ABC
print(i)
i=s.find('ABC',4,10) #from index 4th to 9th
print(i)
i=s.find('ABC',9,11) #from index 9th
print(i)
OUTPUT - 3
6
-1
**********************************************************
s='VMWABCABCABCAB'
subs='ABC'
i = s.find(subs)
if i == -1:
    print('Substring not found')
while i != -1:
    print('{} substring present at index {} '.format(subs, i))
    i = s.find(subs,i+len(subs),len(s))
OUTPUT
ABC substring present at index 3 
ABC substring present at index 6 
ABC substring present at index 9 
***********************************************************
s='VMWABCABCABCAB'
subs=input('Enter substring to search: ')
i=s.find(subs)
if i==-1:
    print('Specified substring not found')
count=0
while i != -1:
    count += 1
    print('{} Present at index {}'.format(subs, i))
    i = s.find(subs,i+len(subs),len(s))
print('No of occurances :',count)
OUTPUT
Enter substring to search: ABC
ABC Present at index 3
ABC Present at index 6
ABC Present at index 9
No of occurances : 3

Enter substring to search: PQR
Specified substring not found
No of occurances : 0
********************************************************************