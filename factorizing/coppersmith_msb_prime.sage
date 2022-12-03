# coppersmith with msb(s) of p are known 
e = 65537
n = ??
# as defined in May'03
pbar = ??
F.<x> = PolynomialRing(Zmod(N), implementation='NTL'); 
# univariate poly as defined in thm 10 chap3 - May RSA thesis
f = x + pbar
# mess around with beta and epsilon if it doesn't work
x0 = f.small_roots(epsilon = 0.49/7, beta=0.49)
f_x0 = pbar + x0[0]
p = gcd(f_x0, N)
# // is important! primes are integers! (not rationals.....duh)
q1  = N // int(p)