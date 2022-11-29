# Point addition for elliptic curves over finite fields
# Change the value of a,b in Y^2 = X^3 + aX + b and p in Fp
# Change x1,x2 and y1,y2 for P = (x1,y1) and Q = (x2,y2)
from Crypto.Util.number import inverse

# Change as per need! 
a = 497
b = 1768 

def pt_add(P, Q, p):
    zero = (0,0)
    # Check if P or Q = zero
    if P == zero:
        return Q 
    if Q == zero:
        return P 
    # Check if P = -Q
    x1,y1 = P
    x2,y2 = Q
    if x1 == x2 and y1 == (-y2 % p):
        return zero
    # Check if P = Q or P /= Q, then use formulas for point addition
    lab = 0
    if x1 == x2 and y1 == y2:
        lab = ((3 * x1 * x1 + a) * inverse(2 * y1, p)) % p
    else:
        lab = ((y2 - y1) * inverse(x2 - x1, p)) % p
    x3 = (lab * lab - x1 - x2) % p
    y3 = (lab * (x1 - x3) - y1) % p
    # Return R
    return (x3,y3)
    
        
    
if __name__ == "__main__":
    #example usage 
    p = 9739
    P = (5274, 2841)
    Q = (8669, 740)
    print(pt_add(P, P, p))
    
    P = (493, 5564)
    Q = (1539, 4742)
    R = (4403,5202)
    S = pt_add(pt_add(pt_add(P, P, p), Q, p),R, p) 
    print(S)
    