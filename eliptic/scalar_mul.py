from point_addition import pt_add

# to calculate nP
def simple_scalar_mul(P, n, p):
    R = (0,0)
    x,y = P
    Q = (x,y)
    while n > 0:
        if(n % 2 == 1):
            R = pt_add(R, Q, p)
        Q = pt_add(Q, Q, p)
        n = n // 2 
    return R

# TODO: implement more efficient scalar multiplication

if __name__ == "__main__":
    #example usage 
    p = 9739
    P = (5274, 2841)
    n = 3
    print(simple_scalar_mul(P, n, p))
    
    P = (493, 5564)
    n = 5
    print(simple_scalar_mul(P, n, p))
