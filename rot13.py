def rot13(message):
    encrypt=''
    uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in message:
        if i.isalnum() or i.isdigit() or i== " "or'.':
            encrypt+=i
        elif i in uppercase_list:
            new_val = uppercase_list.index(i)+13
            if new_val>=26:
                new_val = new_val % 26
                encrypt+=uppercase_list[new_val]
        else:
            new_val = lowercase_list.index(i)+13
            if new_val>=26:
                new_val = new_val % 26
                encrypt+=lowercase_list[new_val]
    return encrypt
            