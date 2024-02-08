#Function that computes the n degree Laugerre Polynomial evaluated
#at the point x, alpha can be any set constant

def Laugerre(alpha:int,n:int,x:float):
    #recursive formula
    #we set the first two polynomials and recursivly evaluted for larger n    
    ZerothDegree = 1.
    FirstDegree = 1. + alpha - x
    if(n == 0):
        return ZerothDegree
    elif(n == 1):
        return FirstDegree
    else:
        #constants for iterative calculations of Legurre    
        C1 = 2*n -1. + alpha - x
        C2 = n - 1. + alpha
        NMinus1Degree = Laugerre(alpha = alpha,n = n-1, x = x)
        NMinus2Degree = Laugerre(alpha = alpha,n = n-2, x = x)
        NthDegree = (C1 * NMinus1Degree - C2 * NMinus2Degree) / n
        return NthDegree
