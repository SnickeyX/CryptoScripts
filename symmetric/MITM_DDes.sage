#!/usr/bin/python3 -u
from Crypto.Cipher import DES
import binascii
import itertools
import random
import string

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

FLAG = "1a51092ab788d129f0ead1a68ebe6f9721a89b90a6644d3aaa04add9247a873813b8bcb8d772a742"

def double_encrypt(m):
    msg = pad(m)

    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    return binascii.hexlify(cipher2.encrypt(enc_msg)).decode()

def E(m, key):
    msg = pad(m)
    cipher1 = DES.new(key, DES.MODE_ECB)
    return binascii.hexlify(cipher1.encrypt(msg)).decode()

def D(c, key):
    cipher1 = DES.new(key, DES.MODE_ECB)
    return binascii.hexlify(cipher1.decrypt(c)).decode()
    
def meet_in_the_middle(C, P):
    C = binascii.unhexlify(C)
    table = {}
    for i in range(0, 2^bits):
        table[E(P, pad(str(i)))] = pad(str(i))
    for i in range(0, 2^bits):
        if D(C, pad(str(i))) in table:
            return table[D(C, pad(str(i)))], pad(str(i))

k1,k2 = meet_in_the_middle("put_in_encryption_on_the_right_here", "hellothereobiwan")
print(k1,k2)

M = D(binascii.unhexlify(FLAG), k2)
P = D(binascii.unhexlify(M), k1)
print(P)