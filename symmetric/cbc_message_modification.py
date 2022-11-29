# Exploit lack of integrity check in CBC mode with random IV
import codecs

input = "iv msg".split(' ')

actual = "<actual msg>"
target = "<modified msg>"

cipherIV = str(codecs.decode(input[0], 'hex'))
cipherMsg = (codecs.decode(input[1], 'hex'))


# xor two strings of different lengths
def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
    
    
paddingNum1 = str(len(cipherMsg) - len(actual))
padding1 = "".join(paddingNum1 * int(paddingNum1))


paddingNum2 = str(len(cipherMsg) - len(target))
padding2 = "".join(paddingNum2 * int(paddingNum2))


actual += padding1
target += padding2 

xorPT = strxor(actual, target)
newIV = strxor(cipherIV, xorPT)

# return the cbc cipher text of our modified msg 
print(codecs.encode(bytes(newIV, "ascii"), "hex"), input[1])

