# data.xml
<EmployeeData>
    <Employee>
        <Id>101</Id>
        <Name>John Doe</Name>
        <Department>Engineering</Department>
        <Salary>75000</Salary>
        <Active>true</Active>
    </Employee>
    <Employee>
        <Id>102</Id>
        <Name>Jane Smith</Name>
        <Department>Marketing</Department>
        <Salary>65000</Salary>
        <Active>false</Active>
    </Employee>
</EmployeeData>

# data.json
{
    "EmployeeData": {
        "Employee": [
            {
                "Id": "101",
                "Name": "John Doe",
                "Department": "Engineering",
                "Salary": "75000",
                "Active": "true"
            },
            {
                "Id": "102",
                "Name": "Jane Smith",
                "Department": "Marketing",
                "Salary": "65000",
                "Active": "false"
            }
        ]
    }
}

# xml_json_compare.py
import json
import xmltodict
def read_json(file_path):
    """Reads and returns a JSON file as a dictionary"""
    with open(file_path, 'r') as f:
        return json.load(f)
def read_xml(file_path):
    """Reads and returns an XML file as a dictionary"""
    with open(file_path, 'r') as f:
        return xmltodict.parse(f.read())
def compare_dicts(d1, d2, path=""):
    """Recursively compares two dictionaries and reports mismatches"""
    for key in d1:
        new_path = f"{path}/{key}" if path else key

        if key not in d2:
            print(f"❌ Missing key in second file: {new_path}")
            continue
        if isinstance(d1[key], dict) and isinstance(d2[key], dict):
            compare_dicts(d1[key], d2[key], new_path)
        elif isinstance(d1[key], list) and isinstance(d2[key], list):
            if len(d1[key]) != len(d2[key]):
                print(f"⚠️ Length mismatch at {new_path}: {len(d1[key])} vs {len(d2[key])}")
            for i in range(min(len(d1[key]), len(d2[key]))):
                compare_dicts(
                    d1[key][i] if isinstance(d1[key][i], dict) else {"value": d1[key][i]},
                    d2[key][i] if isinstance(d2[key][i], dict) else {"value": d2[key][i]},
                    f"{new_path}[{i}]"
                )
        else:
            if str(d1[key]).strip() != str(d2[key]).strip():
                print(f"❌ Value mismatch at {new_path}: {d1[key]} != {d2[key]}")
    # Check for extra keys in d2
    for key in d2:
        if key not in d1:
            print(f"⚠️ Extra key in second file: {path}/{key}")
# --- Example usage ---
xml_file = "data.xml"
json_file = "data.json"
xml_data = read_xml(xml_file)
json_data = read_json(json_file)
# Compare XML and JSON
compare_dicts(xml_data, json_data)
****************************************************************************************
import xmltodict
from pprint import pprint
import json
with open('data.xml','r') as f:
    data = xmltodict.parse(f.read())
pprint(data)
    # print(json.dumps(data, indent=4))
employees = data['EmployeeData']['Employee']
for emp in employees:
    print(emp['Department'])
    print(emp['Name'])
    print(emp['Salary'])
****************************************************************************************
import json
import xmltodict
with open('data.json','r') as f:
    data = json.load(f)
print(json.dumps(data, indent=3))
****************************************************************************************
  
