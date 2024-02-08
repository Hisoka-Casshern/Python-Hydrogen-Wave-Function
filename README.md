# Python-Hydrogen-Wave-Function

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
The full Normalized Radial Component of the Hydrogen Wave Function is given as :

<p>
$$
 \Large R_{nl}(r)= \sqrt{\left(\frac{2}{n}\right)^3 \frac{(n-l-1)!}{2n[(n+l)!]^3}} \cdot e^{-\frac{r}{n}} \cdot \left(\frac{2r}{n}\right)^l \cdot L_{n-l-1}^{2l+1}\left(\frac{2r}{n}\right) 
$$
</p>

