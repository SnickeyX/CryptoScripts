import urllib.request as request
import urllib.error as error 
# Padding used: PKCS#7
# CBC mode used with random IV 
CIPHER =  "<to_insert>"
TARGET = '<url>'
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------

class PaddingOracle(object):
    def query(self, q):
        req = request.Request(TARGET + q)
        try:
            # Wait for response
            f = request.urlopen(req)          
        except error.HTTPError as e:          
            print ("We got: %d",e.code)  
            # Print response code
            # TODO: add response for good padding 
            return False # bad padding
        
    def decrypt_by_request(self, IV, cipher_block):
        final = list()
        for curr_byte in range(1,17):    # Going from last byte to first byte
            newIV = list(IV)
            print("figuring out byte " + str((17-curr_byte)))
            # adding padding for the last (x-1) bytes
            for cb_itr in range(curr_byte-1):              
                 # xor-ing with the known last byte(s) of the cipher_block
                 newIV[-(cb_itr+1)] ^= curr_byte ^ final[cb_itr]     
            newIV[-curr_byte] ^= curr_byte
            for g in range(0,256): # guesses 
                newIV[-curr_byte] ^= g ^ (0 if g == 0 else (g-1))
                print(newIV)
                print(newIV[-curr_byte])
                if(self.query( bytes(newIV).hex() + cipher_block.hex())):
                    print("g is " +  str(g))
                    final.append(g)
                    break
        final.reverse()
        return bytes(final)
                
        
    def decrypt(self, ciphertext):
        bytes_CT = bytes.fromhex(ciphertext)
        final = bytes()
        for i in range(1, len(bytes_CT)//16 - 1):
            print("Deciphering block number :" + str(i))
            left_block  = bytes_CT[(i-1)*16 : i * 16]
            right_bLock = bytes_CT[i * 16 : (i+1) * 16] 
            final = final + self.decrypt_by_request(left_block, right_bLock)
        
        return final.decode("utf-8") # return the decrypted plaintext *assumed utf-8* (change as per need)

if __name__ == "__main__":
    po = PaddingOracle()
    plain_text = po.decrypt(CIPHER)
    print(plain_text)