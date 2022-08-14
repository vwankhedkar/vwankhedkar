# importing the module
import re
# opening and reading the file
with open('pythonfile.txt') as fh:
    fstring = fh.readlines()
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# initializing the list object
lst = []
# extracting the IP addresses
for line in fstring:
    lst.append(pattern.search(line)[0])
# displaying the extracted IP addresses
print(lst)
OUTPUT:
['192.168.10.104', '192.168.10.112', '192.168.10.1']
*******************************************************************
# importing the module
import re

# opening and reading the file
with open('pythonfile.txt') as fh:
    string = fh.readlines()

# declaring the regex pattern for IP addresses
pattern = re.compile('''((25[0-5]|2[0-4][0-9]|([0-2][0-9][0-9])?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1][0-9]?[0-9]?)''')
# initializing the list objects
valid = []
invalid = []
# extracting the IP addresses
for line in string:
    line = line.rstrip()
    result = pattern.search(line)
    print(line, result)
    # valid IP addresses
    if result:
        valid.append(line)

    # invalid IP addresses
    else:
        invalid.append(line)

# displaying the IP addresses
print("Valid IPs")
print(valid)
print("Invalid IPs")
print(invalid)
OUTPUT:
192.168.1.1 None
192.168.4.164 None
0000.000.00.00 None
69.168.4.226 None
255.252.252.250 <re.Match object; span=(0, 15), match='255.252.252.250'>
Valid IPs
['255.252.252.250']
Invalid IPs
['192.168.1.1', '192.168.4.164', '0000.000.00.00', '69.168.4.226']
