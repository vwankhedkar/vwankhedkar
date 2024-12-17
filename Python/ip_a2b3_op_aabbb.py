def expand_string(input_str):
    result = ""
    i = 0
    while i < len(input_str):
        if input_str[i].isalpha():
            if i + 1 < len(input_str) and input_str[i+1].isdigit():
                result += input_str[i] * int(input_str[i+1])
                i += 2
            else:
                result += input_str[i]
                i += 1
        else:
            i += 1
    return result

# Input string
input_str = "awq2b3c3"

# Calling the function and printing the result
output = expand_string(input_str)
print(output)

OUTPUT - awqqbbbccc
