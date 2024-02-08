from LaguerrePolynomialScript import Laugerre
import numpy as np


def factorial(num:int):
    '''helper function'''
    if(num == 1 or num == 0):
        return 1
    else:
        return num*(factorial(num-1))

def RadialPartOfWaveFunction(radius:float, n:int, l:int, a0:float):
    '''main function to calculate radial part of wave function, a0 is Bohr radius'''
    #first calcuate the normalization constant
    X = (2.*radius)/(n*a0)
    C = np.sqrt((np.power(((2.)/(n*a0)),3)) * \
                ((factorial(n-l-1))/(factorial(n+l)*2*n))) * np.exp(-(X/2.)) * np.power(X,l)
    #then the Laguerre polynomial
    L = Laugerre(alpha=(2*l+1),n=(n-l-1),x=X)
    #finally the radial function
    R_nlr = C*L
    return R_nlr
    