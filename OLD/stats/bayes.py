# bayes
#Return the probability of A conditioned on B given that
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2
def f(p0,p1,p2):
    pb = p0*p1 + (1-p0)*(1-p2)
    return p0*p1 / pb

print f(0.1, 0.9, 0.8)
# 0.333


#Return the probability of A conditioned on Not B given that
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2
def g(p0, p1, p2):
    S = p0*(1-p1)
    pb = S + (1-p0)*p2
    return S / pb
