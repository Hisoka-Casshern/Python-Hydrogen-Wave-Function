from LegendrePolynomialScript import AssociatedLegendrePolynomial as Legendre
from NormalizedRadialScript import factorial
import numpy as np

def AngularPartOfWaveFunction(l:int,m_l:int,theta:float,phi:float,
                              printAssociatedLengedre:bool = False):
    '''returns a spherical harmonic evaluated at theta and phi'''
    #first calculate the normalization constant
    if(m_l<0):
        m_l=np.float64(m_l)
    C = np.power(-1,m_l)*np.sqrt(((2*l+1)/(4*np.pi))*\
        (factorial(l-m_l)/factorial(l+m_l)))*np.real(np.exp(1.j * m_l *phi))

    #the legendre polynomial
    r = np.cos(theta)
    L = Legendre(l=l,m=m_l,r=r,printSympyFormula=printAssociatedLengedre)
    Harmonic = L*C
    return Harmonic

