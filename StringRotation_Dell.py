lst = word.split()
lst2 = ''.join(lst)[::-1]
j=0
for i in range(len(word)):
    if word[i]==' ':
        print(word[i],end='')
        j+=1
    else:
        print(lst2[i-j],end='')
----------------------------------------------
strng = "I am Vaishali Mangulal Wankhedkar"
lst = strng.split()
lst2 = ''.join(lst)[::-1]
strng1 = ""
print("Original String: ", strng)
j = 0
for i in range(len(strng)):
   if strng[i] == ' ':
      strng1 += ' '
      j += 1
   else:
      strng1 += lst2[i-j]
print("Changed String: ",strng1)
print("Changed String: ",strng1.lower())
--------------------------------------------------------
Original String:  I am Vaishali Mangulal Wankhedkar
Changed String:  r ak dehknaWl alugnaMi lahsiaVmaI
Changed String:  r ak dehknawl alugnami lahsiavmai
