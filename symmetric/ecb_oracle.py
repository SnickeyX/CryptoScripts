import string
import requests
import time

# Change as per need
num_bytes_to_recover = 10

def encrypt(payload):
    url = "???"
    r = requests.get("url + payload usually") 
    return r.json()['ciphertext'] # or wtv the way to get CT is

def brute_force():
    flag = ""
    bits_to_recover = num_bytes_to_recover - 1 # 0-indexed
    alphabets = '_'+'@'+'}'+"{"+string.digits+string.ascii_lowercase+string.ascii_uppercase
    
    while(True):
        payload = 'a' * (bits_to_recover - len(flag))
        target = encrypt(payload.encode().hex())
        print("Exp", ' ', end="")
            
        for a in alphabets:
            trial = encrypt((payload + flag + a).encode().hex())  
            print(a, " ", end = '')

            if(trial[80:160] == target[80:160]):
                flag += a 
                print(flag)
                break 
            
            # Ensure that the server is not blocking us
            time.sleep(0.5)
                
        # Change as per need, usually flag ends with } 
        if flag.endswith("}"):
            print(flag)
            break 
        
if __name__== "__main__":
    brute_force() 