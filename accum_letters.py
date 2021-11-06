# def accum(s):
#     return '-'.join((a * i).title() for i, a in enumerate(s, 1))

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]

if __name__ == '__main__':
    # s = accum("abcd")
    s = accum("RqaEzty")
    print(s)
