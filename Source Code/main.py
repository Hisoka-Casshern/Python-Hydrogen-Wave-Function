from NormalizedWaveFunctionScript import WaveFunction2D
import matplotlib.pyplot as plt

if  __name__ == '__main__':
    '''main script that runs WafeFunction2D calculations and
    afterwards plots the 2d plot of probaility density distribution,
    here the principal quantum numbers can be set'''

    #set quantum numbers
    n, l, m_l = 9,7,2

    #set resolution 
    boxDimension = 500
    boxResultion = 1000

    #plot scale
    plotScale = 0.08

    #calculate probability density
    _,ProbabilityDensity = WaveFunction2D(n=n, 
                                          l=l, 
                                          m_l=m_l, 
                                          SquareBoxHalfSideSize=boxDimension,
                                          ResolutionInisideBox=boxResultion,
                                          plotScale = plotScale,
                                          printAssociatedLengedre=True)
    
    #plot settings and plot
    fig, ax = plt.subplots(figsize=(8,8)) 
    cmapStyle = 'hot'
    title_font = {
        'family': 'serif',
        'color':  'white',
        'weight': 'bold',  
        'size': 16,        
    }
    colorbar_font = {
        'family': 'serif',
        'color':  'white',
        'weight': 'bold', 
        'size': 12,       
    }
    ax.set_title(f'\n     Hydrogen Atom  \n\n WaveFunction Electron Density Solution for : \n n = {n}, l = {l}, m$_l$ = {m_l}',
                fontdict=title_font)
    ax.text(980, 850, '    lower \nprobability', fontdict=colorbar_font)
    ax.text(980, 250, '   higher\nprobability', fontdict=colorbar_font)
    fig.patch.set_facecolor('black')
    im = ax.imshow(ProbabilityDensity,cmap = cmapStyle)
    cbar = plt.colorbar(im, fraction=0.02)
    cbar.set_ticks([])
    plt.show()
    