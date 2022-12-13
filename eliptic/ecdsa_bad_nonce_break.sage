import hashlib
from Crypto.Util.number import bytes_to_long
from ecdsa.ecdsa import generator_192

g = generator_192
n = int(g.order())

# Hash function depends on chall (sha1, sha256, sha512, etc.)
def sha1(data):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    return sha1_hash.digest()

# Possible messages with their signatures (>= 2)
out1 = {"msg": "msg1", "r": "0x??", "s": "0x??"}
out2 = {"msg": "msg2", "r": "0x??", "s": "0x??"}

msg1 = bytes_to_long(sha1(out1["msg"].encode()))
msg2 = bytes_to_long(sha1(out2["msg"].encode()))

r1 = int(out1["r"],16)
sig1_s = int(out1["s"],16)
s1_inv = inverse_mod(sig1_s, n)
r2 = int(out2["r"], 16)
sig2_s = int(out2["s"], 16)
s2_inv = inverse_mod(sig2_s, n)
 
matrix = Matrix([[n, 0, 0, 0], [0, n, 0, 0],
[r1*s1_inv, r2*s2_inv, (2^128) // n, 0],
[msg1*s1_inv, msg2*s2_inv, 0, 2^128]])

reduced_matrix = matrix.LLL(delta=0.75)
r1_inv = inverse_mod(r1, n)

nonce = 0 
private_key = 0 
# seraches for bad nonce -> derives private key from it (rate of failure is significant - lower with more signartures)
# privKey = (R.x)^-1 * (signature * nonce - hashed_msg) (mod n)
for row in reduced_matrix:
    potential_nonce_1 = row[0] % n
    potential_priv_key = (r1_inv * ((potential_nonce_1 * sig1_s) - msg1)) % n
    if(potential_nonce_1 == 0):
        continue
    potential_s = (inverse_mod(potential_nonce_1, n) * (msg1 + r1 * potential_priv_key)) % n
    if (potential_s == sig1_s):
        nonce = potential_nonce_1
        private_key = potential_priv_key
        print("found private key!")
        
print("I think the secret is: :", private_key)