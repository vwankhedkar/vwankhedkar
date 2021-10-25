def str_to_paren(str):
    str_dir = {}
    for ch in str:
        if ch in str_dir:
            str_dir[ch] += 1
        else:
            str_dir[ch] = 1
    return str_dir

if __name__ == '__main__':
    str = "ababdede"
    print(str_to_paren(str))
