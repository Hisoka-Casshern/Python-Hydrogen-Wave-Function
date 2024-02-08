import sympy 
import numpy as np

def factorial(num:int):
    '''helper function'''
    if(num == 1 or num == 0):
        return 1
    else:
        return num*(factorial(num-1))
    
def LegendrePolynomial(l):
    '''This function constructs a nth Legendre Polynomial at desired l(n)
    using sympy such as to be able to diferentiate it later'''
    x = sympy.symbols('x')
    # we set the first two polynomials and recursivly evaluted for larger n
    # zeroth degree is just 1
    if(l == 0 ):
        return sympy.Integer(1)
    elif(l == 1):
        # first order is a line
        return x
    else:
        #else we get legendre polynomials at n-1 and n-2 and calculte nth
        C1 = (((2 * l - 1)/l)*x)
        C2 = ((l - 1)/l)
        NthDegree = (C1*(LegendrePolynomial(l = l-1))-C2*(LegendrePolynomial(l = l-2)))
        return NthDegree

def AssociatedLegendrePolynomial(l:int,m:int,r:float, printSympyFormula:bool = False):
    '''Associated Legendre polynomial function that evalutes the specific 
    legendre nth polynomial (l) and the degereneracy m at point r, this function performes firstly 
    some operatiosn in numpy before converting to symp as sympy is slower'''

    #set symbols
    x = sympy.symbols('x')
    #make local l and m and second coefficent to account for negative values
    numpyLocalL = l
    localM = sympy.Integer(m)  
    #calculate first coefficent
    C1 = (((-1)**np.abs(m)))*(1.-r**2)**(np.abs(m)/2)
    #C1 = (((-1)**sympy.Abs(localM)))*(1.-localR**2)**(sympy.Abs(localM)/2)
    #calculate second coefficent
    C2 = np.float64(1.)
    #check special case when polynomial is zero and return zero
    if(np.abs(m)>l):
        return 0.
    #check if l is negative
    if(l<0):
        numpyLocalL = np.abs(l) - 1
    #now check if m less than zero and if so recalculate second coefficent
    if(m<0):
        C2 = np.float64(((-1)**np.abs(m))*(factorial(numpyLocalL-np.abs(m))/factorial(numpyLocalL+np.abs(m))))
        #C2 = ((-1)**sympy.Abs(localM))*(factorial(localL-sympy.Abs(localM))/factorial(localL+sympy.Abs(localM)))
    #calculate the nth(l) Legendre Polynomial
    #convert to symp matrix
    sympyLocalL = sympy.Integer(numpyLocalL)
    LthLengendreAtX = LegendrePolynomial(sympyLocalL) 
    #now diferentiate it m times  
    MthDerivativeOfLthLengdreAtX = sympy.diff(LthLengendreAtX,x,sympy.Integer(sympy.Abs(localM)))
    #if desired Legendre to be printed
    if(printSympyFormula == True):
        A = (((-1)**sympy.Abs(m))) * (1 - x**2)**(sympy.Abs(m)/2)
        if(m>=0):
            B = sympy.Float(1.)
        else:
            B = sympy.Float(((-1)**sympy.Abs(m))*(factorial(sympyLocalL-sympy.Abs(m))/factorial(sympyLocalL+sympy.Abs(m))))
        C = MthDerivativeOfLthLengdreAtX
        formula = A * B * C
        sympy.pprint(formula)

    #create a function independant of sympy
    MthDerivativeOfLthLengdreAtX = sympy.lambdify(x,MthDerivativeOfLthLengdreAtX ,'numpy')
    #finally evaluate derivative at x=r 
    C3 = MthDerivativeOfLthLengdreAtX(r)


    #return the associated legndre_l_m evaluted at r
    return C1*C2*C3

