import base64

def hex_to_base64(hex):
    return str(base64.b64encode(hex))[2:-1]

def fixed_xor(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:]

def main():
    # print(hex_to_base64(bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")))
    print(fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))

if __name__ == "__main__":
    main()
