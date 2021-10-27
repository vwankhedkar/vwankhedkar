a = [1,2,1,1,3,4,5,3]

freq = {}
for i in a:
    freq[i] = freq.get(i,0)+1

i = 0
for key in sorted(freq.keys()):
    # print (key)
    val = freq.get(key)
    print(key, "occured", val, "times")
    while val > 0:
        a[i] = key 
        i = i + 1
        val = val - 1
print(a)
