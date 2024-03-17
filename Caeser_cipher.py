
# complete custom additive cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def cypher(message, shift):
    if en == "encode":
        for char in message:
            pos = alphabet.index(char)
            new_pos = pos + shift
            if new_pos> len(alphabet):
                while new_pos>51:
                    new_pos -=52
            new_text = alphabet[new_pos]
            print(new_text, end="")
    else:
        for char in message:
            pos = alphabet.index(char)
            new_pos = pos - shift
            if new_pos> len(alphabet):
                while new_pos>1:
                    new_pos =52-new_pos
            new_text = alphabet[new_pos]
            print(new_text, end="")


en = input("enter encode to encrypt and decode to decrypt: ")
text = input("enter a message: ")
key = int(input("enter a key: "))
key = key % 51
cypher(message=text, shift=key)
