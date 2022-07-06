import string

letters = string.ascii_letters
letters_list = []
for i in range(0, 26):
    letters_list.append(letters[i])
    i += 1
print(letters_list)
print(len(letters_list))

def encoding_word(secret_word, shift_number):
    encoded_word = ""
    over_list_index = 0
    for i in secret_word:
        index = letters_list.index(i) + shift_number # not starting from 0
        if index < len(letters_list):
            encoded_word += letters_list[index]
        elif index >= len(letters_list):
            over_list_index += 1
            encoded_word += letters_list[over_list_index]
    return encoded_word

def decoding_word(encoded_word, shift_number):
    decoded_word = ""
    for i in encoded_word:
        index = letters_list.index(i) - shift_number 
        if index >= 0:
            decoded_word += letters_list[index]
        elif index < 0:
            adjusted_index = index - 1
            decoded_word += letters_list[adjusted_index]
    return decoded_word
         
#encoding_word("hellocoders", 9)
#decoding_word("qnuuxlxmnbc", 9)



cipher_in_progress = True


while cipher_in_progress == True:
    decision = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if decision.lower() == 'encode':
        message = input("Type your message:\n")
        shift_number = int(input("Type the shift number:\n"))
        decoded_word = encoding_word(message, shift_number)
        print(f"Here's the encoded result: {decoded_word}")
    elif decision.lower() == 'decode':
        message = input("Type your message:\n")
        shift_number = int(input("Type the shift number:\n"))
        encoded_word = decoding_word(message, shift_number)
        print(f"Here's the encoded result: {encoded_word}")
    else:
        print(f"I don't know that command: {decision}")

    yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if yes_or_no.lower() == 'yes':
        continue
    elif yes_or_no.lower() == 'no':
        cipher_in_progress = False
    else:
        print(f"I don't know what {yes_or_no} means, but I'll take that as a yes :)")
        continue




