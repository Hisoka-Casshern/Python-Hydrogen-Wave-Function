
# Python-Hydrogen-Wave-Function


**STAVI PRVU SLIKU**


<br />
Here I calculate and plot different electron probability density distributions for the Hydrogen Wave Function. The code is in Python, and only Numpy and Sympy are used to have better insight into different Legendre and Laguerre polynomials.

The wave function for a Hydrogen atom is given by:
<p>
$$
\Large \mathbf{\Psi_{nlm}(r, \theta, \phi)} = \mathbf{R_{nl}(r)} \cdot \mathbf{Y_{lm}(\theta, \phi)}
$$
</p>

Where:
- Ψ<sub>nlm</sub>(r, θ, φ) is the wave function of the hydrogen atom,
- R<sub>nl</sub>(r) is the radial component that depends on the principal quantum number \(n\) and the angular momentum quantum number \(l\),
- Y<sub>lm</sub>(θ, φ) is the spherical harmonic function that depends on the magnetic quantum number \(m\) and the angular coordinates θ (theta) and φ (phi).

<br />
The probability density is defined as:
<p>
$$
\large \mathbf{\rho} = |\mathbf{\Psi}|^2
$$
</p>

<br />
The full Normalized Radial Component of the Hydrogen Wave Function is given by :

<p>
$$
 \Large R_{nl}(r)= \sqrt{\left(\frac{2}{na_0}\right)^3 \frac{(n-l-1)!}{2n(n+l)!}} \cdot e^{-\frac{r}{na_0}} \cdot \left(\frac{2r}{na_0}\right)^l \cdot L_{n-l-1}^{2l+1}\left(\frac{2r}{na_0}\right) 
$$
</p>
where:
<br />
- n is the principal quantum number,
<br />
- l is the angular momentum quantum number,
<br />
- r is the radial distance,
<br />
- L<sub>(n-l-1)</sub><sup>(2l+1)</sup>(x) represents the associated Laguerre polynomial of degree (n-l-1) and order (2l+1) evaluated at the radius
<br />
- The other terms involve normalization and exponential decay

<br />
<br />
The full Normalized Angular Component of the Hydrogen Wave Function is given by :

<br />
<p>
$$
 \Large Y_{lm}(\theta, \phi) = \sqrt{\frac{(2l+1)}{4\pi} \frac{(l-m)!}{(l+m)!}} P_{l}^{m}(\cos(\theta)) e^{im\phi}
$$
</p>
where:
<br />
- l is the angular momentum quantum number,
<br />
- m is the magnetic quantum number
<br />
- θ is the polar and φ azimuthal angle
<br />
- P<sub>(l)</sub><sup>(m)</sup>cos(θ) is the associated Legendre polynomial of degree l and order m 
<br />
- The other terms involve normalization and rotations
<br />
<br />
<br />
Unlike most other scripts that utilize Scipy, here I implement my own Associated Legendre and Laguerre polynomials for the construction of Radial and Harmonic functions. 
<br />
The Associated Legendre polynomial is constructed from the Legendre polynomial using the following relation:
<br />
<p>
$$
 \large P_{l}^{m}(x) = (-1)^m(1-x^2)^{\frac{m}{2}} \frac{d^m}{dx^m}P_{l}(x) 
$$
</p>

where Legendre polynomials are defined by Bonnet's recursion formula:
<p>
$$
\large P_{l}(x) = \frac{2l-1}{l} x P_{l-1}(x) - \frac{l-1}{l} P_{l-2}(x) ,\; \;  with\; \;  P_{0}(x) = 1,\; \;  \quad P_{1}(x) = x
$$
</p>
Utilization of Sympy allows calculating m'th derivative of l'th Legendre polynomial and as such the derivative can be viewed (printed).
<br />
For example: setting l=8 , m=4 gives:
<p>
$$
\large P_{8}(x) = \frac{1}{128}(6435x^8 - 12012x^6 + 6930x^4 + 1260x^2 + 35)
$$ 
</p>
Printing out the 4'th derivative using symbolic differentiation gives:

<p>
$$
0.0803571428571429 \left(1 - x^2\right) \left(50050 x^2 \left(3x^2 - 1\right) + 3003 x^2 \left(5x^2 - 3\right) + 8580 x^2 \left(7x^2 - 3\right) + 27300 x^2 \left(11x^2 - 3\right) + 40425 x^2 \left(13x^2 - 3\right) - 13246 x^2 + 16170\right)
5)
$$ 
</p>

