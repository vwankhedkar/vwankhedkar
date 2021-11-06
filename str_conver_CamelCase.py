def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
    
def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''

from re import compile as reCompile
PATTERN = reCompile(r'(?i)[-_]([a-z])')
def to_camel_case(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)

import re
word_regex_pattern = re.compile("[^A-Za-z]+")

def to_camel_case(text):
    words = word_regex_pattern.split(text)
    return "".join(w.lower() if i is 0 else w.title() for i, w in enumerate(words))
    
if __name__ == '__main__':
    # s = accum("abcd")
    s = accum("RqaEzty")
    print(s)
**********************************************************************************

test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
