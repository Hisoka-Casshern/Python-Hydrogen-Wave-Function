from NormalizedRadialScript import RadialPartOfWaveFunction
from NormalizedAngularScript import AngularPartOfWaveFunction
import numpy as np

def WaveFunction2D(n:int,l:int,m_l:int,SquareBoxHalfSideSize:int=500,ResolutionInisideBox:int=1000,plotScale:float = 0.5,
                   printAssociatedLengedre :bool =False):
    '''this function evalutes a wave function on the 2d volume defined by SquareBoxHalfSideSize*2,
    Resolution is used to increase the point density inside the 2d volume. Returns a numpy array of all
    values, also retruns probability density'''

    #define Bohr radius
    VacuumPermitivity = 8.8541878128 * 1e-12 # F*m^-1S
    ElectronMass = 9.1093837 * 1e-31 #kg
    ElectronCharge = 1.602176623 * 1e-19 #C
    ReducedPlanckConstant =( 6.62607015 * 1e-34)/(2.*np.pi) # Js
    a0 = (4.*np.pi*VacuumPermitivity*np.power(ReducedPlanckConstant,2))\
               /(np.power(ElectronCharge,2)*ElectronMass) #meters
    #scale it to accomodate box units
    scale = 10 * 1e+11 * plotScale
    a0Scaled = a0 * scale

    
    #create a 2d meshgrid of points
    x = np.linspace(-SquareBoxHalfSideSize,SquareBoxHalfSideSize,ResolutionInisideBox)
    y = np.linspace(-SquareBoxHalfSideSize,SquareBoxHalfSideSize,ResolutionInisideBox)
    X,Y = np.meshgrid(x,y)

    #calculate the wave function at given points
    R = np.sqrt(np.power(X,2)+np.power(Y,2))
    Theta = np.arctan(X/(Y+0.00000001))
    Phi = 0.
    WaveFunction = RadialPartOfWaveFunction(radius=R,n=n,l=l,a0=a0Scaled) *\
                        AngularPartOfWaveFunction(l=l,m_l=m_l,theta=Theta,phi=Phi,
                                        printAssociatedLengedre=printAssociatedLengedre)

    #determine probability density
    ProbabilityDensity = np.power(np.abs(WaveFunction),2)
    ProbabilityDensity = np.sqrt(ProbabilityDensity)
    
    return WaveFunction, ProbabilityDensity

