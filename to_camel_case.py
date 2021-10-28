def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("abcd_efgh_ijkl"))

