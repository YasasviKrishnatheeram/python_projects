alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

ask_user = input("Type 'encode' to encode or 'decode' to decode: \n").lower()
message = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

# print(message[0])
# print(message.index("h"))


def encode(message, shift):
    encoded_message = ""
    for letter in message:
        if letter == " ":
            encoded_message[message.index(" ")] = " "

        index = alphabet.index(letter)
        new_index = index + shift
        encoded_message += alphabet[new_index]
    print(f"The encoded message is {encoded_message}")


def decode(message, shift):
    decoded_message = ""
    for letter in message:
        index = alphabet.index(letter)
        new_index = index - shift
        decoded_message += alphabet[new_index]
    print(f"The encoded message is {decoded_message}")


if ask_user == "encode":
    encode(message, shift)
else:
    decode(message,shift)
