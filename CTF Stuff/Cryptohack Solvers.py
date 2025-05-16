from base64 import b64encode
from Crypto.Util.number import long_to_bytes
from pwn import xor
from Algorithms import gcd, extended_gcd

'''
print("".join(chr(o ^ 0x32) for o in [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]))
'''
'''
print("".join(chr(char) for char in [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]))
'''
'''
print(str(bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))[2:-1])
'''
'''
print(b64encode(bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")))
'''
'''
print(str(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))[2:-1])
'''
'''
print(str(xor("label", 13))[2:-1])
'''
'''
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2 = xor(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"), key1)
key3 = xor(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"), key2)
flag = xor(xor(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"), key1), xor(key2, key3))
print(str(flag)[2:-1])
'''
'''
for item in [str(xor(bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"), i.to_bytes(1, 'big'))) for i in range(256)]:
    if item[2:8] == "crypto":
        print(item[2:-1])
        '''
'''
print(str(xor(bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"), "myXORkey"))[2:-1])
'''
'''
print(gcd(66528, 52920))
'''
'''
print(min(extended_gcd(26513, 32321)[1:]))
'''
'''
print(min(11 % 6, 8146798528947 % 17))
'''
'''
print((273246787654 ** 65536) % 65537)
'''

